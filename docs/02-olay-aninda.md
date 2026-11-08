# 2. Olay anında

[← İçindekiler](../README.md) · Yazdırılabilir hâli: [kontrol-listeleri/olay-ani.md](../kontrol-listeleri/olay-ani.md) · Kayıt şablonu: [sablonlar/olay-kaydi.md](../sablonlar/olay-kaydi.md)

Hesabınızda tanımadığınız bir oturum, beklenmedik kullanım, sizin yazmadığınız commit'ler ya da sağlayıcıdan bir güvenlik uyarısı mı gördünüz? Bu bölümü sırayla uygulayın.

> **Altın kural:** Önce durdur ve delili koru, sonra kapıları **temiz bir cihazdan** kapat, en son temizle. Sıra bozulursa ya iz kaybolur ya da saldırgan yeni şifreyi de görür.

## Önce: bu bir olay mı, ne kadar ciddi?

| Seviye | Belirti | Ne yapılır |
|---|---|---|
| **Kırmızı** | Hesapta sizin yapmadığınız işlem, sizin yazmadığınız commit, sızmış bir anahtarın kullanılması, güvenlik aracının etkin bir zararlı bildirmesi | Bu bölümün tamamı, hemen. |
| **Sarı** | Tanınmayan bir oturum ama işlem yok; şüpheli bir eklenti kurulmuş ama belirti yok; güvenlik aracı bir tespit yapıp engellemiş | İlk 15 dakika ve ilk saat adımları; sonra [Bölüm 3](03-claude-ile-adli-inceleme.md) ile inceleme. Olay olmadığı kanıtlanana kadar kırmızı gibi davranın. |
| **Yeşil** | Sağlayıcıdan genel bir güvenlik duyurusu, sizi doğrudan ilgilendirmeyen bir zafiyet haberi | [Aylık kontrol](../kontrol-listeleri/aylik-kontrol.md) adımlarını erkenden uygulayın. |

Emin değilseniz bir üst seviyeyi seçin. Yanlış alarmın maliyeti birkaç saat ve yenilenmiş anahtarlardır; gözden kaçan olayın maliyeti vakamızdaki dokuz gündür.

---

## İlk 15 dakika: durdur ve delili koru

