# Yapay zekâ ajanları için güvenlik rehberi

**Nexivion Labs** · ilk sürüm 6 Kasım 2026

6 Kasım 2026 gecesi ekibimizden bir geliştiricinin Claude hesabı ele geçirildi. Bilgisayarındaki bir VS Code eklentisi dokuz gün boyunca arka planda zararlı yazılım indirdi. Saldırgan, oturum anahtarıyla hesaba girdi ve Claude Code'a başkası adına kod yazdırdı. O gece olaya Claude ile birlikte müdahale ettik.

Bu depo, o gecenin dersleriyle hazırlandı. Üç bölümü var:

1. **Kurmadan önce:** bir depo, eklenti ya da araç kurulmadan önce yapılması zorunlu kontroller.
2. **Olay anında:** hesabınız ya da bilgisayarınız ele geçirildiğinde ilk 15 dakika, ilk saat ve ilk gün.
3. **Claude ile adli inceleme:** kaynağı bulmak için sırayla kullandığımız üç istemin tam metni ve neden bu sırayla verildiği.

> Bu rehber hukuki ya da profesyonel adli bilişim hizmetinin yerine geçmez. Ciddi bir olayda kurumunuzun güvenlik ekibiyle ya da bir uzmanla çalışın.

---

## 1. Kurmadan önce: olmazsa olmaz kontroller

Bir depoyu klonlamadan, bir eklentiyi ya da paketi kurmadan, bir kurulum betiğini çalıştırmadan önce şu soruların hepsinin cevabı "evet" olmalıdır. Bir tanesi bile "hayır" ise kurmayın.

### 1.1 Kaynak

1. **Resmî kaynaktan mı geliyor?** VS Code eklentisi Marketplace'ten, npm paketi npm'den, araç kendi resmî sitesinden ya da resmî GitHub deposundan mı? Bir YouTube açıklamasından, Discord mesajından, WhatsApp grubundan ya da "yoruma yaz göndereyim" diye DM'den gelen VSIX, ZIP veya EXE dosyası **kurulmaz**.
2. **Yayıncı doğrulanmış mı?** Marketplace'te doğrulanmış yayıncı işaretine, GitHub'da kuruluş hesabına bakın. Bilinen bir ürünün adını taklit eden adlara (harf değişikliği, ek kelime) dikkat edin.
3. **"Kırılmış", "bedava Claude/GPT", "sınırsız token" vaadi var mı?** Varsa kurmayın. Bu vaat, zararlı yazılım dağıtmanın en yaygın yemidir.

### 1.2 Kimlik ve geçmiş

4. **Depo ya da yayıncı ne kadar eski?** Birkaç günlük bir hesap, tek katkıcı, ani yıldız artışı ve boş geçmiş uyarı işaretidir.
5. **Topluluk ne diyor?** Ad ile birlikte "malware", "virus", "trojan" kelimelerini arayın. Bizim vakamızdaki eklenti için bağımsız bir araştırmacı uyarıyı olaydan önce yayımlamıştı.

### 1.3 Kodu çalıştırmadan okuyun

6. **Kurulum betikleri:** `package.json` içinde `preinstall`, `install` ve `postinstall` alanları neyi çalıştırıyor?
7. **Ne zaman çalışıyor?** VS Code eklentisinde `activationEvents` içinde `*` ya da `onStartupFinished` varsa eklenti her açılışta, siz bir şey yapmadan çalışır.
8. **Ne yapıyor?** Kodda süreç başlatma (`child_process`, `exec`, `spawn`), internetten dosya indirme (`fetch`, `https.get`), Temp ve AppData klasörlerine `.exe` yazma, `eval` ve uzun base64 blokları var mı?
9. **Boyut normal mi?** Bizim vakamızdaki eklentinin tek kod dosyası 36 MB'tı. Okunamayacak kadar büyük ya da karartılmış (obfuscated) kod tek başına uyarı işaretidir.
10. **Tek satırlık kurulumlar:** `curl … | sh` ve `irm … | iex` komutlarını doğrudan çalıştırmayın. Önce betiği indirin, okuyun, sonra karar verin. Korsan etkinleştirme betikleri hiç çalıştırılmaz.

### 1.4 Tara ve ayrı ortamda dene

11. **Hash ile tarayın:** Dosyanın SHA-256 değerini VirusTotal'da arayın. Kişisel veri taşıyan dosyaları yüklemeyin; yalnız hash ile arayın.
12. **Ayrı ortamda deneyin:** Yeni bir aracı önce sanal makinede, ayrı bir Windows kullanıcısında ya da bir geliştirme konteynerinde deneyin. Bu ortamda API anahtarı, tarayıcı oturumu ve şirket hesabı bulunmasın.

### 1.5 Yetki ve sırlar

