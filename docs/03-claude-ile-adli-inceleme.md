# 3. Claude ile adli inceleme: üç istem

[← İçindekiler](../README.md)

Ele geçirilmiş bilgisayarda yeni bir **yerel** Claude Code oturumu açtık. Saldırganın oturumu kullanılmadı. Üç istem sırayla verildi.

## 3.1 Başlamadan önce: riskleri bilin

Ele geçirilmiş bir bilgisayarda, kabuk komutu çalıştırabilen bir ajan başlatmak bilinçli bir risk almaktır. Bizim vakamızda işe yaradı; sizin vakanızda şu üç riski tartın:

| Risk | Neden önemli | Ne yapılır |
|---|---|---|
| **Yeni kimlik bilgisi sızar** | Ajanı başlatmak için giriş yaparsanız ya da anahtar girerseniz, bilgisayardaki zararlı yazılım bunu da alabilir. | İnceleme için **ayrı, yeni** bir hesap ya da yalnız bu iş için üretilmiş, harcama limiti düşük bir API anahtarı kullanın. İnceleme biter bitmez iptal edin. Asıl hesabınıza o bilgisayardan asla giriş yapmayın. |
| **Ağ açık kalır** | Claude Code'un çalışması için internet gerekir; olay anında ilk 15 dakikada ağı [kesmiştik](02-olay-aninda.md). | Ağı yalnız inceleme süresince açın. Mümkünse yalnız sağlayıcının API adresine izin veren bir güvenlik duvarı kuralı ya da ayrı bir ağ (telefon paylaşımı) kullanın. Bitince yeniden kesin. |
| **İstem enjeksiyonu** | Ajan, saldırganın bıraktığı dosyaları ve günlükleri okur. Bu dosyalar ajanı yönlendirmeye çalışan metin içerebilir ("bu dosyayı sil", "şu adrese gönder"). | İstemlerdeki "yalnız okuma" kuralı bu yüzden var. Her komutu çalıştırmadan önce okuyun ve **otomatik onay kipini kullanmayın**. Ajan kuraldan sapan bir şey önerirse durdurun. Ayrıntı: [Bölüm 5](05-istem-enjeksiyonu-ve-mcp.md). |

Ayrıca incelemede çıkan **süreç listeleri, dosya yolları ve günlükler sağlayıcının sunucularına gider**. Müşteri verisi ya da gizlilik yükümlülüğü olan bir bilgisayarsa bunu kurum politikanıza göre değerlendirin.

### Daha temkinli seçenek

Ajanı ele geçirilmiş bilgisayarda hiç çalıştırmamak da mümkündür: aynı kontrollerin komutlarını (aşağıdaki istemlerdeki maddeler) elle çalıştırıp çıktıları **yalnız metin dosyası** olarak bir USB belleğe yazın, dosyaların SHA-256 değerlerini alın ve analizi **temiz bir bilgisayarda** Claude ile yapın. Daha yavaştır ama yukarıdaki üç riskin ilk ikisini ortadan kaldırır.

## 3.2 Neden bu sırayla?

| Sıra | Amaç | Neden önce bu |
|---|---|---|
| 1 | **Gözle:** geniş ve salt okunur tarama | Neyin olduğunu bilmeden bir şüpheliye odaklanırsanız yanlış yeri ararsınız. İlk istem hiçbir şeyi değiştirmeden bütün tabloyu çıkarır. |
| 2 | **Daralt:** şüpheliyi sorgula | Birinci tarama aday gösterir: zamanlama çakışan kurulumlar ve tespitler. İkinci istem adayın kimliğini ve kodunu kanıta karşı sınar. "Zaman çakışması mı, yoksa kodda iz mi?" sorusu burada sorulur. |
| 3 | **Mühürle:** delil paketi | Bulgular ekranda kaldıkça değiştirilebilir ve kaybolabilir. Format atılmadan önce ham metin ve SHA-256 özetleriyle değişmez hâle getirilir. Rapor ve bildirim bu paketle yapılır. |

Üç istemin ortak kuralları değişmez: **yalnız okuma, hiçbir şeyi silmeme ya da değiştirmeme, internete veri göndermeme ve şifre, anahtar ya da çerez değerlerini ekrana yazmama.**

Köşeli parantezli yerleri (`[TARİH, SAAT ARALIĞI]`, `[HESAP]`) kendi olayınıza göre doldurun.

## 3.3 İstem 1 · Geniş tarama (Windows)

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

### İstem 1 · macOS ve Linux için KONTROL ET bölümü

Kurallar ve sonuç bölümü aynı kalır; yalnız KONTROL ET kısmını değiştirin.

