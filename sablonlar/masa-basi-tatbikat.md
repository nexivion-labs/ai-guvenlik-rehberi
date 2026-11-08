# Masa başı tatbikat (60 dakika)

Tatbikat, gerçek bir olay olmadan "ne yapardık?" sorusunu masada cevaplamaktır. Küçük bir ekip için 60 dakika yeter. Yılda en az iki kez yapın; CIS Kontrolleri bunu 17.7 numaralı koruma olarak önerir. İlk tatbikatı bu depodaki gerçek olayla yapmanız kolaylık sağlar.

## Hazırlık (kolaylaştırıcı, 20 dakika, önceden)

- Aşağıdaki senaryolardan birini seçin, ekibe söylemeyin.
- Katılımcılar gerçek rolleriyle oynar (güvenlik sorumlusu, yedek, geliştiriciler). Kimse başka birini canlandırmaz.
- Masada şunlar açık olsun: [olay anı kontrol listesi](../kontrol-listeleri/olay-ani.md), [olay kaydı](olay-kaydi.md), [iletişim listesi](../docs/07-ekip-politikasi.md#72-roller-küçük-ekip-için).
- Bir kişi not tutar: hangi soruya kimse cevap veremedi, hangi bilgi bulunamadı, hangi adım tartışma çıkardı.

## Akış

| Dakika | Ne olur |
|---|---|
| 0–5 | Kolaylaştırıcı senaryonun ilk cümlesini okur. "Şu an saat 23:10, ne yapıyorsunuz?" |
| 5–20 | Ekip ilk 15 dakikayı konuşur. Kolaylaştırıcı araya "sürpriz" ekler (aşağıda). |
| 20–35 | İlk saat: kapılar hangi sırayla, kim, hangi cihazdan kapatılır? Gerçekten o hesaplara girebiliyor musunuz, kurtarma kodları nerede? |
| 35–45 | İlk gün: inceleme, bildirim, temizlik. Bildirim şablonu doldurulabiliyor mu? |
| 45–55 | Geriye bakış: notlardaki her boşluk için bir eylem, bir sahip, bir tarih. |
| 55–60 | Eylemler [olay kaydının](olay-kaydi.md) "Eylemler" tablosuna, dersler rehbere. |

## Senaryolar

1. **Bu deponun olayı:** Gece 23:00'te bir ekip üyesinin Claude hesabında tanımadığı Claude Code oturumları görünüyor. Sürpriz: üyenin iki adımlı doğrulama telefonu şarjı bitik; kurtarma kodlarının nerede olduğunu hatırlamıyor.
2. **Sızan anahtar:** GitHub'dan "herkese açık bir depoda bir anahtarınız bulundu" e-postası geldi. Anahtar iki gün önce ajanın açtığı bir PR'da. Sürpriz: aynı anahtar üretimde de kullanılıyor ve değiştirmek kesinti demek.
3. **Zararlı eklenti:** Bir geliştirici "yanlışlıkla bir VSIX kurdum galiba" diyor; Defender geçmişinde üç tespit var. Sürpriz: aynı eklenti Settings Sync ile ikinci bilgisayarına da gitmiş.
4. **CI'dan sızıntı:** Kullandığınız bir GitHub eylemi ele geçirildi haberi çıktı; iş akışınız onu `@v4` etiketiyle kullanıyor. Sürpriz: o iş akışının eriştiği sırlardan biri npm yayın token'ı.
5. **Ajan üretimde:** Ajan bir migration'ı yanlış ortamda çalıştırdı; tablo gitti. Sürpriz: son yedek hiç geri yüklenerek denenmemiş.

## Tatbikatın başarılı sayılması için

- Her katılımcı, olay anında ilk 3 adımını kâğıda bakmadan söyleyebilmeli.
- Kurtarma kodlarının ve iletişim listesinin **nerede** olduğu 1 dakikada bulunabilmeli.
- En az üç somut eylem çıkmalı. Hiç eylem çıkmadıysa senaryo kolaydı; bir sonrakini zorlaştırın.

## Tatbikat sonrası kayıt

| Tarih | Senaryo | Katılımcılar | Bulunan boşluklar | Eylemler (sahip, tarih) |
|---|---|---|---|---|
| | | | | |