13. **En az yetki:** Ajanlara ve eklentilere ev klasörünün tamamını değil, yalnız proje klasörünü verin. VS Code'da Çalışma Alanı Güveni (Workspace Trust) açık kalsın; tanımadığınız klasörleri Kısıtlı Kip'te açın.
14. **Sırlar düz dosyada durmasın:** API anahtarlarını `.env` ya da metin dosyasında değil, işletim sisteminin anahtar zincirinde veya bir sır yöneticisinde tutun. Anahtarları kapsamı dar ve süresi kısa olacak şekilde üretin.
15. **İki adımlı doğrulama:** E-posta, GitHub ve yapay zekâ hesaplarınızda açık olsun. E-posta bütün hesaplarınızın anahtarıdır.

### 1.6 Kurduktan sonra

16. **İlk günleri izleyin:** Windows Güvenliği → Koruma geçmişi, açılışta çalışan programlar ve tanımadığınız süreçler. Bizim vakamızda Defender dokuz gün boyunca her gün bir tespit kaydetti; kimse bakmadığı için fark edilmedi.
17. **Ekipte kural olsun:** Şirket bilgisayarlarında ve ortak hesaplarda yalnız onaylı listedeki araçlar kurulur.

---

## 2. Olay anında

### İlk 15 dakika: durdur ve delili koru

- **Silmeyin.** Oturumları, depoları ve dosyaları silmek saldırganın izini de siler.
- **Fotoğraflayın:** oturum listesi, bağlı uygulamalar, fatura ve kullanım ekranı.
- **Ajan oturumunu durdurun**, ama arşivlemeyin ve o oturumla konuşmaya devam etmeyin.
- **Bilgisayarı ele geçirilmiş sayın.** O bilgisayarda bir daha şifre yazmayın.
- **Yalnız çözmeyin:** bir kişi müdahaleyi yönetsin, biri saat saat kayıt tutsun.

### İlk saat: kapıları temiz bir cihazdan kapatın

- **Önce e-posta:** şifre, iki adımlı doğrulama, bütün cihazlardan çıkış ve üçüncü taraf erişimleri.
- **Yapay zekâ hesabı:** tüm cihazlardan çıkış; bağlı GitHub hesabı size ait değilse bağlantıyı kesin.
- **GitHub:** oturumlar, kişisel erişim tokenları, SSH anahtarları ve yetkili uygulamalar.
- **API anahtarları:** o bilgisayarda bulunan her anahtarı iptal edin ve yenileyin.
- **Ekip erişimi:** kişiyi kuruluş depolarından geçici olarak çıkarın, son commit ve push kayıtlarını kontrol edin.
- **İnterneti kesin.** Bilgisayar inceleme bitene kadar ağa bağlanmasın.

### İlk gün: kök neden, bildirim, temizlik

- Aşağıdaki üç istemle salt okunur adli inceleme yapın.
- Hizmet sağlayıcıya ve kötüye kullanılan platforma, oturum kimlikleri, saatler ve kanıtlarla bildirin.
- **Doğru format:** Kurulum belleğini başka, temiz bir bilgisayarda resmî araçla hazırlayın ve bütün disk bölümlerini silin. "Dosyalarımı koru" yetmez.
- Yedekte yalnız belgeler ve kaynak kod olsun. `.exe`, `.vsix`, `node_modules`, `.vscode` ve tarayıcı profili alınmaz.
- Ayar eşitlemesi (Settings Sync) zararlı eklentiyi geri getirebilir. Açmadan önce eklenti listesini kontrol edin.

---

## 3. Claude ile adli inceleme: üç istem

Ele geçirilmiş bilgisayarda yeni bir **yerel** Claude Code oturumu açtık. Saldırganın oturumu kullanılmadı. Üç istem sırayla verildi.

### Neden bu sırayla?

| Sıra | Amaç | Neden önce bu |
|---|---|---|
| 1 | **Gözle:** geniş ve salt okunur tarama | Neyin olduğunu bilmeden bir şüpheliye odaklanırsanız yanlış yeri ararsınız. İlk istem hiçbir şeyi değiştirmeden bütün tabloyu çıkarır. |
| 2 | **Daralt:** şüpheliyi sorgula | Birinci tarama aday gösterir: zamanlama çakışan kurulumlar ve tespitler. İkinci istem adayın kimliğini ve kodunu kanıta karşı sınar. "Zaman çakışması mı, yoksa kodda iz mi?" sorusu burada sorulur. |
| 3 | **Mühürle:** delil paketi | Bulgular ekranda kaldıkça değiştirilebilir ve kaybolabilir. Format atılmadan önce ham metin ve SHA-256 özetleriyle değişmez hâle getirilir. Rapor ve bildirim bu paketle yapılır. |

Üç istemin ortak kuralları değişmez: **yalnız okuma, hiçbir şeyi silmeme ya da değiştirmeme, internete veri göndermeme ve şifre, anahtar ya da çerez değerlerini ekrana yazmama.**

### İstem 1 · Geniş tarama

