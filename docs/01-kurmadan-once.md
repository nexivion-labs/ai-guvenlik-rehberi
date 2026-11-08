# 1. Kurmadan önce: olmazsa olmaz kontroller

[← İçindekiler](../README.md) · Yazdırılabilir hâli: [kontrol-listeleri/kurmadan-once.md](../kontrol-listeleri/kurmadan-once.md)

Bir depoyu klonlamadan, bir eklentiyi ya da paketi kurmadan, bir kurulum betiğini çalıştırmadan önce aşağıdaki soruların hepsinin cevabı "evet" olmalıdır. Bir tanesi bile "hayır" ise kurmayın.

> **Neden bu kadar katı?** Yapay zekâ ajanları bilgisayarınızda sizin yetkinizle dosya okur, komut çalıştırır ve ağa bağlanır. Bilgisayara giren her araç, ajanın da elindeki her şeye dolaylı olarak erişir: API anahtarları, oturum bilgileri, kaynak kod. Vakamızda tek bir eklenti, dokuz gün içinde Claude hesabını ele geçirmeye yetti.

---

## 1.1 Kaynak

1. **Resmî kaynaktan mı geliyor?** VS Code eklentisi Marketplace'ten, npm paketi npm'den, araç kendi resmî sitesinden ya da resmî GitHub deposundan mı? Bir YouTube açıklamasından, Discord mesajından, WhatsApp grubundan ya da "yoruma yaz göndereyim" diye DM'den gelen VSIX, ZIP veya EXE dosyası **kurulmaz**.
2. **Yayıncı doğrulanmış mı?** Marketplace'te doğrulanmış yayıncı işaretine, GitHub'da kuruluş hesabına bakın. Bilinen bir ürünün adını taklit eden adlara (harf değişikliği, ek kelime, `-pro`, `-free`, `-official` ekleri) dikkat edin. Doğrulanmış işaret tek başına güvence değildir; yalnız alan adının sahibini gösterir.
3. **"Kırılmış", "bedava Claude/GPT", "sınırsız token" vaadi var mı?** Varsa kurmayın. Bu vaat, zararlı yazılım dağıtmanın en yaygın yemidir.
4. **Alternatif pazar yerlerine dikkat.** Cursor, Windsurf, VSCodium gibi editörler eklentileri çoğunlukla Open VSX'ten çeker. Open VSX'te aynı ada sahip ama farklı yayıncıya ait eklentiler bulunabilir. Eklenti kimliğini (`yayıncı.ad`) resmî kaynaktakiyle birebir karşılaştırın.

## 1.2 Kimlik ve geçmiş

5. **Depo ya da yayıncı ne kadar eski?** Birkaç günlük bir hesap, tek katkıcı, ani yıldız artışı ve boş geçmiş uyarı işaretidir.
6. **Topluluk ne diyor?** Ad ile birlikte "malware", "virus", "trojan", "stealer" kelimelerini arayın. Bizim vakamızdaki eklenti için bağımsız bir araştırmacı uyarıyı olaydan önce yayımlamıştı.
7. **Son sürüm neden çıktı?** Uzun süre güncellenmeyen bir paketin birden yeni bir sürüm yayımlaması, bakımcı hesabının ele geçirildiğinin işareti olabilir. Değişiklik notu yoksa ya da kodla uyuşmuyorsa birkaç gün bekleyin.

## 1.3 Kodu çalıştırmadan okuyun

8. **Kurulum betikleri:** `package.json` içinde `preinstall`, `install` ve `postinstall` alanları neyi çalıştırıyor? Python'da `setup.py` dosyası kurulum sırasında kod çalıştırabilir.
9. **Ne zaman çalışıyor?** VS Code eklentisinde `activationEvents` içinde `*` ya da `onStartupFinished` varsa eklenti her açılışta, siz bir şey yapmadan çalışır.
10. **Ne yapıyor?** Kodda süreç başlatma (`child_process`, `exec`, `spawn`, `subprocess`), internetten dosya indirme (`fetch`, `https.get`, `curl`, `Invoke-WebRequest`), Temp ve AppData klasörlerine `.exe` yazma, `eval`/`new Function` ve uzun base64 blokları var mı?
11. **Boyut normal mi?** Bizim vakamızdaki eklentinin tek kod dosyası 36 MB'tı. Okunamayacak kadar büyük ya da karartılmış (obfuscated) kod tek başına uyarı işaretidir.
12. **Tek satırlık kurulumlar:** `curl … | sh` ve `irm … | iex` komutlarını doğrudan çalıştırmayın. Önce betiği indirin, okuyun, sonra karar verin. Korsan etkinleştirme betikleri hiç çalıştırılmaz.

### VSIX dosyasını kurmadan incelemek

VSIX aslında bir ZIP arşividir. Kurmadan açıp bakabilirsiniz:

