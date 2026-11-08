# İyileştirme döngüsü kaydı

7 Kasım 2026 akşamı yürütülen 10 turluk iyileştirme döngüsünün kaydı. Her tur ayrı bir commit'tir ("Tur N: …").

## Tur 1 — Kapsam ve çelişki taraması (21:15–21:17)

- **Araştırılan:** OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10, 9 Aralık 2025), NIST SP 800-61 Rev. 3 (Nisan 2025) ve CSF 2.0 ilişkisi.
- **Bulgular:** Rehberin önerileri tek tek doğru ama bir "öz" yoktu; okur neyin vazgeçilmez olduğunu çıkaramıyordu. Hiçbir öneri bir standarda bağlanmamıştı. Senaryo bazlı plan yoktu.
- **P0:** çekirdek kurallar · **P1:** standart eşlemesi, senaryo bölümü · **P2:** —
- **Değişiklikler:** `docs/00-cekirdek-kurallar.md` (10 kural), `docs/standart-eslemesi.md` (ASI, LLM Top 10, CSF 2.0), `docs/08-senaryolar.md` (S1 sızan sır, S2 ekip arkadaşının hesabı), README içindekiler.
- **Eleştiri:** ASI07 (ajanlar arası iletişim) rehberin okuruna uymuyor; kapsam dışı olarak açıkça yazıldı. Çekirdek kurallar 10'u geçmesin diye birleştirme yapıldı.
- **Doğrulanamayan:** OWASP sayfalarının tam URL'leri bu oturumdan açılamadı; ana alan adı verildi.
- **Sonraki tura not:** Hesap güvenliği bölümünde passkey, kurtarma kodları ve oturum çalma (infostealer) ayrıntısı eksik.

## Tur 2 — Hesap, kimlik ve oturum güvenliği (21:17–21:18)

- **Araştırılan:** Anthropic'in Ağustos 2026 bilgi hırsızı uyarısı (Vidar, LummaC2, StealC, RedLine, Acreed, AMOS); GitHub iki adımlı doğrulama, passkey ve kurtarma kodları.
- **Bulgular:** Rehber "iki adımlı doğrulamayı açın" diyordu ama vakanın kendisi bunun oturum hırsızlığına karşı yetmediğini gösteriyordu. Hesaplar arası kurtarma zinciri, ikinci adım yöntemlerinin farkı ve kurtarma kodları anlatılmıyordu.
- **P0:** oturum hırsızlığı ve 2FA sınırı · **P1:** hesap bağımlılık zinciri, kurtarma kodları · **P2:** ayrı tarayıcı profili
- **Değişiklikler:** `docs/09-hesap-ve-oturum-guvenligi.md`; senaryolar S3 (bilgi hırsızı), S4 (kayıp telefon); çekirdek kural 9 güncellendi; standart eşlemesi ve Bölüm 2 bağlantıları.
- **Eleştiri:** "Ayrı tarayıcı profili" tek başına koruma değil; abartmamak için "saldırı yüzeyini daraltır" diye sınırlandırıldı. Zararlı aile adları yalnız kaynaktaki gibi verildi, tespit imzası verilmedi.
- **Doğrulanamayan:** Anthropic'in kendi duyuru metni (haber kaynağı üzerinden aktarıldı).
- **Sonraki tura not:** Bölüm 4'te Cursor/Copilot karşılıkları yok; hook örneği somut değil.

## Tur 3 — Ajan sertleştirme (21:18–21:20)

- **Araştırılan:** Claude Code hook belgeleri (PreToolUse, stdin JSON, çıkış kodu 2), Cursor Run Modes belgeleri (Auto-review, Allowlist, Run Everything, Read Access, sandbox.json) ve Cursor forumundaki kip değişikliği şikâyetleri, VS Code kurumsal yapay zekâ politikaları.
- **Bulgular:** Bölüm 4.7 hook'u yalnız anlatıyordu, kullanılabilir bir örnek yoktu. Rehber Claude Code dışındaki ajanları hiç ele almıyordu. Cursor'da varsayılan kip bir sınıflandırıcıya dayanıyor ve üretici bunun güvenlik sınırı olmadığını söylüyor.
- **P0:** çalışan hook örneği · **P1:** diğer ajanlar tablosu, S5 (zararlı depo talimatı) · **P2:** S6 (geri alınamayan işlem)
- **Değişiklikler:** `ornekler/hooks/guvenlik_kapisi.py` (16 izin/engel vakasıyla denendi, bozuk girdide engeller), Bölüm 4.7 kurulum ve sınırlar, Bölüm 4.9 Cursor ve Copilot karşılıkları, senaryolar S5–S6.
- **Eleştiri:** İlk sürüm `.env.example` dosyasını da engelliyordu (yanlış pozitif); düzeltildi. Hook'un atlatılabileceği açıkça yazıldı, "ikinci göz" olarak konumlandı. Copilot satırı ayar adı vermiyor çünkü doğrulanmış kaynak bulunamadı.
- **Doğrulanamayan:** Copilot ajan modunun güncel ayar adları.
- **Sonraki tura not:** İstem enjeksiyonu bölümünde ajanın "belleği" (CLAUDE.md, otomatik bellek) üzerinden kalıcı zehirlenme ve MCP araç açıklamalarının sonradan değişmesi (rug pull) somutlaştırılmalı.

