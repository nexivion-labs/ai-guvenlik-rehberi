# 4. Claude Code'u sertleştirme

[← İçindekiler](../README.md) · Örnek dosya: [ornekler/claude-settings.json](../ornekler/claude-settings.json)

Bu bölüm Claude Code için yazıldı; ilkeler (en az yetki, onay, yalıtım, sırları uzak tutma) Cursor, Copilot, Cline gibi diğer ajanlara da uygulanır.

> **Sürüm uyarısı:** Claude Code hızlı değişen bir araç. Aşağıdaki ayar adları Kasım 2026 belgelerine göre yazıldı. Uygulamadan önce kendi sürümünüzde [resmî belgelerle](https://code.claude.com/docs/en/settings) doğrulayın ve `/permissions`, `/sandbox` komutlarıyla sonucu kontrol edin.

---

## 4.1 Önce şunu kabul edin: ajan, bilgisayardan daha güvenli olamaz

Claude Code oturum bilgilerini macOS'ta Anahtar Zinciri'nde (Anahtar Zinciri yoksa dosyaya düşer), Linux'ta `~/.claude/.credentials.json` (dosya izni 0600), Windows'ta `%USERPROFILE%\.claude\.credentials.json` dosyasında tutar. Uzak MCP sunucularına OAuth ile bağlandıysanız o token'lar da aynı dosyadadır. Bu dosyalar yalnız sizin kullanıcınıza açıktır, ama **sizin kullanıcınızla çalışan her program** (zararlı bir eklenti dahil) onlara ulaşabilir ve token'lar taşınabilirdir: dosya başka bir makineye kopyalanınca orada da çalışır. Bağımsız araştırmacılar ([Silverfort, 2026](https://www.silverfort.com/blog/skipping-the-lock-a-claude-code-cli-weakness-lets-any-macos-process-read-stored-credentials/)) macOS'ta Anahtar Zinciri kaydının varsayılan erişim listesiyle oluşturulduğunu ve kullanıcı yetkisiyle çalışan bir sürecin parola sorulmadan okuyabildiğini göstermiştir.

Vakamızda en olası açıklama tam olarak buydu: saldırgan şifreye değil, bilgisayardaki oturum bilgisine ulaştı. Bu yüzden aşağıdaki ayarlar **ikinci savunma hattıdır**; birinci hat [Bölüm 1](01-kurmadan-once.md)'deki kurulum disiplinidir.

## 4.2 Ayar dosyaları ve öncelik

| Dosya | Kapsam | Kim düzenler |
|---|---|---|
| `~/.claude/settings.json` | Sizin bütün projeleriniz | Siz |
| `.claude/settings.json` (proje içinde) | Projede çalışan herkes; depoya commit edilir | Ekip |
| `.claude/settings.local.json` | Yalnız sizin bu projedeki tercihleriniz; commit edilmez | Siz |
| `managed-settings.json` | Bilgisayardaki herkes; diğerleri bunu ezemez | Yönetici |

Yönetilen ayar dosyasının yeri: macOS `/Library/Application Support/ClaudeCode/`, Linux ve WSL `/etc/claude-code/`, Windows `C:\ProgramData\ClaudeCode\`. Ekip kurallarını (ör. "atlama kipi kapalı") buraya koyarsanız kimse kendi ayarıyla kapatamaz.

## 4.3 Sırlara erişimi kapatın

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(~/.claude/.credentials.json)"
    ]
  }
}
```

**Önemli sınır:** Resmî belgelere göre `Read`/`Edit` yasak kuralları şunlara uygulanır: Claude'un kendi dosya araçları (Read, Edit, Write, Grep, Glob), istemlerdeki `@dosya` bahisleri, IDE'nin paylaştığı açık dosya bağlamı ve Claude Code'un **tanıdığı** kabuk dosya komutları (`cat`, `head`, `tail`, `sed`, `tee`) ile `>`/`<` yönlendirmelerinin hedefleri. Şunlara **uygulanmaz**: bütün klasörü tarayan `grep -r`, dosyayı kendisi açan bir Python/Node betiği, `CLAUDE.md` içindeki `@import` satırları. Bağımsız bir test ([Rulestack, 30 Eylül 2026](https://dev.to/rulestack/claude-codes-read-deny-rules-let-4-of-11-routes-through-grep-r-a-python-one-liner-and-two-ajf)) 11 erişim yolundan 4'ünün geçtiğini göstermiştir. Yani yasak kuralları **Claude'un neye uzanacağını şekillendirir, işletim sistemi düzeyinde bir duvar değildir**. Gerçek sınır için [sandbox](#45-sandboxı-açın) + `denyRead` gerekir. En iyisi sırların proje klasöründe hiç bulunmamasıdır.

İki yazım tuzağı: dosya kuralları yalnız `Read(...)` ve `Edit(...)` adıyla çalışır; `Write(./x)` diye yazılan bir kural kabul edilir ama **hiç uygulanmaz** (`Edit` kuralı bütün yazma araçlarını kapsar). `Bash(ls *)` gibi kurallarda yıldızdan önceki boşluk önemlidir; `Bash(ls*)` `lsof`'u da eşler.

Alt süreçlere (kabuk komutları, hook'lar, yerel MCP sunucuları) ortam değişkenlerindeki sırların geçmesini engellemek için Claude Code'u şu değişkenle başlatın:

```bash
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1
```

Resmî sandbox belgesi bu değişkeni ortam değişkeni sızıntısına karşı kontrol olarak sayar. İki yan etkisi var: Linux'ta `bubblewrap` gerektirir ve yoksa Claude Code başlamaz (hata mesajı kurulumu söyler); ayrıca ayarlandığında dosya sistemi yalıtımını kapatan ayarları yok sayar ve her komutu sandbox'ta çalıştırır. Yani bu değişken, sandbox'ı "zorunlu" kılmanın da yoludur.

## 4.4 İzinleri bilinçli verin

- Kurallar `allow` (sormadan izin ver), `ask` (her seferinde sor) ve `deny` (asla) listelerindedir. **Sıra: önce `deny`, sonra `ask`, sonra `allow`.** Daha özel bir `allow`, genel bir `deny`'ı ezmez.
- "Bir daha sorma" dediğiniz her onay, `allow` listesine yazılır. Ayda bir `/permissions` ile listeyi gözden geçirin; geniş kuralları (`Bash`, `Bash(*)`) silin.
- Geri alınması zor işlemleri `ask` ya da `deny` listesine koyun:

```json
{
  "permissions": {
    "ask": [
      "Bash(git push *)",
      "Bash(npm publish *)",
      "Bash(curl *)",
      "Bash(wget *)"
    ],
    "deny": [
      "Bash(git push --force *)",
      "Bash(rm -rf *)"
    ]
  }
}
```

- **Atlama kipini kapatın.** `--dangerously-skip-permissions` bütün onayları kaldırır. Yalnız internete kapalı, sırsız, atılabilir bir konteynerde anlamlıdır. Ekip bilgisayarlarında yönetilen ayarlarla kapatın:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  }
}
```

- Ek klasör erişimi (`additionalDirectories`) verirken ev klasörünün tamamını vermeyin.

## 4.5 Sandbox'ı açın

Sandbox, Claude'un çalıştırdığı **kabuk komutlarını** ve onların alt süreçlerini işletim sistemi düzeyinde sınırlar: varsayılan olarak yalnız çalışma klasörüne yazabilir, yeni bir ağ adresine bağlanmadan önce onay ister. İstem enjeksiyonu başarılı olursa kabuk üzerinden verilecek zararı bu sınırlar küçültür; ama aşağıda sayılan boşluklar (okuma varsayılan açık, dosya araçları ve MCP sandbox dışında, kaçış kapısı) kapatılmadan bu bir güvenlik sınırı sayılmaz.

- **Açmak:** Claude Code içinde `/sandbox` komutu. Bütün projelerde açık olsun istiyorsanız `~/.claude/settings.json` içinde `"sandbox": { "enabled": true }`. Ubuntu 24.04 ve üzerinde varsayılan AppArmor politikası bubblewrap'i engelleyebilir; `/sandbox` paneli eksik bağımlılığı gösterir.
- **Platform:** macOS, Linux ve WSL2'de çalışır. **Yerel Windows'ta ve WSL1'de çalışmaz**; Windows kullanıyorsanız Claude Code'u WSL2 içinde çalıştırın. Linux ve WSL2'de `bubblewrap` ve `socat` paketleri gerekir:

  ```bash
  sudo apt-get install bubblewrap socat
  ```

- **Kaçış kapısını kapatın:** Sandbox içinde başarısız olan bir komut, varsayılan olarak sandbox dışında yeniden denenmek üzere onaya sunulur. Dikkat: `Bash(curl *)` gibi bir `allow` kuralı bu yeniden denemeyi de **sormadan** onaylar. Kaçışı tamamen kapatmak için `"allowUnsandboxedCommands": false` ("Strict sandbox mode"). Bunu yönetilen ayarlardan yaparsanız depo içindeki ayarlar sandbox'ı gevşetemez.
- **Sessizce kapanmasın:** Sandbox kurulamazsa (bağımlılık eksik, platform desteklemiyor) Claude Code **varsayılan olarak komutları sandbox'sız çalıştırır**. Hata verip durması için `"failIfUnavailable": true`.
- **Okuma varsayılan olarak açıktır.** Sandbox yazmayı çalışma klasörüyle sınırlar ama okumayı sınırlamaz: `~/.ssh` ve `~/.aws/credentials` gibi dosyalar **okunabilir**. Yerleşik bir kimlik bilgisi yasak listesi yoktur; koruma istediğiniz her dosyayı siz yazarsınız: `sandbox.filesystem.denyRead` ya da aşağıdaki `sandbox.credentials` bloğu. Ortam değişkenleri de sandbox'a aynen geçer; sırları `credentials.envVars` ile kaldırın ya da `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` ayarlayın.

```json
{
  "sandbox": {
    "enabled": true,
    "allowUnsandboxedCommands": false,
    "failIfUnavailable": true,
    "filesystem": { "denyRead": ["~/.ssh", "~/.aws", "~/.claude/.credentials.json", "~/**/.env"] },
    "credentials": {
      "files": [{ "path": "~/.aws/credentials", "mode": "deny" }],
      "envVars": [{ "name": "GITHUB_TOKEN", "mode": "deny" }, { "name": "NPM_TOKEN", "mode": "deny" }]
    }
  }
}
```

  `credentials` bloğu yalnız kullanıcı (`~/.claude/settings.json`) ve yönetilen ayarlardan okunur; proje ayarlarına yazarsanız uygulanmaz.
- **Sandbox yalnız kabuk komutlarını sarar.** Claude'un Read/Edit/Write/WebFetch araçları izin kurallarına tabidir (`denyRead`, Read aracını durdurmaz); hook'lar, yerel MCP sunucuları, LSP sunucuları ve `!` ile sizin yazdığınız komutlar **tam yetkinizle, sandbox dışında** çalışır. Sandbox, izin kurallarının yerine değil yanına konur.
- **Çalıştığını test edin:** `/sandbox` panelinde bağımlılıkların tam olduğunu görün; Claude'dan ev klasörünüze bir dosya yazmasını isteyin, başaramamalı. Sandbox dışında yeniden deneme teklif ederse reddedin.

Daha ağır yalıtım seçenekleri (sürecin tamamını saran sandbox runtime, Dev Container, bulut sanal makinesi) için [Bölüm 12](12-bulutta-ajan.md).

## 4.6 Yabancı bir depoyu açmadan önce

Klonladığınız bir depo, ajanı yönlendiren dosyalar taşıyabilir. Claude Code'u o klasörde ilk kez başlatmadan ve klasöre güvenmeden önce şunlara bakın:

| Dosya | Neden tehlikeli olabilir |
|---|---|
| `CLAUDE.md`, `AGENTS.md`, `.cursorrules` vb. | Ajana talimat verir. "Testleri çalıştırmadan önce şu betiği çalıştır" gibi zararsız görünen satırlar içerebilir. |
| `.claude/settings.json` | İzin kuralları ve **hook**'lar içerebilir. Hook'lar belirli olaylarda kabuk komutu çalıştırır. |
| `.mcp.json` | Projeye MCP sunucusu ekler; sunucu, bilgisayarınızda bir program olarak çalışır. |
| `.vscode/settings.json`, `.vscode/tasks.json` | Klasör açılınca çalışan görevler tanımlayabilir. |
| `.devcontainer/devcontainer.json` | Codespace ya da Dev Container açılırken `postCreateCommand` gibi komutlar çalıştırır. |
| `package.json` betikleri, `Makefile` | Ajan "kurulumu yap" dediğinde çalışır. |

Kural: **Bu dosyaları okumadan klasöre güvenmeyin.** Proje MCP sunucularını toptan onaylayan ayarı (`enableAllProjectMcpServers`) açık tutmayın; sunucuları tek tek onaylayın.

## 4.7 Kendi hook'larınızla bir güvenlik ağı kurun

Hook'lar yalnız tehlike değil, savunma aracıdır da. Her `Bash` aracı çağrısından önce çalışan bir `PreToolUse` hook'u, komut metnini okur ve riskli bir kalıp görürse **çıkış kodu 2** ile çağrıyı engeller; stderr'e yazdığınız açıklama Claude'a gösterilir ve Claude başka bir yol dener.

Hazır örnek: [ornekler/hooks/guvenlik_kapisi.py](../ornekler/hooks/guvenlik_kapisi.py). Şunları engeller: `.env` dosyalarına dokunma (`.env.example` hariç), SSH/AWS/npm kimlik bilgisi dosyaları, `curl … | sh` ve `irm … | iex`, base64 çözüp çalıştırma, zorla push, kök ya da ev klasörünü silme, bütün ortam değişkenlerini dökme, `--no-verify` ile commit/push kontrollerini atlama. Girdiyi okuyamazsa korumayı sessizce kapatmak yerine engeller.

Kurulum:

1. Dosyayı projede `.claude/hooks/guvenlik_kapisi.py` olarak kaydedin.
2. `.claude/settings.json` içine ekleyin:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/guvenlik_kapisi.py\""
          }
        ]
      }
    ]
  }
}
```

3. Elle deneyin. Engellenmesi gereken komut 2, izin verilmesi gereken komut 0 döndürmeli:

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"cat .env"}}' | python3 .claude/hooks/guvenlik_kapisi.py; echo $?
echo '{"tool_name":"Bash","tool_input":{"command":"npm test"}}' | python3 .claude/hooks/guvenlik_kapisi.py; echo $?
```

Sınırları:

- Kalıp listesi atlatılabilir (ör. dosya adını değişkene koymak, komutu bir betiğe yazıp betiği çalıştırmak). Hook **ikinci bir göz**dür; asıl sınır [sandbox](#45-sandboxı-açın) ve izin kurallarıdır.
- Yalnız engellemesi gerekeni değil, engellememesi gerekeni de test edin (`rm -rf node_modules` geçmeli, `rm -rf ~` takılmalı). Her şeyi engelleyen bir hook birkaç gün içinde kapatılır.
- **Çıkış kodu 1 engellemez.** Alışkanlıkla `exit 1` yazarsanız Claude Code bunu "engellemeyen hata" sayar, uyarı gösterir ve komut **çalışır**. Yalnız `exit 2` engeller. Örnek hook bu yüzden hem bozuk girdide hem eşleşmede 2 döndürür.
- Hook'lar izin kipinden **önce** çalışır: bir PreToolUse hook'unun engeli, `--dangerously-skip-permissions` kipinde bile geçerlidir. Bu, hook'u atlama kipine karşı da bir güvenlik ağı yapar.
- Hook sizin yetkinizle çalışır. Başkasının yazdığı hook'u da diğer kodlar gibi okuyun. Ayrıntı: [Claude Code hook belgeleri](https://code.claude.com/docs/en/hooks).

## 4.8 Oturum geçmişi de bir sırdır

Claude Code her oturumun tam dökümünü düz metin olarak `~/.claude/projects/` altında tutar (ayrıntı ve seçenekler: [Bölüm 13.2](13-veri-nereye-gidiyor.md#132-diskte-kalan-iz)). Bir oturumda ajana bir sır gösterdiyseniz o sır bu geçmişte durur. Bu klasörü yedeklere, ekran paylaşımlarına ve paylaşılan klasörlere dahil etmeyin. Bir olaydan sonra bu klasörü yedekten geri yüklemeyin ([Bölüm 2, ilk gün](02-olay-aninda.md)); ayarları onaylı örnekten yeniden kurun.

## 4.9 Diğer ajanlarda karşılıkları

İlkeler aynıdır; ayar adları farklıdır. Ayar adları sık değiştiği için kendi sürümünüzün belgesine bakın.

| İlke | Claude Code | Cursor | VS Code + Copilot ajan modu |
|---|---|---|---|
| Komutlara onay | `permissions` (`allow` / `ask` / `deny`) | Ayarlar → Agents → Approvals & Execution → Run Mode. En temkinlisi **Allowlist** (listede olmayan her komut sorulur). "Run Everything" kullanmayın. | `chat.tools.terminal.autoApprove` ile komut bazında kural (`true`/`false`, düzenli ifade destekler); varsayılan olarak salt okunur komutlar otomatik, `rm`/`del` gibi riskliler sorar. **`chat.tools.global.autoApprove`'u ve `/yolo` komutunu kullanmayın**; "Autopilot" kipi de bütün araçları otomatik onaylar. Kurumsal kullanımda bu ayarlar merkezi politikayla kilitlenebilir. |
| Sınıflandırıcıya güvenme | — | Varsayılan "Auto-review" kipi riskli çağrıları bir sınıflandırıcıyla eler; Cursor'ın kendi belgesi bunun **güvenlik sınırı olmadığını** söyler. | — |
| Sandbox | `/sandbox` (macOS, Linux, WSL2) | Terminal sandbox'ı (`~/.cursor/sandbox.json`) | Dev Container ya da ayrı kullanıcı |
| Dosya erişimini daraltma | `Read` yasak kuralları | Read Access: **Workspace** (varsayılan "System", çalışma alanı dışını da okur); `.cursorignore` | Workspace Trust; `chat.tools.edits.autoApprove` ile hangi dosyaların düzenlenmeden önce onay isteyeceği; `chat.tools.urls.autoApprove` ile hangi URL'lere izin verildiği |
| Proje talimat dosyaları | `CLAUDE.md`, `.claude/` | `.cursor/rules`, `.cursorrules` | `.github/copilot-instructions.md` |

Not: Cursor'da bir onay penceresindeki önceden işaretli kutular kipinizi değiştirebilir; onay verirken pencerenin tamamını okuyun ve sonra Run Mode ayarınızın değişmediğini kontrol edin.

## 4.10 Hızlı başlangıç

1. [ornekler/claude-settings.json](../ornekler/claude-settings.json) dosyasını inceleyin, projenize uyarlayın ve `.claude/settings.json` olarak commit edin.
2. `/sandbox` ile sandbox'ı açın (Windows'ta önce WSL2).
3. `/permissions` ile mevcut `allow` listesini temizleyin.
4. [Güvenlik kapısı hook'unu](#47-kendi-hooklarınızla-bir-güvenlik-ağı-kurun) ekleyin ve iki test komutuyla deneyin.
5. Ekip bilgisayarlarında `disableBypassPermissionsMode` kuralını yönetilen ayarlara koyun.
6. Ayda bir [aylık kontrol listesini](../kontrol-listeleri/aylik-kontrol.md) uygulayın.

---

**Önceki:** [← 3. Claude ile adli inceleme](03-claude-ile-adli-inceleme.md) · **Sonraki:** [5. İstem enjeksiyonu ve MCP →](05-istem-enjeksiyonu-ve-mcp.md)