```bash
# Linux / macOS
mkdir vsix-inceleme && cd vsix-inceleme
unzip ../eklenti.vsix
cat extension/package.json        # activationEvents, main, scripts alanlarına bakın
ls -la extension/                  # dosya boyutlarına bakın
grep -rnE "child_process|exec\(|spawn\(|https\.get|eval\(" extension/ --include=*.js | head -50
```

```powershell
# Windows PowerShell
Expand-Archive -Path .\eklenti.vsix -DestinationPath .\vsix-inceleme
Get-Content .\vsix-inceleme\extension\package.json
Get-ChildItem .\vsix-inceleme\extension -Recurse | Sort-Object Length -Descending | Select-Object -First 10 FullName, Length
Get-ChildItem .\vsix-inceleme\extension -Recurse -Filter *.js | Select-String -Pattern "child_process","exec\(","spawn\(","https\.get","eval\(" | Select-Object -First 50
```

Bu komutlar yalnız okur; hiçbir şey kurmaz ya da çalıştırmaz. Yine de karartılmış kodda bu aramalar bir şey bulmayabilir. "Bulamadım" demek "temiz" demek değildir.

## 1.4 Tara ve ayrı ortamda dene

13. **Hash ile tarayın:** Dosyanın SHA-256 değerini VirusTotal'da arayın. Kişisel veri taşıyan dosyaları yüklemeyin; yalnız hash ile arayın.

    ```bash
    sha256sum dosya.vsix                  # Linux
    shasum -a 256 dosya.vsix              # macOS
    ```
    ```powershell
    Get-FileHash .\dosya.vsix -Algorithm SHA256   # Windows
    ```

    Temiz sonuç, dosyanın güvenli olduğunu kanıtlamaz; yeni zararlılar ilk günlerde tespit edilmeyebilir.

14. **Ayrı ortamda deneyin:** Yeni bir aracı önce sanal makinede, ayrı bir işletim sistemi kullanıcısında ya da bir geliştirme konteynerinde (Dev Container) deneyin. Bu ortamda API anahtarı, tarayıcı oturumu ve şirket hesabı bulunmasın. Windows'ta Windows Sandbox da hızlı bir seçenektir.

## 1.5 Yetki ve sırlar

15. **En az yetki:** Ajanlara ve eklentilere ev klasörünün tamamını değil, yalnız proje klasörünü verin. VS Code'da Çalışma Alanı Güveni (Workspace Trust) açık kalsın; tanımadığınız klasörleri Kısıtlı Kip'te açın. Claude Code için ayrıntılar: [Bölüm 4](04-claude-code-sertlestirme.md).
16. **Sırlar düz dosyada durmasın:** API anahtarlarını `.env` ya da metin dosyasında değil, işletim sisteminin anahtar zincirinde veya bir sır yöneticisinde tutun. Anahtarları kapsamı dar ve süresi kısa olacak şekilde üretin. `.env` kullanmak zorundaysanız `.gitignore`'a ekleyin ve ajanın okumasını [engelleyin](04-claude-code-sertlestirme.md#43-sırlara-erişimi-kapatın).
17. **İki adımlı doğrulama:** E-posta, GitHub ve yapay zekâ hesaplarınızda açık olsun. E-posta bütün hesaplarınızın anahtarıdır. Mümkünse SMS yerine doğrulama uygulaması ya da donanım anahtarı (passkey, YubiKey) kullanın.
18. **Ayar eşitlemesine dikkat:** VS Code Settings Sync, eklenti listenizi ve bazı eklentilerin ayar dosyalarını buluta taşır. Bazı eklentiler (ör. bazı MCP istemcileri) sırları düz metin ayar dosyalarında tutar. Eşitlenen şeyin ne olduğunu bilin.

## 1.6 Kurduktan sonra

19. **İlk günleri izleyin** (bütün platformların komutları: [Bölüm 10](10-platform-basvuru-karti.md)): Windows Güvenliği → Koruma geçmişi, açılışta çalışan programlar ve tanımadığınız süreçler. Bizim vakamızda Defender dokuz gün boyunca her gün bir tespit kaydetti; kimse bakmadığı için fark edilmedi. macOS'ta Sistem Ayarları → Genel → Oturum Açma Öğeleri ve `~/Library/LaunchAgents`, Linux'ta `systemctl --user list-unit-files` ve `crontab -l` bakılacak ilk yerlerdir.
20. **Ekipte kural olsun:** Şirket bilgisayarlarında ve ortak hesaplarda yalnız [onaylı listedeki](../sablonlar/onayli-araclar.md) araçlar kurulur. VS Code'da bu kural teknik olarak da uygulanabilir: [Bölüm 6.3](06-tedarik-zinciri.md#63-vs-code-eklenti-izin-listesi).

---

**Sonraki:** [2. Olay anında →](02-olay-aninda.md)