## Tur 4 — İstem enjeksiyonu ve MCP (21:19–21:21)

- **Araştırılan:** OWASP MCP Top 10 (beta, MCP03 araç zehirlenmesi), Invariant Labs'in araç zehirlenmesi uyarısı (Nisan 2025), sonradan değişme örnekleri (postmark-mcp, CVE-2025-54136), OWASP ASI06 bellek zehirlenmesi.
- **Bulgular:** Bölüm 5 MCP'yi genel bir "paket riski" olarak ele alıyordu; araç açıklaması zehirlenmesi, gölgeleme ve sonradan değişme ayrı ayrı anlatılmıyordu. Talimat dosyaları üzerinden kalıcı zehirlenme hiç yoktu.
- **P0:** kalıcı zehirlenme · **P1:** MCP'ye özgü üç saldırı, S7, S8 · **P2:** MCP Top 10 eşlemesi
- **Değişiklikler:** Bölüm 5.3 (kalıcı zehirlenme), 5.4'e üç saldırı tablosu, örnek ayarlara talimat ve MCP dosyaları için `ask` kuralları, standart eşlemesine OWASP MCP Top 10, senaryolar S7–S8.
- **Eleştiri:** MCP Top 10 beta olduğu için yalnız kesin bilinen MCP03 kodla verildi; diğerleri "—" ile işaretlendi. Gerçek örneklerde saldırı tekniği ayrıntısı verilmedi.
- **Doğrulanamayan:** postmark-mcp olayının birincil araştırma raporu bu oturumdan açılmadı (ikincil kaynak).
- **Sonraki tura not:** Tedarik zincirinde GitHub Actions (sabitlenmemiş eylemler, `pull_request_target`, token yetkileri) yok.

## Tur 5 — Tedarik zinciri (21:21–21:22)

- **Araştırılan:** GitHub Actions sertleştirme uygulamaları (SHA ile sabitleme, `permissions: {}`, `pull_request_target` riski, `run:` içinde ifade enjeksiyonu, `persist-credentials`, OIDC), 2026 CI ele geçirme olayları, Dependabot.
- **Bulgular:** Bölüm 6 yalnız paket yöneticilerini ve editör eklentilerini kapsıyordu; sırların ve yayın yetkisinin bulunduğu CI hiç yoktu. Ajanların iş akışı dosyalarını düzenleyebilmesi ve CI'da ajan çalıştırma ayrı bir risk.
- **P0:** GitHub Actions sertleştirmesi · **P1:** CI'da ajan, S9, S10 · **P2:** Dependabot bekleme süresi
- **Değişiklikler:** Bölüm 6.4, `ornekler/github/guvenli-ci.yml` ve `dependabot.yml` (YAML olarak ayrıştırıldı), örnek ayarlara `.github/workflows/` için `ask`, senaryolar S9–S10.
- **Eleştiri:** Örnek iş akışına gerçek SHA yazmak cazipti ama yanlış ya da eskimiş bir SHA'yı "güvenli" diye sunmak tam olarak rehberin önlemeye çalıştığı hata olurdu; yer tutucu bırakıldı ve resmî depodan doğrulama şartı yazıldı. İlk YAML'da tırnak hatası vardı, ayrıştırıcıyla yakalandı.
- **Doğrulanamayan:** Dependabot `cooldown` anahtarının güncel adı birincil belgeden kontrol edilemedi.
- **Sonraki tura not:** Olay müdahalesi bölümü delil zinciri (kim, ne zaman, hangi dosya) ve iletişim planı açısından zayıf.

## Tur 6 — Olay müdahalesi ve adli inceleme (21:22–21:25)