```text
Bu bilgisayarda bir güvenlik olayı inceliyoruz. [TARİH, SAAT ARALIĞI] arasında birisi bu kullanıcının
[HESAP] hesabıyla işlem yaptı. Bilgisayarda bunu mümkün kılan bir program ya da iz olup olmadığını arıyoruz.

KURALLAR: Yalnız okuma yap. Hiçbir dosyayı silme, değiştirme, taşıma; hiçbir programı kaldırma ya da
durdurma; hiçbir şey indirme veya kurma; internete veri gönderme. Her komutu çalıştırmadan önce ne
yaptığını tek cümleyle söyle. Bulduğun şifre, anahtar ya da çerez değerlerini ekrana YAZMA, yalnız
"şurada anahtar var" de.

KONTROL ET (PowerShell ile):
1. Son 10 günde kurulan programlar.
2. Açılışta çalışanlar: Başlangıç klasörleri, Run ve RunOnce anahtarları.
3. Microsoft dışı zamanlanmış görevler: oluşturulma tarihi ve çalıştırdığı komutla.
4. Çalışan süreçler ve dışarıya açık bağlantılar; tanınmayanları işaretle.
5. Tarayıcı eklentileri: ad, kimlik, kurulma tarihi.
6. Bilgisayardaki yapay zekâ ajan uygulamaları: nerede kurulu, ne zaman kuruldu, imzalı mı,
   hangi klasörlere erişimi var, hangi sunuculara bağlanıyor.
7. Yapay zekâ araçlarının ayar klasörlerinde olay günleri değişen dosyalar (yalnız ad ve tarih).
8. Uzak masaüstü ve uzaktan erişim programları, Windows Uzak Masaüstü'nün durumu.
9. Windows Defender'ın durumu ve son tespitleri.

SONUÇ: Bulguları "şüpheli / incelenmeli / normal" diye üç gruba ayır, her birinde kanıtı (yol, tarih)
yaz. Olay tarihine yakın her şeyi öne çıkar. Hiçbir düzeltme yapma; önerini ayrıca yaz.
```

### İstem 2 · Şüpheliyi sorgula

```text
Öne çıkan eklentiler ve programlar için şunları ham olarak göster: tam kimlik (yayıncı.ad), sürüm,
kurulma ve güncellenme tarihi, kaynağı (resmî mağaza mı, VSIX ya da indirilmiş dosya mı), klasör yolu.

Her biri için zararlı yazılımla bağı neye dayanıyor: yalnız zaman çakışması mı, yoksa kodunda veya
günlüğünde dosya indirme, Temp'e yazma, cmd ya da PowerShell çalıştırma izi var mı? Klasörlerde Temp'e
.exe yazan, internetten dosya indiren ya da child_process ile program çalıştıran kod satırlarını
dosya:satır olarak listele. Defender tespit anları ile programın başlama anlarını yan yana bir tabloya
koy. Hiçbir şeyi değiştirme ya da silme.
```

### İstem 3 · Delil paketi

```text
Bulduğun her şeyi ham metin olarak bir delil paketine yaz.

KURALLAR: Yalnız masaüstünde vaka-kanit adında yeni bir klasör aç ve sadece oraya yaz. Başka hiçbir
dosyayı değiştirme, silme ya da taşıma. Şüpheli eklentiyi silme ve devre dışı bırakma. Hiçbir exe, dll,
betik ya da arşiv dosyasını bu klasöre kopyalama. Şifre, anahtar, belirteç ve çerez değerlerini hiçbir
dosyaya yazma; yalnız dosya yolunu ve tarihini yaz. İnternete hiçbir şey gönderme.

Klasöre ayrı metin dosyaları olarak yaz: inceleme raporunun tam metni; bu oturumda çalıştırdığın bütün
komutlar; Defender tespitleri; şüpheli dosyaların tam SHA-256 değeri, boyutu, tarihi, imza durumu ve
sürüm bilgisi; Temp klasöründeki exe listesi; şüpheli eklentinin manifesti ve kod dosyasının SHA-256
değeri; zaman eşleşmesi tablosu; eklenti listesi; terminal geçmişi (şifre içeren satırlar gizlenmiş);
yapay zekâ uygulamasının günlüğünden olay saatleri; açılışta çalışanlar ve bağlantılar; son kurulumlar.
En sonda klasördeki her dosyanın SHA-256 değerini ozetler.txt dosyasına yaz.
```

Paketi bilgisayardan alırken yalnız metin dosyalarını alın ve her dosyanın SHA-256 değerini `ozetler.txt` ile karşılaştırın. Bizim vakamızda 12 dosyanın hepsi aktarımdan sonra birebir tuttu.

---

## Kaynaklar

- Anthropic, Tehdit İstihbaratı Raporu, Eylül 2026: https://www.anthropic.com/threat-intelligence-report-september-2026
- Bağımsız alpme raporu: https://github.com/PenguinBTW/alpme-detector
- Claude Destek, API anahtarı ele geçirildiyse: https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised

Olayı Anthropic'e ve GitHub'a kanıtlarıyla bildirdik. Ekran görüntüleri ekip arkadaşımızın rızasıyla paylaşılmıştır.

**Nexivion Labs** · nexivionlabs.io