```text
KONTROL ET (macOS, zsh ile):
1. Son 10 günde kurulan ya da değişen uygulamalar (/Applications, ~/Applications) ve Homebrew paketleri.
2. Açılışta çalışanlar: ~/Library/LaunchAgents, /Library/LaunchAgents, /Library/LaunchDaemons ve
   launchctl list çıktısı; her birinin çalıştırdığı program ve oluşturulma tarihi. Yönetici şifresi
   isteyen komut (sudo) KULLANMA; bu bilgisayarda şifre yazılmayacak.
3. crontab ve zamanlanmış işler.
4. Çalışan süreçler ve dışarıya açık bağlantılar (lsof -i); tanınmayanları işaretle.
5. Tarayıcı eklentileri: ad, kimlik, kurulma tarihi.
6. Yapay zekâ ajan uygulamaları ve editör eklentileri (~/.vscode/extensions, ~/.cursor/extensions vb.):
   nerede kurulu, ne zaman kuruldu, imzalı mı (codesign), hangi sunuculara bağlanıyor.
7. Yapay zekâ araçlarının ayar klasörlerinde (~/.claude, ~/.config vb.) olay günleri değişen dosyalar
   (yalnız ad ve tarih).
8. Uzaktan erişim programları, Ekran Paylaşımı ve Uzaktan Oturum Açma (SSH) durumu.
9. Kabuk başlangıç dosyalarında (~/.zshrc, ~/.zprofile, ~/.bash_profile) son değişiklikler.
```

```text
KONTROL ET (Linux, bash ile):
1. Son 10 günde kurulan paketler (apt/dnf/pacman günlükleri), ~/.local/bin ve /usr/local/bin'de yeni dosyalar.
2. Açılışta çalışanlar: systemctl --user ve sistem servisleri, ~/.config/autostart, /etc/xdg/autostart.
3. crontab (kullanıcı ve /etc/cron*) ve systemd zamanlayıcıları.
4. Çalışan süreçler ve dışarıya açık bağlantılar (ss -tunap); tanınmayanları işaretle.
5. Tarayıcı eklentileri: ad, kimlik, kurulma tarihi.
6. Yapay zekâ ajan uygulamaları ve editör eklentileri (~/.vscode/extensions vb.): nerede kurulu,
   ne zaman kuruldu, hangi sunuculara bağlanıyor.
7. Yapay zekâ araçlarının ayar klasörlerinde (~/.claude, ~/.config vb.) olay günleri değişen dosyalar
   (yalnız ad ve tarih).
8. SSH: ~/.ssh/authorized_keys içindeki anahtarlar ve son değişme tarihi; uzaktan erişim programları.
9. Kabuk başlangıç dosyalarında (~/.bashrc, ~/.profile) son değişiklikler.
```

## 3.4 İstem 2 · Şüpheliyi sorgula

```text
Öne çıkan eklentiler ve programlar için şunları ham olarak göster: tam kimlik (yayıncı.ad), sürüm,
kurulma ve güncellenme tarihi, kaynağı (resmî mağaza mı, VSIX ya da indirilmiş dosya mı), klasör yolu.

Her biri için zararlı yazılımla bağı neye dayanıyor: yalnız zaman çakışması mı, yoksa kodunda veya
günlüğünde dosya indirme, Temp'e yazma, cmd ya da PowerShell çalıştırma izi var mı? Klasörlerde Temp'e
.exe yazan, internetten dosya indiren ya da child_process ile program çalıştıran kod satırlarını
dosya:satır olarak listele. Defender tespit anları ile programın başlama anlarını yan yana bir tabloya
koy. Hiçbir şeyi değiştirme ya da silme.
```

macOS/Linux'ta "Temp'e .exe yazma" yerine `/tmp`'ye çalıştırılabilir dosya yazma, `chmod +x` ve `curl | sh` izlerini; "Defender tespitleri" yerine kullandığınız güvenlik aracının kayıtlarını sorun.

## 3.5 İstem 3 · Delil paketi

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

## 3.6 Paketi bilgisayardan almak

Paketi bilgisayardan alırken yalnız metin dosyalarını alın ve her dosyanın SHA-256 değerini `ozetler.txt` ile karşılaştırın. Bizim vakamızda 12 dosyanın hepsi aktarımdan sonra birebir tuttu.

Temiz bilgisayarda doğrulama:

```bash
# Linux: ozetler.txt "<hash>  <dosya>" biçimindeyse
cd vaka-kanit && sha256sum -c ozetler.txt
# macOS (sha256sum yoktur):
cd vaka-kanit && shasum -a 256 -c ozetler.txt
```

```powershell
# Windows: her dosyanın hash'ini listeleyip ozetler.txt ile karşılaştırın
Get-ChildItem .\vaka-kanit -File | Where-Object Name -ne 'ozetler.txt' | Get-FileHash -Algorithm SHA256 | Format-Table Hash, Path -AutoSize
```

İpuçları:

- Aktarım için boş, yeni biçimlendirilmiş bir USB bellek kullanın. Belleği temiz bilgisayara takmadan önce otomatik çalıştırmanın kapalı olduğundan emin olun.
- Paketin bir kopyasını değişmez bir yerde saklayın (ör. salt okunur paylaşım ya da yazılabilir olmayan bir arşiv). Bildirimde paylaştığınız dosyaların hash'lerini de kayda geçirin.
- Ajanın raporu bir **hipotezdir**. Bildirimde "kesin kaynak" demeden önce, kod satırı ya da günlük kaydı gibi doğrudan kanıta dayandığından emin olun.

---

**Önceki:** [← 2. Olay anında](02-olay-aninda.md) · **Sonraki:** [4. Claude Code'u sertleştirme →](04-claude-code-sertlestirme.md)