- **Araştırılan:** Delil zinciri uygulamaları (ISO 27001 kontrol 5.28 yaklaşımı), GitHub Destek'in olay sırasında günlük saklamadığı ve saklama süresini uzatmadığı bilgisi, günlüklerin saklama süreleri.
- **Bulgular:** Rehber "fotoğraflayın" diyordu ama toplanan delillerin kaydı, hash'i ve devri için bir yapı yoktu. Günlüklerin süresi dolmadan dışa aktarılması yazmıyordu. Olayın ciddiyetine göre karar verme (her şüphede tam müdahale mi?) ve iletişim planı eksikti.
- **P0:** günlükleri hemen dışa aktarma · **P1:** ciddiyet seviyeleri, delil zinciri şablonu, iletişim, S11 (kişisel veri ve KVKK) · **P2:** S12 (yanlış alarm)
- **Değişiklikler:** Bölüm 2'ye seviye tablosu, GitHub günlük dışa aktarma, iletişim alt bölümü; `sablonlar/delil-zinciri.md`; olay anı kontrol listesine üç madde; senaryolar S11–S12.
- **Eleştiri:** KVKK süresi hukuki tavsiye gibi okunmasın diye "Kurul kararlarında belirtilen" diye kaynaklandırıldı ve hukukçuyla doğrulama şartı kondu. Adli istemlere (değiştirilmemesi gereken metin) dokunulmadı; Windows olay günlüğü dışa aktarma önerisi, istem 3'teki "yalnız metin dosyası" kuralıyla çeliştiği için eklenmedi.
- **Doğrulanamayan:** KVKK 72 saat kuralı birincil kaynaktan bu oturumda okunmadı (genel bilgi; hukukçu doğrulaması şartıyla yazıldı).
- **Sonraki tura not:** Platform tablosu: komutların Windows/macOS/Linux/WSL farkları tek yerde değil; macOS'ta Defender karşılığı yok.

## Tur 7 — Platform kapsamı ve komut doğruluğu (21:23–21:26)

- **Araştırılan:** Platformlara göre yerleşik koruma, kalıcılık noktaları, kimlik bilgisi konumları, eklenti klasörleri; komutların salt okunur olduğunun kontrolü.
- **Bulgular:** Platform farkları altı ayrı bölüme dağılmıştı; okur olay anında doğru komutu arıyordu. macOS/Linux kullanıcıları için "Defender bakın" önerisinin karşılığı yoktu.
- **P1:** platform başvuru kartı · **P2:** eklenti listeleme komutu
- **Değişiklikler:** `docs/10-platform-basvuru-karti.md` (yerleşik koruma, sandbox, kimlik bilgisi yeri, eklenti listeleme, kalıcılık, bağlantılar, güvenlik aracı geçmişi, hash), Bölüm 1.6 bağlantısı, README.
- **Eleştiri:** İlk taslak "Linux komutları denendi" diyordu; `ss` ve `crontab` test ortamında yoktu. İfade, gerçekte neyin denendiğini söyleyecek şekilde düzeltildi. macOS `sfltool dumpbtm` yönetici şifresi istediği açıkça yazıldı.
- **Doğrulanamayan:** PowerShell ve macOS komutları çalıştırılamadı (bu ortamda yok); sözdizimi kontrolü yapıldı.
- **Sonraki tura not:** Ekip bölümü: yönetim/uyumluluk tarafında tatbikat (masa başı egzersizi) ve ölçülebilir hedefler yok.

## Tur 8 — Ekip, süreç ve uyumluluk (21:24–21:26)

- **Araştırılan:** Küçük ekipler için masa başı tatbikat tasarımı, CIS Kritik Güvenlik Kontrolleri v8 IG1 ve 17.7 (düzenli olay müdahalesi tatbikatı).
- **Bulgular:** Bölüm 7 kurallar koyuyordu ama işleyip işlemediğini ölçecek bir şey yoktu; plan hiç denenmiyordu. Rehberin kendi olayı hazır bir tatbikat senaryosu.
- **P1:** tatbikat şablonu, beş ölçüt · **P2:** CIS eşlemesi
- **Değişiklikler:** `sablonlar/masa-basi-tatbikat.md` (60 dakikalık akış, 5 senaryo, sürprizler, başarı ölçütü), Bölüm 7.4 ölçütler, 7.5 tatbikat, işe giriş listesine kurtarma kodu, aylık kontrole iki madde, standart eşlemesine CIS IG1.
- **Eleştiri:** Ölçütlere hedef sayılar koymak, uydurma kesinlik riski taşır; hedefler "0", "azalan" ve vakanın kendi sayısına (9 gün) bağlandı. CIS eşlemesi kontrol numaralarıyla sınırlı tutuldu, alt koruma numaraları (17.7 hariç) doğrulanamadığı için yazılmadı.
- **Sonraki tura not (kullanıcı isteği):** Tur 9 ve 10, yeni içerik yerine **doğrulamaya** ayrılacak: rehberdeki olgusal iddialar tek tek birincil kaynaklarla kontrol edilecek.

