# Değişiklikler

## 2.1 — 7 Kasım 2026 (akşam, iyileştirme döngüsü)

On turluk araştırma–doğrulama döngüsü; ayrıntılar [DONGU-LOG.md](DONGU-LOG.md).

- Yeni: çekirdek kurallar (Bölüm 0), hesap ve oturum güvenliği (Bölüm 9), platform başvuru kartı (Bölüm 10), 12 senaryo (Bölüm 8), standart eşlemesi (OWASP Agentic/LLM/MCP Top 10, NIST CSF 2.0 ve SP 800-61r3, CIS IG1).
- Yeni malzeme: çalışan PreToolUse güvenlik kapısı hook'u, sertleştirilmiş GitHub Actions ve Dependabot örnekleri, delil zinciri kaydı, masa başı tatbikat şablonu, beş ölçüt.
- Düzeltmeler (birincil kaynaklarla): sandbox okumayı varsayılan olarak kısıtlamaz ve `allow` kuralı sandbox dışı yeniden denemeyi onaylar; `Read` yasak kurallarının gerçek kapsamı; `Write(...)` kuralının yok sayılması; npm 12'nin çıkmış olması ve `approve-scripts`; tüm oturumlardan çıkışın yalnız web'de olması; KVKK 72 saat kuralının kaynağı.
- Olaydaki eklenti adlandırıldı: Alpme v1.0.25 (bağımsız raporlara dayanarak), kontrol yöntemiyle.

## 2. sürüm — 7 Kasım 2026

### Yapı
- Tek README, bölümlere ayrıldı (`docs/`). README artık içindekiler, hızlı müdahale özeti ve olaydan çıkan dersleri içeriyor.
- Yazdırılabilir kontrol listeleri (`kontrol-listeleri/`), doldurulabilir şablonlar (`sablonlar/`) ve örnek ayar dosyaları (`ornekler/`) eklendi.
- Sözlük, katkı rehberi ve güvenlik politikası eklendi.

### Yeni bölümler
- **4. Claude Code'u sertleştirme:** ayar dosyaları ve öncelik, yasak kurallarının sınırı, izinler, atlama kipini kapatma, sandbox, yabancı depoları açmadan önce bakılacak dosyalar, hook'lar, oturum geçmişi.
- **5. İstem enjeksiyonu ve MCP:** tehlikeli üçlü, pratik savunmalar, MCP sunucusu ekleme kontrol listesi, MCP izin kuralları.
- **6. Tedarik zinciri:** npm `.npmrc` sertleştirmesi, pnpm/Yarn/Bun/pip karşılıkları, VS Code `extensions.allowed` izin listesi.
- **7. Ekip politikası:** beş kural, roller, GitHub kuruluş ayarları, işe giriş ve ayrılış listeleri.

### Mevcut bölümlerde
- **1. Kurmadan önce:** Open VSX uyarısı, beklenmedik sürüm uyarısı, VSIX'i kurmadan inceleme komutları (Windows/macOS/Linux), platforma göre hash komutları, ayar eşitlemesi uyarısı, macOS/Linux açılış öğeleri.
- **2. Olay anında:** Claude'a özgü adımlar (etkin oturumlar, Claude Code yetkileri ayrı), e-posta yönlendirme kuralları, GitHub güvenlik günlüğü ve Actions, diğer sırlar, KVKK notu, yedekte `.claude` ve kabuk başlangıç dosyaları, bir hafta sonra geriye bakış.
- **3. Adli inceleme:** ele geçirilmiş bilgisayarda ajan çalıştırmanın üç riski (yeni kimlik sızması, ağın açık kalması, istem enjeksiyonu) ve daha temkinli seçenek; "ağı kes" ile "Claude ile incele" arasındaki çelişki giderildi; İstem 1 için macOS ve Linux sürümleri; hash doğrulama komutları.
- Kaynaklara Claude oturum yönetimi destek makaleleri, Claude Code ve VS Code kurumsal belgeleri eklendi.

### Değişmeyenler
- Olay anlatımı ve üç istemin metni aynen korundu.

## 1. sürüm — 6 Kasım 2026

- İlk yayın: kurmadan önce kontroller, olay anında, Claude ile adli inceleme.
