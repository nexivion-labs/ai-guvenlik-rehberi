# 11. Yedekleme ve kurtarma

[← İçindekiler](../README.md)

Rehberin birçok adımı sonunda "yedekten geri yükleyin" der. Bu bölüm o cümlenin arkasını doldurur. Temel fikir tek cümle: **denenmemiş yedek, yedek değildir.** Ajanların işe karışmasıyla bu daha da önemli hâle geldi: bir ajan, bir yedeği silebileceği gibi, yanlış anlaşılmış bir görevle üretim verisini de silebilir ([S6](08-senaryolar.md#s6-ajan-geri-alınamayan-bir-işlem-yaptı)).

---

## 11.1 Neyin yedeği?

| Varlık | Nerede durur | Yedek nasıl |
|---|---|---|
| Kaynak kod | Git deposu (GitHub) | Uzak depo zaten bir kopyadır; ama **tek kopya değildir**. Kuruluş deposunun düzenli bir klon ya da arşiv kopyası başka bir yerde dursun (GitHub'ın kendi dışa aktarma özelliği ya da haftalık `git clone --mirror`). Ele geçirilen bir hesap depoyu silebilir ya da geçmişi yeniden yazabilir. |
| Veritabanı | Üretim sunucusu / yönetilen hizmet | Otomatik günlük yedek + zamana göre geri dönüş (point-in-time) açık olsun. Yedekler **ayrı bir hesapta ya da ayrı kimlik bilgisiyle** erişilen bir yerde dursun; üretim anahtarı yedeği silemesin. |
| Sırlar ve yapılandırma | Sır yöneticisi | Sır yöneticisinin kendi yedeği ya da şifreli dışa aktarımı; kurtarma anahtarı çevrimdışı. Sırları git'e yedeklemeyin. |
| Kişisel belgeler | Bilgisayar | Bulut eşitleme yedek değildir (silinen dosya her yerde silinir). Sürüm geçmişi tutan bir yedek aracı ya da düzenli çevrimdışı kopya. |
| Ajan yapılandırması | `.claude/`, `CLAUDE.md`, `.npmrc` vb. | Depoda, kodla birlikte. Oturum geçmişi (`~/.claude/` altındaki konuşmalar) **yedeklenmez**; sır içerebilir ([Bölüm 4.8](04-claude-code-sertlestirme.md#48-oturum-geçmişi-de-bir-sırdır)). |

## 11.2 3-2-1 kuralı, ajan çağı için

Klasik kural: en az **3** kopya, **2** farklı ortamda, **1**'i başka bir yerde. Buna iki şey ekleyin:

- **1 kopya değiştirilemez (immutable) ya da çevrimdışı olsun.** Ajanın ya da ele geçirilmiş bir hesabın erişebildiği her kopya tek bir komutla gidebilir. Bulut depolamada nesne kilidi (object lock), yerelde takılı olmayan bir disk.
- **0 kopya ajanın çalışma klasöründe olsun.** Ajanın yazabildiği yerde duran yedek, ajanın silebileceği yedektir. Sandbox'ta yazma izni çalışma klasörüyle sınırlıyken bile `allowWrite` ile açtığınız bir yedek klasörü aynı riski taşır.

## 11.3 Geri yükleme tatbikatı (üç ayda bir, 30 dakika)

1. Rastgele bir yedek seçin (en sonuncusu değil; iki hafta öncekini).
2. Üretimden **ayrı** bir ortama geri yükleyin. Üretime geri yükleme denemesi yapmayın.
3. Üç şeyi doğrulayın: açılıyor mu, kayıt sayıları beklenen aralıkta mı, bir örnek işlem (ör. bir kullanıcı sorgusu) doğru sonuç veriyor mu?
4. Süreyi ölçün: "yedekten dönmek ne kadar sürüyor?" sorusunun cevabı bir sayı olmalı. Olay anında bu sayıya göre karar verirsiniz.
5. Sonucu [tatbikat kaydına](../sablonlar/masa-basi-tatbikat.md#tatbikat-sonrası-kayıt) yazın. Başarısızsa bu bir bulgudur, utanç değil; yedek düzeltilene kadar P0.

## 11.4 Ajan ve yedek: kurallar

- Ajanın çalıştığı kimlik bilgisiyle yedekler **silinemesin**. Çoğu bulut sağlayıcısında yedek silme yetkisi ayrı bir izindir; ajana verilen role bu izni eklemeyin.
- Ajana "veritabanını temizle", "eski kayıtları sil", "migration çalıştır" gibi görevler verilecekse önce bir anlık görüntü (snapshot) alınsın ve bu adım görevin parçası olsun: "önce snapshot al, kimliğini yaz, sonra devam et".
- Geri yükleme komutları (`pg_restore`, `terraform apply` ile yeniden oluşturma vb.) ajanda `ask` listesinde olsun; yanlış ortama geri yükleme, silmek kadar yıkıcıdır.

## 11.5 Olaydan sonra geri yüklerken

- Yedeğin **olay öncesinden** olduğundan emin olun; aksi hâlde zararlıyı ya da saldırganın değişikliklerini geri getirirsiniz. Kaynak kod için [Bölüm 2](02-olay-aninda.md)'deki gibi son temiz commit'i doğrulayın.
- Geri yüklenen ortamda eski anahtarlar bulunabilir (yapılandırma dosyaları, ortam değişkenleri). Geri yüklemeden sonra bütün anahtarları yenileyin; yedekte duran anahtar, yedek alındığı andaki anahtardır ve sızmış olabilir.
- Geri yükleme de bir olay kaydı satırıdır: ne zaman, hangi yedekten, kim.

---

**İlgili:** [S6 Ajan geri alınamayan bir işlem yaptı](08-senaryolar.md#s6-ajan-geri-alınamayan-bir-işlem-yaptı) · [Bölüm 2, ilk gün](02-olay-aninda.md) · [Masa başı tatbikat](../sablonlar/masa-basi-tatbikat.md)
