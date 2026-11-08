# Olay anı kontrol listesi

Ayrıntılar: [Bölüm 2](../docs/02-olay-aninda.md). Her adımı yaptığınız saati [olay kaydına](../sablonlar/olay-kaydi.md) yazın.

**Olay yöneticisi:** __________ **Kayıt tutan:** __________ **Başlangıç saati:** __________

**Seviye:** ☐ Kırmızı ☐ Sarı ☐ Yeşil ([nasıl karar verilir](../docs/02-olay-aninda.md)) — emin değilseniz bir üst seviye.

## İlk 15 dakika: durdur ve koru
- [ ] Hiçbir şey silinmedi (oturum, depo, dosya, eklenti).
- [ ] Ekranda açık olan her şey (ajan oturumu, terminal, güvenlik uyarısı) **telefonla** fotoğraflandı; yeni sayfa açılmadı, giriş yapılmadı.
- [ ] Ajan oturumu durduruldu; arşivlenmedi, o oturumla konuşulmadı.
- [ ] Bilgisayar ele geçirilmiş sayıldı: üzerinde şifre yazılmıyor, yeni oturum açılmıyor.
- [ ] Bilgisayar kapatılmadı, uykuya alınmadı; **ağ bağlantısı kesildi** (kablo, Wi-Fi, VPN).
- [ ] Bir yönetici ve bir kayıt tutan belirlendi.

## İlk saat: temiz cihazdan, bu sırayla
- [ ] **E-posta:** şifre, iki adımlı doğrulama, tüm cihazlardan çıkış, üçüncü taraf erişimleri, yönlendirme kuralları ve filtreler.
- [ ] **Yapay zekâ hesabı:** etkin oturumlar, bağlı uygulamalar ve kullanım ekranı **fotoğraflandı** → tanınmayanlar sonlandırıldı → tüm cihazlardan çıkış.
- [ ] **Claude Code yetkileri** ayrıca kontrol edildi ve tanınmayanlar silindi.
- [ ] Bağlı GitHub hesabı ve bağlayıcılar kontrol edildi.
- [ ] **API anahtarları:** o bilgisayardaki her anahtar iptal edildi ve yenilendi.
- [ ] **GitHub:** oturumlar, token'lar (classic + fine-grained), SSH/GPG anahtarları, OAuth uygulamaları, deploy anahtarları.
- [ ] **Günlükler dışa aktarıldı** (GitHub güvenlik/audit günlüğü, sağlayıcı kullanım kayıtları); hash'leri [delil zinciri kaydına](../sablonlar/delil-zinciri.md) yazıldı.
- [ ] **Diğer sırlar:** bulut, veritabanı, ödeme, npm/PyPI token'ları, MCP token'ları, tarayıcıdaki kayıtlı şifreler.
- [ ] **Ekip erişimi:** kişi geçici olarak kuruluş depolarından çıkarıldı; son commit, push, PR ve CI çalıştırmaları kontrol edildi.
- [ ] Ele geçirilmiş bilgisayarın ağı hâlâ kesik.

## İlk gün
- [ ] Olay yalnız bilmesi gerekenlerle, ele geçirilmemiş bir kanaldan konuşuluyor.
- [ ] Salt okunur adli inceleme yapıldı ([Bölüm 3](../docs/03-claude-ile-adli-inceleme.md)); delil paketi ve `ozetler.txt` hazır.
- [ ] Kök neden yazılı hâle getirildi (kanıtıyla).
- [ ] Sağlayıcıya, GitHub'a ve pazar yerine bildirim yapıldı ([şablon](../sablonlar/olay-bildirimi.md)).
- [ ] Kişisel veri etkilendiyse hukuki danışmanlık alındı (KVKK).
- [ ] Tam format: temiz bilgisayarda hazırlanan kurulum belleği, tüm bölümler silindi.
- [ ] Yedekten yalnız belge ve kaynak kod döndü; kod mümkünse uzak depodan klonlandı.
- [ ] Settings Sync açılmadan önce bulut tarafındaki eklenti listesi kontrol edildi.

## Bir hafta sonra
- [ ] Suçlu aramayan geriye bakış toplantısı yapıldı; eylemlerin sahibi ve tarihi var.