## Tur 9 — Doğrulama (21:25–21:28)

Kullanıcının isteğiyle bu tur yeni içerik yerine mevcut iddiaların birincil kaynaklarla doğrulanmasına ayrıldı.

| İddia | Kaynak | Sonuç |
|---|---|---|
| Sandbox macOS/Linux/WSL2'de çalışır, yerel Windows'ta çalışmaz | code.claude.com/docs/en/sandboxing (tam metin okundu) | Doğrulandı |
| Sandbox varsayılan olarak okumayı kısıtlar | aynı | **Yanlıştı** — `~/.ssh`, `~/.aws/credentials` okunabilir; `denyRead`/`credentials` gerekir. Düzeltildi. |
| `allowUnsandboxedCommands`, `failIfUnavailable`, `excludedCommands` adları | aynı | Doğrulandı; ek: `allow` kuralı sandbox dışı yeniden denemeyi onaylar; kurulamazsa varsayılan sandbox'sız devam. Eklendi. |
| `credentials` bloğu proje ayarlarında uygulanmaz (v2.1.246+) | aynı | Doğrulandı; örnek dosyaya not kondu. |
| `Read` yasakları yalnız Claude araçlarına uygulanır | code.claude.com/docs/en/permissions (arama özeti) + bağımsız test | **Eksikti** — tanınan kabuk komutlarına (`cat`, `head`, `tail`, `sed`, `tee`) ve yönlendirmelere de uygulanır; `grep -r` ve betiklere uygulanmaz. Düzeltildi. |
| `Write(...)` kuralı çalışır | aynı | **Yanlış varsayım** — yok sayılır, yalnız `Edit`. Eklendi. |
| Kimlik bilgisi konumları (Keychain, `.credentials.json`, 0600) | Anthropic belgesi (Silverfort ve secretspec alıntılarıyla) | Doğrulandı; MCP OAuth token'larının aynı dosyada olduğu eklendi. |
| Tüm oturumlardan çıkış API anahtarlarını etkilemez, Claude Code'u kapatır | support.claude.com/…/10310342 (tam metin) | Doğrulandı; **yalnız web'de** olduğu eklendi. |
| VS Code `extensions.allowed` 1.96+, anahtar anlamları, politika adı | code.visualstudio.com/docs/enterprise/extensions (tam metin) | Doğrulandı; sürüm dizisi ve çakışma kuralı eklendi. |
| npm 12 "planlandı" | GitHub duyurusu (Haziran 2026) ve Temmuz 2026 haberleri | **Eskimişti** — npm 12 çıktı; betikler kapalı, `allow-git=none`, `approve-scripts`. Güncellendi. |
| pnpm `minimumReleaseAge` dakika | lirantal/npm-security-best-practices | Doğrulandı (10.16+). |
| KVKK 72 saat | kvkk.gov.tr, Kurul kararı 2019/10 | Doğrulandı; madde ve karar numarası eklendi. |
| GitHub Actions: SHA, `permissions: {}`, `pull_request_target`, `persist-credentials` | GitHub'ın kendi depolarındaki uygulama (github/github-ospo PR #204) | Doğrulandı. |
| Hook: stdin JSON, çıkış kodu 2 engeller | Resmî belge (Almanca yansıma, arama özeti); İngilizce sayfa bu oturumdan açılamadı | Doğrulandı (ikincil yolla). |
| Olaydaki eklenti | PenguinBTW/alpme-detector, Trustpilot | Alpme v1.0.25 olarak tanımlandı; README'ye IOC kutusu eklendi. Kullanıcının delil paketiyle karşılaştırması bekleniyor. |

Doğrulanamayanlar: Copilot ajan modu ayar adları; Dependabot `cooldown` anahtarının güncel adı; postmark-mcp birincil raporu; PowerShell ve macOS komutlarının çalıştırılması.

## Tur 10 — Bütünsel inceleme ve kapanış (21:28–21:30)

