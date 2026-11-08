# 7. Ekip politikası ve düzenli kontroller

[← İçindekiler](../README.md) · [Aylık kontrol listesi](../kontrol-listeleri/aylik-kontrol.md) · [Onaylı araçlar şablonu](../sablonlar/onayli-araclar.md)

Vakamızdaki en pahalı hata teknik değildi: Defender'ın dokuz gün boyunca kaydettiği tespitlere kimse bakmadı. Güvenlik araçları ancak birilerinin düzenli baktığı ölçüde işe yarar. Bu bölüm, küçük bir ekibin (2–20 kişi) uygulayabileceği hafif bir politika önerir.

---

## 7.1 Beş kural

1. **Onaylı liste.** Şirket bilgisayarlarında ve ortak hesaplarda yalnız [onaylı listedeki](../sablonlar/onayli-araclar.md) araçlar, eklentiler ve MCP sunucuları kullanılır. Listeye ekleme, bir kişinin [Bölüm 1](01-kurmadan-once.md) kontrollerini yapıp yazılı onay vermesiyle olur.
2. **Kişisel ve iş ayrı.** İş hesaplarına (GitHub kuruluşu, şirket API anahtarları, yapay zekâ ekip hesabı) korsan yazılım, oyun hilesi ya da "deneme" amaçlı araç kurulan bir bilgisayardan erişilmez.
3. **Paylaşılan anahtar yok.** Her kişinin kendi anahtarı, her projenin kendi kapsamı olur. Bir kişi ayrıldığında ya da bir olay olduğunda yalnız onun anahtarları iptal edilir, herkes etkilenmez.
4. **Olay bildirmek ödüllendirilir.** "Yanlış bir şey kurdum galiba" diyen kişi suçlanmaz. Erken bildirim, vakamızda olduğu gibi dokuz günlük gecikmeyi önler.
5. **Ayda bir kontrol.** Takvime yazılmış, sahibi belli, 30 dakikalık bir [aylık kontrol](../kontrol-listeleri/aylik-kontrol.md).

## 7.2 Roller (küçük ekip için)

| Rol | Sorumluluk |
|---|---|
| **Güvenlik sorumlusu** (bir kişi, yarı zamanlı) | Onaylı listeyi tutar, aylık kontrolü takip eder, olay anında müdahaleyi yönetir. |
| **Yedek sorumlu** | Sorumlu yokken olayı yönetir. Olay anında kayıt tutan kişi genelde odur. |
| **Herkes** | Kendi bilgisayarında aylık kontrolü yapar, şüpheli bir şeyi hemen bildirir. |

Olay anında kime, nereden (telefon, ayrı bir mesajlaşma grubu) ulaşılacağı önceden yazılı olsun. Ele geçirilmiş bilgisayardaki Slack ya da e-posta o anda güvenilir bir kanal değildir.

## 7.3 GitHub kuruluşu için asgari ayarlar

- Kuruluş genelinde **iki adımlı doğrulama zorunlu**.
- Varsayılan dala (main) **dal koruması**: doğrudan push yok, PR ve en az bir onay zorunlu. Ajan kendi başına `main`'e yazamasın.
- **Secret scanning ve push protection** açık: sırrı içeren bir commit'in push'u engellenir.
- **Fine-grained token** politikası: klasik token'lar yerine kapsamı dar, süresi sınırlı token'lar.
- GitHub Actions'ta üçüncü taraf eylemler **tam commit SHA'sıyla** sabitlensin (`uses: org/action@<sha>`), iş akışı token'ının (`GITHUB_TOKEN`) yetkisi varsayılan olarak salt okunur olsun.
- Ayda bir: kuruluş üyeleri, dış işbirlikçiler, yetkili OAuth uygulamaları ve deploy anahtarları gözden geçirilsin.

## 7.4 Ölçün: beş sayı

Politikanın işleyip işlemediğini hissiyatla değil sayıyla anlayın. Ayda bir aşağıdaki beş sayıyı yazın; kötüye giden bir sayı, bir sonraki ayın işidir.

| Ölçüt | Nasıl ölçülür | Hedef |
|---|---|---|
| Onaylı liste dışı araç sayısı | Aylık kontrolde bulunan, listede olmayan eklenti/araç | 0 |
| Güvenlik aracı tespitinin fark edilme süresi | Tespit zamanı ile birinin bakması arasındaki süre | < 1 gün (vakamızda 9 gündü) |
| Kullanılmayan anahtar ve oturum sayısı | Aylık kontrolde iptal edilenler | Azalan |
| Tatbikat tazeliği | Son masa başı tatbikatından bu yana geçen ay | ≤ 6 ay |
| Açık eylem sayısı | Geriye bakış ve tatbikatlardan çıkan, tarihi geçmiş eylemler | 0 |

## 7.5 Tatbikat yapın

Planın kâğıt üstünde kalıp kalmadığını anlamanın tek yolu denemektir. [Masa başı tatbikat şablonu](../sablonlar/masa-basi-tatbikat.md) 60 dakikalık bir akış ve beş senaryo içerir; ilk tatbikat için bu deponun kendi olayı hazır bir senaryodur.

## 7.6 Yeni katılan biri için ilk gün

- [ ] Bu rehberin [Bölüm 1](01-kurmadan-once.md) ve [Bölüm 2](02-olay-aninda.md)'sini okudu.
- [ ] E-posta, GitHub ve yapay zekâ hesabında iki adımlı doğrulama açık.
- [ ] Bilgisayarında yalnız onaylı araçlar var; VS Code eklenti izin listesi uygulandı.
- [ ] Claude Code ekip ayarları (`.claude/settings.json`) ve sandbox açık.
- [ ] Olay anında kime ulaşacağını biliyor.
- [ ] Kurtarma kodlarını bilgisayar dışında bir yere kaydetti.

## 7.7 Biri ayrıldığında

- [ ] GitHub kuruluşundan ve ekip yapay zekâ hesabından çıkarıldı.
- [ ] Kişiye ait ya da kişinin gördüğü bütün paylaşılan anahtarlar yenilendi.
- [ ] Kişinin oluşturduğu deploy anahtarları, webhook'lar ve OAuth uygulamaları gözden geçirildi.
- [ ] Kişinin bilgisayarı şirketinse geri alındı ve [S13](08-senaryolar.md#s13-dizüstü-bilgisayar-kayboldu-ya-da-çalındı) mantığıyla temizlendi; kişisel bilgisayarsa üzerindeki şirket anahtarları ve ajan yetkileri iptal edildi.

Ayrılış eksik kalırsa ne olur: [S15](08-senaryolar.md#s15-ayrılan-ekip-üyesinin-erişimi-kaldı).

---

**Önceki:** [← 6. Tedarik zinciri](06-tedarik-zinciri.md) · **Sonraki:** [8. Senaryolar →](08-senaryolar.md)
