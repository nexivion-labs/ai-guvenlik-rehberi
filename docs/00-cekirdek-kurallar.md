# Çekirdek kurallar

[← İçindekiler](../README.md)

Rehberin geri kalanı bu on kuralın ayrıntısıdır. Hiçbir şey okumaya vaktiniz yoksa bunları uygulayın. Her kuralın yanında hangi bölümde açıklandığı ve hangi standarda karşılık geldiği yazıyor ([standart eşlemesi](standart-eslemesi.md)).

| # | Kural | Ayrıntı | Karşılık |
|---|---|---|---|
| 1 | **Ajan, çalıştığı bilgisayardan daha güvenli olamaz.** Ajana verdiğiniz her yetki, o bilgisayara giren her programın da yetkisidir. | [Bölüm 4.1](04-claude-code-sertlestirme.md) | ASI03, CSF PR.PS |
| 2 | **Resmî kaynak dışından hiçbir şey kurulmaz; kurulan her şey önce okunur.** | [Bölüm 1](01-kurmadan-once.md) | ASI04, CSF GV.SC |
| 3 | **Sır, ajanın görebileceği yerde durmaz.** Anahtar zinciri ya da sır yöneticisi; kapsamı dar, süresi kısa anahtar. | [Bölüm 4.3](04-claude-code-sertlestirme.md#43-sırlara-erişimi-kapatın) | ASI03, CSF PR.AA |
| 4 | **Ajanın okuduğu her dış içerik bir talimat olabilir.** Dış içerik, sır ve dışarı veri gönderme aynı görevde bir araya gelmez. | [Bölüm 5](05-istem-enjeksiyonu-ve-mcp.md) | ASI01, LLM01 |
| 5 | **Geri alınamayan her işlem bir insanın onayından geçer.** Push, yayın, silme, para harcama, dışarı veri gönderme. | [Bölüm 4.4](04-claude-code-sertlestirme.md#44-izinleri-bilinçli-verin) | ASI02, ASI09 |
| 6 | **Kural yetmez, sınır gerekir.** İzin kurallarının yanında sandbox, konteyner ya da ayrı kullanıcı. | [Bölüm 4.5](04-claude-code-sertlestirme.md#45-sandboxı-açın) | ASI05, CSF PR.IR |
| 7 | **Uyarıya bakan biri olmazsa uyarı yoktur.** Güvenlik aracının geçmişi düzenli ve sahibi belli biri tarafından okunur. | [Bölüm 7](07-ekip-politikasi.md) | CSF DE.CM, GV.RR |
| 8 | **Olayda sıra: durdur ve koru → temiz cihazdan kapat → incele → temizle.** Önce silmek, izi siler. | [Bölüm 2](02-olay-aninda.md) | NIST SP 800-61r3, CSF RS |
| 9 | **E-posta, bütün hesapların anahtarıdır; iki adımlı doğrulama oturumu korumaz.** E-posta ilk korunur, olayda ilk kapatılır; oturumlar kısa ömürlü tutulur. | [Bölüm 9](09-hesap-ve-oturum-guvenligi.md), [Bölüm 2](02-olay-aninda.md) | ASI03, CSF PR.AA |
| 10 | **Ajanın söylediği bir hipotezdir.** Ajan raporunu, kodunu, önerdiği paketi ve PR'ını kanıta karşı doğrulayın; ajanın kodu dışarıdan gelen PR gibi incelenir. | [Bölüm 14](14-ajanin-yazdigi-kod.md), [Bölüm 3](03-claude-ile-adli-inceleme.md) | ASI09, LLM05 |

Kodlar: **ASI** = OWASP Top 10 for Agentic Applications (2026), **LLM** = OWASP Top 10 for LLM Applications (2025), **CSF** = NIST Cybersecurity Framework 2.0 (GV Yönet, ID Tanımla, PR Koru, DE Tespit, RS Müdahale, RC Kurtar).