- **Üç gözle okuma:** *Paniklemiş okur* — "ajan oturumunu durdurun" nasıl yapılacağını söylemiyordu; eklendi. README'nin hızlı listesi yazdırılabilir kontrol listesine gitmiyordu; eklendi. *Saldırgan* — Alpme kutusu ve senaryolar teknik ayrıntı vermiyor; hook'un kalıp listesi herkese açık ama bu kabul edilen bir risk (hook "ikinci göz", asıl sınır sandbox). *Denetçi* — hangi iddianın ne zaman, hangi kaynakla doğrulandığı belli değildi; README'ye "Doğruluk ve güncellik" bölümü ve DONGU-LOG bağlantısı eklendi.
- **Regresyon:** iç bağlantılar 0 hata; üç adli istem birebir korunuyor; hook 9 vakada beklenen sonucu veriyor; YAML/JSON örnekleri ayrıştırılıyor; `DONGU-LOG.md` artık CHANGELOG ve README'den bağlı.
- **Durma kriteri:** Bu turda yeni P0 bulgu çıkmadı.

## Kullanıcının karar vermesi gerekenler

1. **Alpme kutusu:** README'ye eklenen eklenti kimliği bağımsız raporlara dayanıyor. Yayımlamadan önce `vaka-kanit` paketindeki `yayıncı.ad` ve sürümle karşılaştırın; eşleşmiyorsa kutuyu düzeltin ya da çıkarın.
2. **`SECURITY.md`:** GitHub'da "Private vulnerability reporting" özelliğini açın; isterseniz bir e-posta adresi ekleyin.
3. **Örnek ayarlar:** `npm install`/`pip install` için `ask` kuralı günlük akışı yavaşlatıyorsa çıkarın.
4. **Hook kalıpları:** `printenv` engeli bazı iş akışlarını rahatsız edebilir; ekibinize göre gevşetin.
5. **İngilizce sürüm** ve **push**: GitHub uygulaması kurulunca `rehber-v2` dalı push edilip PR açılacak.

## İkinci geçiş — Yedekleme ve bulut (21:30–21:33)

- **Gerekçe:** 10 tur erken bitti; kullanıcı 22:00'ye kadar çalışılmasını istedi. Doldurma yerine döngü boyunca not edilen iki gerçek boşluk kapatıldı.
- **Araştırılan:** Claude Code güvenlik ve sandbox-environments belgeleri (bulut oturum yalıtımı, kapsamlı git kimlik bilgisi, ağ izin listesi, uzaktan kontrol farkı), Anthropic mühendislik yazısı, GitHub Codespaces güvenlik belgesi (ayrı VM, port görünürlüğü, sırların yazma yetkisine bağlı enjekte edilmesi), Trend Micro'nun public port bulgusu.
- **Değişiklikler:** Bölüm 11 (yedekleme ve kurtarma, 3-2-1 + 2 ek kural, geri yükleme tatbikatı), Bölüm 12 (yalıtım seviyeleri tablosu, Claude Code on the web, Codespaces/Dev Container, ortak kurallar); Bölüm 4.6 tablosuna `devcontainer.json`; aylık kontrole geri yükleme tatbikatı; CSF RC ve CIS 11 eşlemeleri.
- **Doğrulanamayan:** Hook belgesinin İngilizce sayfası bu oturumdan açılamadı; mekanikler Almanca yansımadan ve ikincil kaynaklardan teyitli.
- **Son durum:** 35 dosya, ~2.150 satır Markdown, 19 commit; iç bağlantı hatası 0; adli istemler birebir korunmuş; hook testi 9/9; YAML/JSON geçerli.

## Üçüncü geçiş — Kalan doğrulamalar (21:40–21:45)

| Önceki kayıt | Yeni kaynak | Sonuç |
|---|---|---|
| Copilot ajan modu ayar adları doğrulanamadı | code.visualstudio.com/docs/agents/run/approvals | `chat.tools.terminal.autoApprove` (komut bazlı, regex), `chat.tools.global.autoApprove` (hepsini onaylar), `/yolo`, Autopilot kipi, `chat.tools.urls.autoApprove`, `chat.tools.edits.autoApprove`. Bölüm 4.9 güncellendi. |
| Dependabot `cooldown` anahtarı | docs.github.com dependabot options reference | `cooldown.default-days` doğru; 1–90 gün; semver bazlı alt anahtarlar var. Örnek dosyaya not, Bölüm 6.4'e açıklama. |
| postmark-mcp birincil raporu | koi.ai blog + Postmark açıklaması | Sahte paket (resmî değil), 15 temiz sürüm sonra 1.0.16'da BCC, ~1.500 haftalık indirme, Eylül 2025. Bölüm 5.4 netleştirildi. |
| Hook mekanikleri | Resmî belgeyi birebir aktaran ikincil kaynaklar (Ekim 2026) | Doğrulandı; iki önemli ek: `exit 1` engellemez, PreToolUse hook'u atlama kipinden önce çalışır. Bölüm 4.7'ye eklendi. |
| Anthropic Ağustos 2026 uyarısı | BleepingComputer'ın yayımladığı e-posta metni, Dark Reading | Anthropic'in e-postadaki ifadesi ve "yalnız oturumları geçersiz kıldık, zararlı yerinde" uyarısı Bölüm 9'a eklendi. |

