# Yapay zekâ ajanları için güvenlik rehberi

**Nexivion Labs** · ilk sürüm 6 Kasım 2026 · sürüm 2.1, 7 Kasım 2026 ([değişiklikler](CHANGELOG.md))

6 Kasım 2026 gecesi ekibimizden bir geliştiricinin Claude hesabı ele geçirildi. Bilgisayarındaki bir VS Code eklentisi dokuz gün boyunca arka planda zararlı yazılım indirdi. Saldırgan, oturum anahtarıyla hesaba girdi ve Claude Code'a başkası adına kod yazdırdı. O gece olaya Claude ile birlikte müdahale ettik.

Bu depo, o gecenin dersleriyle hazırlandı. Yapay zekâ ajanlarıyla (Claude Code, Cursor, Copilot, Cline ve benzerleri) çalışan geliştiriciler ve küçük ekipler için yazıldı.

> Bu rehber hukuki ya da profesyonel adli bilişim hizmetinin yerine geçmez. Ciddi bir olayda kurumunuzun güvenlik ekibiyle ya da bir uzmanla çalışın.

---

## Şu an bir olay mı yaşıyorsunuz?

Okumayı bırakın ve doğrudan şuraya gidin: **[Olay anında: ilk 15 dakika, ilk saat, ilk gün](docs/02-olay-aninda.md)**

Kısa hâli:

1. **Silmeyin, kapatmayın, ama ağdan ayırın.** Oturumu durdurun, ekranları telefonla fotoğraflayın, kabloyu/Wi-Fi'ı kesin.
2. **O bilgisayarı ele geçirilmiş sayın.** Ondan hiçbir hesaba giriş yapmayın.
3. **Temiz bir cihazdan** sırayla kapatın: e-posta → yapay zekâ hesabı (bulut oturumunu durdur, ekranları fotoğrafla, tüm oturumlardan çık, Claude Code yetkileri, API anahtarları) → GitHub (oturumlar, token'lar, **güvenlik günlüğünü hemen dışa aktar**) → diğer anahtarlar.
4. Bir kişi yönetsin, bir kişi saat saat [olay kaydı](sablonlar/olay-kaydi.md) tutsun.

Yazdırıp elinizde tutabileceğiniz tek sayfa: [kontrol-listeleri/olay-ani.md](kontrol-listeleri/olay-ani.md)

---

## İçindekiler

| # | Bölüm | Ne zaman okunur |
|---|---|---|
| 0 | [Çekirdek kurallar](docs/00-cekirdek-kurallar.md) | Önce bunu okuyun: rehberin on maddelik özü |
| 1 | [Kurmadan önce: olmazsa olmaz kontroller](docs/01-kurmadan-once.md) | Yeni bir eklenti, paket, depo ya da araç kurmadan önce |
| 2 | [Olay anında](docs/02-olay-aninda.md) | Hesap ya da bilgisayar ele geçirildiğinde |
| 3 | [Claude ile adli inceleme: üç istem](docs/03-claude-ile-adli-inceleme.md) | Olayın kaynağını bulmak için |
| 4 | [Claude Code'u sertleştirme](docs/04-claude-code-sertlestirme.md) | Kurulumdan hemen sonra, ekip ayarlarını belirlerken |
| 5 | [İstem enjeksiyonu ve MCP sunucuları](docs/05-istem-enjeksiyonu-ve-mcp.md) | Ajana dış içerik okutmadan, MCP sunucusu eklemeden önce |
| 6 | [Tedarik zinciri: npm, pip ve eklentiler](docs/06-tedarik-zinciri.md) | Paket yöneticisi ve eklenti politikası belirlerken |
| 7 | [Ekip politikası ve düzenli kontroller](docs/07-ekip-politikasi.md) | Ekibe yeni biri katıldığında, her ay |
| 8 | [Senaryolar: önle, fark et, müdahale et](docs/08-senaryolar.md) | Belirli bir durum için hazır plan ararken |
| 9 | [Hesap, kimlik ve oturum güvenliği](docs/09-hesap-ve-oturum-guvenligi.md) | Hesaplarınızı ilk kez gözden geçirirken; iki adımlı doğrulama yetmez mi diye merak ederken |
| 10 | [Platform başvuru kartı](docs/10-platform-basvuru-karti.md) | Windows, macOS, Linux ve WSL2 için komut karşılıklarını ararken |
| 11 | [Yedekleme ve kurtarma](docs/11-yedekleme-ve-kurtarma.md) | "Yedekten döneriz" demeden önce; üç ayda bir geri yükleme tatbikatı |
| 12 | [Bulutta ve konteynerde çalışan ajanlar](docs/12-bulutta-ajan.md) | Claude Code on the web, Codespaces ya da Dev Container kullanıyorsanız |
| 13 | [Veri nereye gidiyor?](docs/13-veri-nereye-gidiyor.md) | Gizlilik, eğitim izni, diskteki oturum dökümleri ve tarayıcıda çalışan ajanlar |
| 14 | [Ajanın yazdığı kodun güvenliği](docs/14-ajanin-yazdigi-kod.md) | Ajanın PR'ını incelemeden, önerdiği paketi kurmadan önce |
| — | [Standart eşlemesi](docs/standart-eslemesi.md) | OWASP ve NIST karşılıklarını görmek için |

### Hazır malzemeler

- **Kontrol listeleri:** [Tek sayfalık kurulum öncesi kontrol](kontrol-listeleri/kurmadan-once.md) · [Olay anı kontrol listesi](kontrol-listeleri/olay-ani.md) · [Aylık kontrol](kontrol-listeleri/aylik-kontrol.md) · [Ajan kodu inceleme](kontrol-listeleri/ajan-kodu-inceleme.md)
- **Şablonlar:** [Olay kaydı (zaman çizelgesi)](sablonlar/olay-kaydi.md) · [Sağlayıcıya olay bildirimi](sablonlar/olay-bildirimi.md) · [Delil zinciri kaydı](sablonlar/delil-zinciri.md) · [Onaylı araçlar listesi](sablonlar/onayli-araclar.md) · [Masa başı tatbikat](sablonlar/masa-basi-tatbikat.md)
- **Örnek ayar dosyaları:** [Claude Code `settings.json`](ornekler/claude-settings.json) · [`.npmrc`](ornekler/npmrc) · [VS Code eklenti izin listesi](ornekler/vscode-extensions-allowed.jsonc) · [Örnek `CLAUDE.md`](ornekler/CLAUDE.md.ornek) · [Güvenlik kapısı hook'u](ornekler/hooks/guvenlik_kapisi.py) · [Sertleştirilmiş GitHub Actions](ornekler/github/guvenli-ci.yml)
- **[Sözlük](SOZLUK.md):** rehberde geçen teknik terimlerin Türkçe açıklamaları.

---

## Olayla ilişkilendirilen eklenti: Alpme

> **Durum: bağımsız raporlara dayanıyor; kendi delil paketimizle karşılaştırma henüz yapılmadı.** Aşağıdaki kimlik, olaydan önce yayımlanmış bağımsız bir tespit aracına ve kullanıcı bildirimlerine dayanır. Kendi `vaka-kanit` paketimizdeki eklenti kimliğiyle birebir eşleştiğini doğruladığımızda bu notu kaldıracağız; eşleşmezse kutuyu düzelteceğiz. [Çekirdek kural 10](docs/00-cekirdek-kurallar.md): kanıtla doğrulanmamış şey hipotezdir.

Rehberin ilk sürümünde eklentinin adını vermemiştik. Bağımsız raporlar kamuya açık olduğu için, okuyanların kendi bilgisayarlarını kontrol edebilmesi adına ekliyoruz.

| Alan | Bilgi |
|---|---|
| Ad ve sürüm | **Alpme**, v1.0.25 (VS Code eklentisi) |
| Yem | alpme.com üzerinden "ücretsiz yapay zekâ kredisi / birleşik API geçidi" vaadi; eklenti dosyası siteden indiriliyordu |
| Ne yapıyor | Kurulumdan sonra arka planda çalıştırılabilir dosyalar indirip çalıştıran bir damlatıcı (dropper); indirilenler tarayıcı çerezlerini, oturumları ve uygulama token'larını (Discord, Instagram, yapay zekâ hesapları dahil) toplayan bilgi hırsızları |
| Nasıl kontrol ederim | Eklenti klasörünüzde `alpme` geçen bir dizin var mı: `%USERPROFILE%\.vscode\extensions\` (Windows), `~/.vscode/extensions/` (macOS/Linux) ve kullandığınız diğer editörlerin eklenti klasörleri. Komutlar: [Bölüm 10.2](docs/10-platform-basvuru-karti.md#102-kurulu-editör-eklentilerini-listeleme) |
| Varsa | Silmeyin; [Olay anında](docs/02-olay-aninda.md) bölümünü uygulayın. Bu eklentiyi kurmuş bir bilgisayardaki **bütün** oturumlar ve şifreler ele geçirilmiş sayılmalıdır. |

Bağımsız kaynaklar: PenguinBTW'nin tespit aracı ve adli raporu (https://github.com/PenguinBTW/alpme-detector), Trustpilot'taki kullanıcı bildirimleri. Bu rehber zararlı yazılımın teknik ayrıntılarını bilerek vermez; savunma için yukarıdakiler yeterlidir.

## Olaydan çıkardığımız beş ders

1. **Uyarılar vardı, bakan yoktu.** Windows Defender dokuz gün boyunca her gün bir tespit kaydetti. Güvenlik aracının kurulu olması yetmez; birinin düzenli bakması gerekir.
2. **Eklenti, kodun kendisi kadar yetkilidir.** VS Code eklentileri sizin kullanıcı yetkinizle, siz bir şey yapmadan çalışabilir. Ajanın güvenliği, ajanın çalıştığı bilgisayarın güvenliğinden büyük olamaz.
3. **Oturum anahtarı, şifreden daha değerlidir.** Saldırgan şifreye ihtiyaç duymadı; bilgisayardan alınan oturum bilgisiyle girdi. İki adımlı doğrulama bu durumda tek başına korumaz; oturumların da kapatılması gerekir.
4. **Silmek, izi siler.** İlk refleks "hemen kaldır" oluyor. Önce delil, sonra temizlik.
5. **Ajan, müdahalede de işe yarar, ama kurallarla.** Salt okunur, adım adım ve sırları ekrana yazmayan bir inceleme, kaynağı saatler içinde bulmamızı sağladı.

---

## Doğruluk ve güncellik

Rehberdeki araç ayarları, komutlar ve sürüm bilgileri **7 Kasım 2026** tarihinde resmî belgelerle karşılaştırıldı (Claude Code sandbox ve izin belgeleri, VS Code kurumsal belgeleri, npm 12 duyurusu, Claude destek makaleleri, KVKK Kurul kararı 2019/10). Araçlar hızla değiştiği için bir ayar çalışmazsa önce ilgili resmî belgeye bakın, sonra [bize bildirin](CONTRIBUTING.md). Hangi iddianın hangi kaynakla doğrulandığı ve doğrulanamayanlar [DONGU-LOG.md](DONGU-LOG.md) dosyasında kayıtlıdır.

## Katkı

Rehber yaşayan bir belgedir. Hata, eksik ya da kendi olayınızdan bir ders varsa [katkı rehberine](CONTRIBUTING.md) bakın. Rehberin kendisinde bir güvenlik sorunu (ör. yanlış ya da tehlikeli bir komut) bulursanız [SECURITY.md](SECURITY.md) dosyasındaki yolu izleyin.

## Kaynaklar

- Anthropic, Tehdit İstihbaratı Raporu, Eylül 2026: https://www.anthropic.com/threat-intelligence-report-september-2026
- PenguinBTW, Alpme eklentisi tespit aracı ve adli rapor (olaydan önce yayımlanmış bağımsız uyarı): https://github.com/PenguinBTW/alpme-detector
- KVKK, Veri İhlali Bildirimi (Kurul kararı 2019/10): https://www.kvkk.gov.tr/Icerik/5362/Veri-Ihlali-Bildirimi
- Claude Destek, tüm oturumlardan çıkış: https://support.claude.com/en/articles/10310342-how-do-i-log-out-of-all-active-sessions
- Claude Destek, etkin oturumları yönetme: https://support.claude.com/en/articles/13124001-managing-your-active-sessions
- Claude Destek, API anahtarı ele geçirildiyse: https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised
- Claude Code belgeleri (güvenlik, izinler, sandbox, ayarlar): https://code.claude.com/docs/en/security
- VS Code, kurumsal eklenti yönetimi: https://code.visualstudio.com/docs/enterprise/extensions

Olayı Anthropic'e ve GitHub'a kanıtlarıyla bildirdik. Ekran görüntüleri ekip arkadaşımızın rızasıyla paylaşılmıştır.

Lisans: [CC BY 4.0](LICENSE) · **Nexivion Labs** · nexivionlabs.io
