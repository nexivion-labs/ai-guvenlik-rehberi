# Sağlayıcıya olay bildirimi şablonu

Destek ekipleri genelde İngilizce çalışır; aşağıda Türkçe ve İngilizce iki sürüm var. Köşeli parantezleri doldurun. **Şifre, anahtar ya da çerez değeri paylaşmayın**; yalnız kimlikleri, saatleri ve hash'leri yazın.

Bildirimi asıl hesabınızla, **temiz bir cihazdan** gönderin.

---

## Türkçe

**Konu:** Hesap ele geçirme bildirimi – [hesap e-postası] – [tarih]

Merhaba,

[Tarih] tarihinde [saat aralığı, saat dilimiyle] arasında hesabımın yetkim dışında kullanıldığını tespit ettim.

**Özet:** Bilgisayarımdaki zararlı bir [eklenti / yazılım] oturum bilgilerimi ele geçirdi. Saldırgan bu bilgiyle hesabıma giriş yaptı ve [ne yaptı: Claude Code ile kod yazdırdı, API kullanımı, vb.].

**Yaptıklarım:**
- [Saat] tüm oturumlardan çıkış yaptım.
- [Saat] [Claude Code yetkilerini / API anahtarlarını] iptal ettim.
- [Saat] bağlı [GitHub] hesabını ayırdım.

**Kanıtlar:**
- Yetkisiz oturum(lar): [oturum kimliği / cihaz / konum / saat]
- Yetkisiz kullanım: [konuşma ya da oturum kimlikleri, saatler]
- Zararlı dosyanın SHA-256 değeri: [hash]
- Zararlı eklentinin kimliği: [yayıncı.ad, sürüm]
- Ek: delil paketi dosya listesi ve `ozetler.txt` hash'i: [hash]

**Talebim:**
1. Hesabım için güvenlik incelemesi ve sunucu tarafında bütün oturum/token'ların iptal edildiğinin teyidi.
2. Yetkisiz kullanımdan doğan [ücretlerin] incelenmesi.
3. [Varsa] saldırganın erişimiyle ilgili paylaşabileceğiniz bilgi.

Teşekkürler,
[Ad Soyad] · [Kuruluş] · [İletişim]

---

## English

**Subject:** Account compromise report – [account email] – [date]

Hello,

On [date], between [time range, with time zone], my account was used without my authorization.

**Summary:** A malicious [extension / program] on my computer stole my session credentials. The attacker used them to access my account and [what they did: ran Claude Code sessions, API usage, etc.].

**Actions taken:**
- [Time] Logged out of all sessions.
- [Time] Revoked [Claude Code authorizations / API keys].
- [Time] Disconnected the linked [GitHub] account.

**Evidence:**
- Unauthorized session(s): [session ID / device / location / time]
- Unauthorized activity: [conversation or session IDs, times]
- SHA-256 of the malicious file: [hash]
- Malicious extension ID: [publisher.name, version]
- Attached: evidence package file list and SHA-256 of `ozetler.txt`: [hash]

**Requests:**
1. A security review of my account and confirmation that all sessions/tokens have been revoked server-side.
2. Review of [charges] resulting from the unauthorized use.
3. [If applicable] Any information you can share about the attacker's access.

Thank you,
[Name] · [Organization] · [Contact]

---

## Nereye bildirilir?

| Ne | Nereye |
|---|---|
| Claude hesabı | Claude Yardım Merkezi'ndeki destek sohbeti (support.claude.com) |
| GitHub hesabı / kötüye kullanılan depo | GitHub Support ve depo sayfasındaki "Report abuse" |
| VS Code eklentisi | Marketplace'te eklenti sayfasındaki "Report Abuse" |
| Open VSX eklentisi | Open VSX deposundaki bildirim yolu |
| npm paketi | npm'de paket sayfasındaki "Report malware" |
| PyPI paketi | PyPI'de paket sayfasındaki "Report project as malware" |