- **Silmeyin.** Oturumları, depoları, dosyaları ve eklentiyi silmek saldırganın izini de siler.
- **Ekranda ne varsa fotoğraflayın:** açık olan ajan oturumu, terminaldeki son komutlar, tarayıcıda zaten açık duran sekmeler, güvenlik aracının bildirimi. Telefonla çekin. **Yeni sayfa açmayın, giriş yapmayın:** oturum listesi, bağlı uygulamalar ve kullanım ekranı gibi hesap sayfalarını ilk saatte **temiz cihazdan** açıp, kapatmadan hemen önce fotoğraflayacaksınız.
- **Ajan oturumunu durdurun**, ama arşivlemeyin ve o oturumla konuşmaya devam etmeyin. Nasıl: terminaldeki Claude Code'da `Ctrl+C`; IDE'de ajan panelindeki durdur düğmesi. **Bulutta çalışan bir oturumsa** (Claude Code on the web ve benzeri) yerel ağı kesmek onu durdurmaz; oturum sunucuda çalışmaya ve depoya yazmaya devam eder. Böyle bir oturumu **temiz cihazdan** web arayüzüne girip durdurun; bu, ilk saatteki "yapay zekâ hesabı" adımının ilk işi olsun. Oturum kimliğini (varsa URL'deki) fotoğraflayın; sağlayıcıya bildirimde isteyecekler.
- **Bilgisayarı ele geçirilmiş sayın.** O bilgisayarda bir daha şifre yazmayın, yeni oturum açmayın. Tuş kaydedici varsa yazdığınız her şey saldırgana gider.
- **Kapatmayın, uyku moduna da almayın,** bellekteki izler kaybolur. Ama **ağ bağlantısını hemen kesin** (kablo, Wi-Fi, VPN). Bu delili bozmaz; saldırganın o bilgisayar üzerinden veri çekmesini ve yeni oturum bilgisi almasını durdurur. Kapıları zaten temiz bir cihazdan kapatacaksınız, ele geçirilmiş bilgisayarın internete ihtiyacı yok.
- **Yalnız çözmeyin:** bir kişi müdahaleyi yönetsin, biri saat saat [kayıt tutsun](../sablonlar/olay-kaydi.md). Kayıtta her satırda saat, kim, ne yaptı, ne gördü olsun.

## İlk saat: kapıları temiz bir cihazdan kapatın

"Temiz cihaz": olaydan etkilenmemiş başka bir bilgisayar ya da telefon. Aşağıdaki sıra önemlidir; e-posta bütün diğer hesapların kurtarma kapısıdır.

### 1) E-posta

- Şifreyi değiştirin, iki adımlı doğrulamayı açın ya da yenileyin.
- Bütün cihazlardan çıkış yapın.
- Üçüncü taraf uygulama erişimlerini, yönlendirme (forwarding) kurallarını ve filtreleri kontrol edin. Saldırganlar güvenlik e-postalarını gizlemek için filtre ekler.

### 2) Yapay zekâ hesabı (Claude örneği)

Neden bu sırayla ve neden iki adımlı doğrulama yetmez: [Bölüm 9](09-hesap-ve-oturum-guvenligi.md).

- **Önce fotoğraflayın, sonra kapatın:** etkin oturumlar listesi, bağlı uygulamalar, kullanım ve fatura ekranı. Kapattıktan sonra bu bilgi kaybolur; sağlayıcıya bildirimde bunları isteyecekler.


- **Etkin oturumlar:** claude.ai → Ayarlar → Hesap → Etkin oturumlar. Tanımadığınız oturumları sonlandırın, ardından **tüm cihazlardan çıkış** yapın. Bu seçenek yalnız **web tarayıcısında** vardır; iOS/Android uygulamasında yoktur, yani temiz cihazınız telefonsa tarayıcıyı kullanın. Çıkış, Claude Code oturumlarını ve CI için `setup-token` ile üretilmiş token'ları da kapatır, ancak **API anahtarlarını etkilemez**.
- **Claude Code yetkileri:** Claude Code girişleri Ayarlar → Hesap'taki oturum listesinde görünür; görünmeyen token'lar için Ayarlar → Claude Code'da çöp kutusu simgesiyle silin.
- **Bağlı hesaplar:** bağlı GitHub hesabı ya da bağlayıcılar (connector) size ait değilse ya da tanımıyorsanız bağlantıyı kesin.
- **API anahtarları:** Console'daki bütün anahtarları gözden geçirin; o bilgisayarda bulunan her anahtarı iptal edin ve yenisini üretin.
- **Ödeme ve kullanım:** beklenmedik kullanım ya da ödeme varsa ekranları kaydedin ve destekle iletişime geçin.
- Tarayıcı eklentisi gibi ayrı yetkilendirilmiş istemciler kullanıyorsanız onların da çıkış yaptığını doğrulayın; hepsi her zaman oturum listesinde görünmeyebilir. Şüphe varsa destekten hesap güvenliği incelemesi isteyin.

Diğer sağlayıcılarda (ChatGPT, Cursor, Copilot vb.) karşılığı: etkin oturumlar → tümünden çıkış → API anahtarlarını yenile → bağlı uygulamaları kontrol et.

### 3) GitHub

- Ayarlar → Oturumlar: tanımadıklarını sonlandırın.
- Kişisel erişim token'ları (classic ve fine-grained), SSH anahtarları, GPG anahtarları, yetkili OAuth ve GitHub uygulamaları, deploy anahtarları.
- Güvenlik günlüğü (Settings → Security log) ve kuruluş için Audit log: **hemen dışa aktarın** (Export). Günlüklerin saklama süresi sınırlıdır ve GitHub Destek sizin için günlük saklayamaz ya da süreyi uzatamaz. Dışa aktardığınız dosyanın SHA-256 değerini [delil zinciri kaydına](../sablonlar/delil-zinciri.md) yazın.
- Son commit, push, yeni oluşturulan depolar, eklenen işbirlikçiler, değiştirilen GitHub Actions iş akışları ve depo sırları (secrets).

### 4) Diğer anahtarlar ve sırlar

- O bilgisayarda bulunan **her** anahtar: bulut sağlayıcıları (AWS, GCP, Azure), veritabanı, ödeme, e-posta servisleri, npm/PyPI yayın token'ları, MCP sunucularına verdiğiniz token'lar.
- Tarayıcıda kayıtlı şifreler ve oturumlar ele geçirilmiş sayılır. Önemli hesaplarda şifre değiştirin ve oturumları kapatın.
- Parola yöneticisi o bilgisayarda açıksa ana şifresini de değiştirin.

### 5) Ekip erişimi

- Kişiyi kuruluş depolarından ve paylaşılan hesaplardan geçici olarak çıkarın (bu bir suçlama değil, bir karantinadır; kişiye bunu açıkça söyleyin).
- Son commit ve push kayıtlarını, açılan PR'ları ve CI/CD çalıştırmalarını kontrol edin.

### 6) Ağ kesik kalsın

- İlk 15 dakikada kestiğiniz ağ bağlantısının kesik kaldığından emin olun (Wi-Fi'ın kendiliğinden yeniden bağlanmadığını, kablosuz ağ tanımlarının kapalı olduğunu kontrol edin). İnceleme bitene kadar ağa bağlanmasın.
- **Dikkat:** [Bölüm 3](03-claude-ile-adli-inceleme.md)'teki Claude ile adli inceleme internet gerektirir. Bu çelişkiyi nasıl yöneteceğiniz orada anlatılıyor; kısaca: inceleme için ayrı, yeni ve kısıtlı bir kimlik kullanın ve ağı yalnız incelemenin süresi kadar açın.

## İlk gün: kök neden, bildirim, temizlik

### İletişim

- Olayı yalnız bilmesi gerekenlerle ve **ele geçirilmiş cihazların dışındaki** bir kanaldan (telefon, ayrı bir mesajlaşma grubu) konuşun. Ele geçirilmiş bir e-posta ya da Slack hesabı saldırgana müdahalenizi canlı izletir.
- Ayrıntıları geniş bir listeye yaymadan önce, hukuki bir yükümlülük ihtimali varsa hukukçuyla konuşun.
- Etkilenen kişiye (hesabı ele geçirilen ekip arkadaşı) düzenli bilgi verin; suçlayıcı dil kullanmayın.

### Teknik

- **Kök neden:** [Üç istemle](03-claude-ile-adli-inceleme.md) salt okunur adli inceleme yapın. Amaç, "nasıl girdi?" sorusunu cevaplamak. Kök neden bulunmadan temizlik yapılırsa aynı kapıdan tekrar girilir.
- **Bildirim:** Hizmet sağlayıcıya ve kötüye kullanılan platforma oturum kimlikleri, saatler ve kanıtlarla bildirin. Hazır metin: [sablonlar/olay-bildirimi.md](../sablonlar/olay-bildirimi.md). Zararlı eklentiyi pazar yerine (VS Code Marketplace'te "Report Abuse"), zararlı paketi npm/PyPI'ye bildirin.
- **Yasal yükümlülükler:** Olay kişisel verileri (müşteri verisi, çalışan bilgisi) etkilediyse KVKK kapsamında bildirim yükümlülüğünüz olabilir. Bir hukukçuya danışın; süreler kısa olabilir.
- **Doğru format:** Kurulum belleğini başka, temiz bir bilgisayarda resmî araçla hazırlayın ve bütün disk bölümlerini silin. "Dosyalarımı koru" ya da "bu bilgisayarı sıfırla" seçenekleri yetmez.
- **Yedek:** Yedekte yalnız belgeler ve kaynak kod olsun. `.exe`, `.vsix`, `node_modules`, `.vscode`, `.claude`, tarayıcı profili ve kabuk başlangıç dosyaları (`.bashrc`, `.zshrc`, PowerShell profili) alınmaz. Kaynak kodu mümkünse yedekten değil, uzak depodan (GitHub) yeniden klonlayın ve olay öncesi son temiz commit'i doğrulayın.
- **Ayar eşitlemesi:** Settings Sync zararlı eklentiyi geri getirebilir. Açmadan önce bulut tarafındaki eklenti listesini kontrol edin, gerekirse eşitleme verisini sıfırlayın.
- **Yeniden kurulumda:** [Bölüm 1](01-kurmadan-once.md) ve [Bölüm 4](04-claude-code-sertlestirme.md)'ü uygulayarak, yalnız onaylı araçlarla başlayın.

## Olaydan bir hafta sonra: geriye bakış

Suçlu aramayan kısa bir toplantı yapın ve şunları yazılı hâle getirin:

1. Ne oldu? (zaman çizelgesi, olay kaydından)
2. Neyi erken fark edebilirdik? (vakamızda: Defender tespitleri)
3. Neyi değiştiriyoruz? (her madde için sahibi ve tarihi olan eylem)
4. Bu rehbere ne eklenmeli? ([katkı](../CONTRIBUTING.md))

---

**Önceki:** [← 1. Kurmadan önce](01-kurmadan-once.md) · **Sonraki:** [3. Claude ile adli inceleme →](03-claude-ile-adli-inceleme.md)
