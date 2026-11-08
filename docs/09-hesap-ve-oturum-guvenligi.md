# 9. Hesap, kimlik ve oturum güvenliği

[← İçindekiler](../README.md)

Vakamızda saldırgan şifreye ihtiyaç duymadı; en olası açıklama oturum bilgisinin bilgisayardan alınmasıdır. Ağustos 2026'da Anthropic da bazı Claude kullanıcılarını aynı yöntemle ilgili e-postayla uyardı (etkilenen bir kullanıcının paylaştığı metinde: "yaygın bilgi hırsızı zararlılarla insanların bilgisayarlarından Claude oturumlarını çalan bir kötü niyetli aktör"). İlk belirti çoğu zaman şuydu: kullanım limiti siz kullanmazken doluyor. Anthropic'in müdahalesi çalınan oturumları geçersiz kılmaktan ibaretti; **bilgisayardaki zararlı yazılım yerinde kalıyordu**, yani kullanıcı temizlemeden yeniden giriş yaparsa yeni oturum da çalınabilirdi. Olayda etkilenen bir kullanıcı, enfeksiyonu korsan bir oyun indirmesine bağlamıştı. Anthropic'in uyarısı: kullanıcıların bilgisayarındaki yaygın bilgi hırsızı (infostealer) zararlılar, tarayıcıdaki **açık Claude oturumlarını** kopyalamış, saldırganlar bu oturumlarla hesaplara girip kullanım hakkını tüketmişti. Uyarıda Windows'ta Vidar, LummaC2, StealC, RedLine ve Acreed, birkaç Mac'te de Atomic Stealer (AMOS) adları geçiyordu.

Bu bölümün ana fikri: **iki adımlı doğrulama girişi korur, girişten sonra oluşan oturumu korumaz.** Oturumu korumanın yolu, oturumun bulunduğu bilgisayarı korumak ve oturumları kısa ömürlü tutmaktır.

---

## 9.1 Hesapların bağımlılık sırası

Bir hesabı korumadan önce, onun "kurtarma kapısının" hangi hesap olduğunu bilin. Tipik bir geliştiricide zincir şöyledir:

```text
Telefon (SIM, doğrulama uygulaması)
  └─ E-posta / Google hesabı
       ├─ Claude hesabı (giriş e-posta bağlantısı ya da Google ile; ayrı bir şifre yok)
       ├─ GitHub
       ├─ Bulut sağlayıcıları, alan adı, ödeme
       └─ Parola yöneticisi (kurtarma)
```

Zincirin en üstü zayıfsa alttaki her şey zayıftır. Claude'da şifre olmadığı için **Claude hesabınızın güvenliği, e-posta ya da Google hesabınızın güvenliğine eşittir.** Koruma ve olay anında kapatma sırası bu yüzden yukarıdan aşağıdır.

## 9.2 İkinci adım yöntemleri: güçlüden zayıfa

| Yöntem | Oltalamaya dayanıklı mı? | Not |
|---|---|---|
| Passkey ya da donanım güvenlik anahtarı (YubiKey vb.) | Evet | En güçlüsü. En az iki tane kaydedin (biri yedek). |
| Doğrulama uygulaması (TOTP) | Hayır | Sahte bir giriş sayfasına kod girilebilir. Kabul edilebilir asgari düzey. |
| Uygulama bildirimi ("Evet, bendim") | Kısmen | Art arda gelen onay isteklerini asla onaylamayın. |
| SMS | Hayır | SIM kopyalama ve yönlendirmeye açık. Başka seçenek varsa kullanmayın. |

**Kurtarma kodları:** İki adımlı doğrulamayı açtığınız her hesapta kurtarma kodlarını indirin ve **o bilgisayardan bağımsız** bir yerde saklayın (parola yöneticisi ya da basılı kopya). Ele geçirilmiş bilgisayarda duran kurtarma kodu, saldırganın kodudur.

## 9.3 Oturumları korumak

- **Ayrı tarayıcı profili:** İş hesaplarını (GitHub kuruluşu, yapay zekâ ekip hesabı, bulut konsolu) eklenti yüklü olmayan ayrı bir tarayıcı profilinde açın. Bilgi hırsızları ve zararlı tarayıcı eklentileri genellikle bütün profilleri tarar, ama eklentisiz bir profil saldırı yüzeyini daraltır.
- **Kullanmadığınızda çıkış yapın:** Hassas konsollarda (bulut, ödeme, alan adı) işiniz bitince oturumu kapatın. Açık oturum, çalınabilecek oturumdur.
- **Etkin oturumlara ayda bir bakın:** Claude'da Ayarlar → Hesap → Etkin oturumlar; GitHub'da Ayarlar → Oturumlar; Google'da Güvenlik → Cihazlarınız. Tanımadığınızı sonlandırın.
- **Kullanım uyarıları:** Yapay zekâ ve bulut hesaplarında harcama limiti ve kullanım uyarısı tanımlayın. Vakaların çoğunda ilk belirti beklenmedik kullanımdır.
- **Tarayıcıya şifre kaydetmeyin:** Bilgi hırsızlarının ilk hedefi tarayıcıda kayıtlı şifrelerdir. Bir parola yöneticisi kullanın ve ana şifresini bilgisayarda düz metin olarak tutmayın.

## 9.4 API anahtarları

- Her proje ve her ortam (geliştirme, üretim) için ayrı anahtar. Bir anahtar sızdığında yalnız o iptal edilir.
- Sağlayıcı izin veriyorsa anahtar başına harcama limiti ve kapsam (yalnız gereken yetki) tanımlayın.
- Anahtarı hiçbir zaman sohbet geçmişine, issue'ya, ekran görüntüsüne ya da ekran paylaşımına koymayın.
- Kullanılmayan anahtarları ayda bir iptal edin ([aylık kontrol](../kontrol-listeleri/aylik-kontrol.md)).
- Kullanıcı oturumunu kapatmak API anahtarlarını iptal etmez; ikisi ayrı ayrı yönetilir.

## 9.5 Hesap ele geçirildi mi? Belirtiler

- Tanımadığınız oturum, konum ya da cihaz.
- Sizin kullanmadığınız saatlerde kullanım artışı ya da limitin beklenmedik şekilde dolması.
- Sizin yazmadığınız sohbetler, projeler ya da Claude Code oturumları.
- Sağlayıcıdan gelen güvenlik e-postası ya da zorunlu çıkış.
- E-postanızda sizin oluşturmadığınız filtre ya da yönlendirme kuralı.

Bunlardan biri varsa: [Olay anında](02-olay-aninda.md).

## 9.6 Senaryolar

Bu bölümle ilgili senaryolar: [S3: Bilgi hırsızı oturumları çaldı](08-senaryolar.md#s3-bilgi-hırsızı-tarayıcı-oturumlarını-çaldı), [S4: İki adımlı doğrulamanın bağlı olduğu telefon kayboldu](08-senaryolar.md#s4-iki-adımlı-doğrulamanın-bağlı-olduğu-telefon-kayboldu), [S13: Dizüstü bilgisayar kayboldu](08-senaryolar.md#s13-dizüstü-bilgisayar-kayboldu-ya-da-çalındı).

---

**Kaynak:** Anthropic'in Ağustos 2026 oturum hırsızlığı uyarısı (BleepingComputer, 30 Ağustos 2026: https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/); GitHub, iki adımlı doğrulama kurtarma kodları: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods
