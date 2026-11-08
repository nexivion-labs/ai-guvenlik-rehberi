# 6. Tedarik zinciri: npm, pip ve eklentiler

[← İçindekiler](../README.md) · Örnekler: [ornekler/npmrc](../ornekler/npmrc) · [ornekler/vscode-extensions-allowed.jsonc](../ornekler/vscode-extensions-allowed.jsonc)

Ajanlar paket kurmayı çok kolaylaştırır: "şu kütüphaneyi ekle" demek yeter. Bu kolaylık, tedarik zinciri saldırılarının da kapısıdır. 2026'da bile yaygın kullanılan paketlerin bakımcı hesapları ele geçirildi ve birkaç saat boyunca zararlı sürümler yayımlandı. Bu saatlerde `npm install` çalıştıran herkes etkilendi.

Saldırıların çoğu iki varsayıma dayanır: (1) yeni sürümü hemen kurarsınız, (2) paket yöneticisi kurulum betiğini otomatik çalıştırır. Aşağıdaki ayarlar ikisini de kırar.

---

## 6.1 npm

npm 11.10 ve üzeri sürümlerde proje köküne bir `.npmrc` dosyası koyun:

```ini
# Kurulum betiklerini (preinstall, install, postinstall) çalıştırma
ignore-scripts=true

# Git kaynaklı bağımlılıkları reddet (yalnız kök package.json'daki doğrudan bağımlılıklara izin ver)
allow-git=root

# Yayımlanmasının üzerinden en az 7 gün geçmemiş sürümleri kurma
min-release-age=7

# Sürümleri ^ ya da ~ olmadan, tam olarak kaydet
save-exact=true
```

Hazır dosya: [ornekler/npmrc](../ornekler/npmrc) (depoya `.npmrc` adıyla koyun).