Kalan doğrulanamayan: PowerShell ve macOS komutlarının çalıştırılması (ortam yok).

## Dördüncü geçiş — Bağımsız inceleme ve düzeltmeler (21:45–21:58)

Rehberi hiç görmemiş ayrı bir ajan üç gözle (saldırgan / paniklemiş okur / denetçi) okudu; 14 bulgu verdi, hepsi işlendi:

| # | Bulgu | Düzeltme |
|---|---|---|
| 1 | Alpme kutusu, ekip deliliyle karşılaştırılmadan kesin dille yazılmıştı; rehberin kendi 10. kuralıyla çelişiyordu | Kutuya "bağımsız raporlara dayanır, kendi delilimizle henüz karşılaştırılmadı" uyarısı; başlık "ilişkilendirilen" oldu |
| 2 | İlk 15 dakikada "oturum listesini fotoğrafla" denmesi, aynı blokta "giriş yapma, ağı kes" ile çelişiyordu | Fotoğraf adımı ikiye bölündü: ekranda açık olan şimdi; hesap sayfaları ilk saatte temiz cihazdan, kapatmadan hemen önce |
| 3 | Bulut oturumu için "sekmeyi açık bırak" yerel ağ kesilince oturumu durdurmaz | Bulut oturumunu temiz cihazdan web arayüzünden durdurma adımı eklendi |
| 4 | `sudo sfltool dumpbtm` ele geçirilmiş Mac'te şifre yazdırıyor | Adli istemden çıkarıldı, başvuru kartında yalnız aylık kontrol için ve yorum satırında |
| 5 | README, docs/02 ve olay kaydı şablonu kapatma sırasını farklı veriyordu; README günlük dışa aktarmayı atlıyordu | Üçü docs/02'ye hizalandı; README'ye günlük dışa aktarma eklendi |
| 6 | "İstem enjeksiyonu başarılı olsa bile zarar bu sınırlarla kalır" yanlış güven veriyordu | Cümle, aynı bölümün saydığı boşluklara atıfla yumuşatıldı |
| 7 | CSF ID.SC kodu 1.1'e ait; 2.0'da GV.SC | Düzeltildi |
| 8 | Veracode %86 rakamı insan incelemesine atfedilmişti | Modellerin oranı olarak düzeltildi |
| 9 | Dört sayı kaynaksızdı (Silverfort, Rulestack 4/11, 127 sahte ad, 237 depo) | Bağlantı ya da kaynak atfı eklendi |
| 10 | İki ortam değişkeni doğrulama tablosunda yoktu | `SUBPROCESS_ENV_SCRUB` resmî sandbox belgesiyle doğrulandı (bubblewrap şartı ve zorunlu sandbox yan etkisi eklendi); `SKIP_PROMPT_HISTORY` doğrulanamadı, metin buna göre indirgendi |
| 11 | Sürüm dizesi ve DONGU-LOG iç tutarsızlıkları | README "sürüm 2.1"; log sayıları aşağıda düzeltildi |
| 12 | macOS'ta `sha256sum -c` yok | `shasum -a 256 -c` eklendi |
| 13 | Hook proje `.npmrc` dosyasını engelliyordu (yanlış pozitif) | Yalnız `~/.npmrc` engelleniyor; test edildi |
| 14 | Örnek CLAUDE.md'de düz metin çapa yanlıştı | Düzeltildi |

Saldırgan gözü: saldırgana yarayacak içerik bulunmadı; tek sorun 6. maddedeki yanlış güven cümlesiydi.

Düzeltme (Tur 3 kaydı): hook ilk turda 16 komutla, sonraki regresyonlarda 9–11 komutluk sabit setle denendi; şu an 11 vaka + 5 npmrc vakası. Dosya sayısı: 40.