- Bazı paketler kurulum betiğine gerçekten ihtiyaç duyar (`sharp`, `esbuild`, `bcrypt` gibi yerel modüller). Önce betiksiz kurun, sonra yalnız güvendiklerinizi derleyin: `npm ci --ignore-scripts && npm rebuild sharp esbuild`.
- **npm 12 (Temmuz 2026) ile varsayılanlar değişti.** `npm --version` ile sürümünüze bakın:
  - **npm 12 ve üzeri:** Bağımlılıkların kurulum betikleri **varsayılan olarak çalışmaz**; `allow-git` ve `allow-remote` varsayılanı `none`. Betiğe gerçekten ihtiyaç duyan paketleri tek tek onaylarsınız: `npm approve-scripts --allow-scripts-pending` bekleyenleri listeler, `npm approve-scripts <paket>` onaylar (varsayılan olarak sürüme sabitlenir ve `package.json`'a yazılır), `npm deny-scripts <paket>` reddeder. Bu sürümde `.npmrc`'deki `ignore-scripts=true` satırını **kaldırın**; yoksa onay listesini ezer ve onayladığınız betikler de çalışmaz.
  - **npm 11.10–11.x:** Yukarıdaki `.npmrc` ayarları geçerlidir. npm 11.16+ betikleri henüz engellemez ama kurulum sonunda incelenmemiş betiği olan paketleri listeler; npm 12'ye hazırlanmak için bu uyarıları okuyun.
  - **npm 11.10 altı:** `allow-git` ve `min-release-age` yoktur; önce npm'i güncelleyin.
- **Yayın token'ları:** GitHub, 2FA'yı atlayan npm token'larıyla yayın yetkisini kademeli olarak kaldırıyor (Ağustos 2026 ve Ocak 2027). Otomatik yayın için uzun ömürlü token yerine **trusted publishing (OIDC)** ya da insan onaylı aşamalı yayın kullanın.
- **CI'da** `npm install` değil, kilit dosyasına sadık kalan `npm ci` kullanın. `package-lock.json` her zaman commit edilsin ve PR'larda kilit dosyası değişiklikleri incelensin.
- `npx bir-paket` komutu paketi indirip hemen çalıştırır. Ajanın önerdiği `npx` komutlarını da kurulum gibi değerlendirin; sürümü sabitleyin.

## 6.2 pnpm, Yarn, Bun ve Python

| Araç | Betikleri kapatma | Yeni sürümü bekletme |
|---|---|---|
| pnpm (10.16+) | Bağımlılık betikleri varsayılan olarak kapalı; izinliler `onlyBuiltDependencies` ile | `minimumReleaseAge` (dakika; 7 gün = 10080) |
| Yarn (Berry) | `enableScripts: false` | `npmMinimalAgeGate` |
| Bun | Varsayılan olarak yalnız `trustedDependencies` | `minimumReleaseAge` (saniye) |
| pip | Kaynaktan derleme kod çalıştırabilir; `--only-binary :all:` ile yalnız hazır paket | — (sürüm sabitleme ve hash ile) |

Python için:

```bash
# Sürümleri ve hash'leri sabitleyin
pip install --require-hashes -r requirements.txt
# Sanal ortam dışında global kurulum yapmayın
python -m venv .venv
```

`pip install` öncesinde paket adını PyPI'de kontrol edin; harf hatasıyla benzer adlı zararlı paketler (typosquatting) yaygındır. Ajanın "bu paketi kur" önerisinde paket adını özellikle doğrulayın: araştırmalara göre ajanların önerdiği paket adlarının yaklaşık beşte biri uydurmadır ve saldırganlar bu adları önceden kaydeder (slopsquatting, [Bölüm 14.1](14-ajanin-yazdigi-kod.md#141-sayılar)).

## 6.3 VS Code eklenti izin listesi

VS Code 1.96 ve üzerinde `extensions.allowed` ayarıyla yalnız belirli yayıncıların ya da eklentilerin kurulmasına izin verebilirsiniz. Listede olmayan eklentiler kurulamaz; kuruluysa devre dışı kalır.

```jsonc
"extensions.allowed": {
  "*": false,                              // Varsayılan: hiçbir şey
  "microsoft": true,                       // Bir yayıncının tüm eklentileri
  "github": true,
  "anthropic.claude-code": true,           // Tek bir eklenti
  "esbenp.prettier-vscode": "stable"       // Yalnız kararlı sürümler
}
```

Hazır dosya: [ornekler/vscode-extensions-allowed.jsonc](../ornekler/vscode-extensions-allowed.jsonc). Eklenti kimliklerini kendi onaylı listenize göre düzenleyin.

- Belirli sürümleri de sabitleyebilirsiniz (`"yayinci.ad": ["1.2.3", "1.2.4"]`); aralık desteklenmez, her sürüm ayrı yazılır. Daha özel kural kazanır: `"*": false` ile `"github": true` birlikte, yalnız github yayıncısına izin verir. Aynı anahtarı iki kez yazmak ayarı geçersiz kılar.
- Kişisel bilgisayarda kullanıcı ayarlarına eklemek bile işe yarar: yeni bir eklenti kurmak için önce listeyi bilinçli olarak değiştirmeniz gerekir.
- Ekip bilgisayarlarında aynı ayar `AllowedExtensions` politikasıyla (Windows Grup İlkesi, Intune, macOS yapılandırma profili) zorunlu kılınabilir; kullanıcı ayarı politikayı ezemez.
- Politikada sözdizimi hatası olursa ayar hiç uygulanmaz. Uyguladıktan sonra listede olmayan bir eklentiyi aramayı deneyin; Kur düğmesi pasif olmalı.
- Cursor, Windsurf gibi VS Code tabanlı editörler bu ayarı desteklemeyebilir; kendi belgelerine bakın.

## 6.4 GitHub Actions

CI, sırlarınızın ve yayın yetkinizin bulunduğu yerdir. 2025 ve 2026'da yaygın kullanılan eylemlerin ve depoların CI hatları üzerinden ele geçirildiği olaylar yaşandı. Ajanlar iş akışı dosyalarını da düzenleyebildiği için bu bölüm ajan kullananlar için ayrıca önemlidir.

Hazır örnekler: [ornekler/github/guvenli-ci.yml](../ornekler/github/guvenli-ci.yml) · [ornekler/github/dependabot.yml](../ornekler/github/dependabot.yml)

1. **Varsayılan izin: hiçbir şey.** Her iş akışının başına `permissions: {}` yazın; her işe yalnız gerekeni verin (çoğu zaman `contents: read`). Depo ayarlarında da Settings → Actions → General → Workflow permissions: "Read repository contents".
2. **Eylemleri tam commit SHA'sıyla sabitleyin.** `@v4` ya da `@main` değiştirilebilir; eylemin deposu ele geçirilirse aynı etiket başka kodu gösterebilir. `uses: actions/checkout@<40 karakterlik SHA> # v4.x.y` biçimini kullanın. Sabitlenmiş eylemlerin güncel kalması için Dependabot'u `github-actions` için açın; `cooldown.default-days` (1–90 gün) ile yeni sürümleri birkaç gün bekletin, böylece ele geçirilmiş bir sürüm geri çekilmeden önce size PR olarak gelmez.
3. **`pull_request_target` kullanmayın.** Bu tetikleyici, fork'tan gelen bir PR'ı ana deponun sırları ve yazma yetkisiyle çalıştırır. Fork kodunu bu tetikleyiciyle çalıştırmak sırları dışarı verir. PR'ları `pull_request` ile test edin.
4. **`run:` içinde güvenilmeyen değeri doğrudan yazmayın.** `run: echo "${{ github.event.issue.title }}"` gibi bir satır, başlığa komut yazan herkese kabuk açar. Değeri önce bir ortam değişkenine atayın: `env: BASLIK: ${{ github.event.issue.title }}` ve `run: echo "$BASLIK"`.
5. **`actions/checkout` için `persist-credentials: false`** kullanın; token sonraki adımlarda diskte kalmasın.
6. **Uzun ömürlü bulut anahtarı yerine OIDC.** AWS, GCP, Azure'a sırla değil, kısa ömürlü kimlikle bağlanın.
7. **İş akışı dosyaları kod incelemesinden geçsin.** `.github/workflows/` için CODEOWNERS tanımlayın; ajanın bu klasörü değiştirmesini onaya bağlayın ([örnek ayar](../ornekler/claude-settings.json)).

### CI'da ajan çalıştırıyorsanız

Issue ya da PR yorumuyla tetiklenen bir yapay zekâ ajanı (ör. "@claude bu hatayı düzelt"), tetikleyen kişinin yazdığı metni okur. Bu, [istem enjeksiyonunun](05-istem-enjeksiyonu-ve-mcp.md) CI'daki hâlidir:

- Ajanı yalnız depoya yazma yetkisi olan kişilerin tetiklemesine izin verin; dışarıdan gelen issue'larla otomatik tetiklenmesin.
- Ajanın iş akışına yalnız gereken izinleri verin; üretim sırlarını o iş akışına koymayın.
- Ajanın açtığı PR'lar insan onayı olmadan birleşmesin.

## 6.5 Ajanın bağımlılık eklemesine kural koyun

Projenin `CLAUDE.md` (ya da eşdeğeri) dosyasına şu tür bir kural eklemek, ajanın sizden habersiz paket eklemesini zorlaştırır:

```markdown
## Bağımlılık kuralları
- Yeni bir bağımlılık eklemeden önce paket adını, yayıncıyı, haftalık indirme sayısını ve son
  yayın tarihini göster ve onay iste.
- `npm install` yerine `npm install --ignore-scripts` kullan.
- `curl | sh`, `irm | iex` ya da benzeri tek satırlık kurulumları asla çalıştırma.
```

Tam örnek: [ornekler/CLAUDE.md.ornek](../ornekler/CLAUDE.md.ornek). Bu bir talimattır, teknik engel değildir. Teknik engel için yukarıdaki `.npmrc` ayarlarını ve [Bölüm 4](04-claude-code-sertlestirme.md)'teki `ask` kurallarını birlikte kullanın.

---

**Önceki:** [← 5. İstem enjeksiyonu ve MCP](05-istem-enjeksiyonu-ve-mcp.md) · **Sonraki:** [7. Ekip politikası →](07-ekip-politikasi.md)
