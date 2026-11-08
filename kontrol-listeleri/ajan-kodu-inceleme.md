# Ajanın yazdığı kodu inceleme listesi

Ajanın açtığı her PR için. Ayrıntılar: [Bölüm 14](../docs/14-ajanin-yazdigi-kod.md). "Kendi aracımız yazdı" güven sebebi değildir; dışarıdan gelen PR gibi okuyun.

**PR:** __________ **İnceleyen:** __________ **Tarih:** __________

## Bağımlılıklar
- [ ] Yeni eklenen her paket kayıt defterinde elle arandı; yayıncı, yaş, indirme sayısı ve depo bağlantısı makul.
- [ ] Paket adı, var olan ve doğru paket (benzer adlı başka bir paket değil).
- [ ] Sürüm sabitlenmiş; kilit dosyası değişikliği okundu.
- [ ] Kurulum betiği olan paket varsa gerekçesi var.

## Kod
- [ ] Kullanıcı girdisi SQL, kabuk komutu, HTML, dosya yolu ya da günlüğe **doğrudan** girmiyor.
- [ ] Kimlik doğrulama ve yetki kontrolü, yeni uç noktaların her birinde var.
- [ ] Sertifika doğrulama, CSRF koruması, CORS gibi kontroller kapatılmamış ("geçici" olanlar dahil).
- [ ] Koda gömülü anahtar, şifre, token yok.
- [ ] Rastgelelik ve kriptografi için uygun kütüphane kullanılmış.
- [ ] Hata mesajları iç bilgi (yol, sorgu, yığın izi) sızdırmıyor.

## Testler ve CI
- [ ] Silinen ya da `skip` edilen test yok; varsa gerekçesi PR açıklamasında.
- [ ] Statik analiz, bağımlılık taraması ve sır taraması geçti.
- [ ] `.github/workflows/`, `CLAUDE.md`, `.claude/`, `.mcp.json`, `devcontainer.json` değişmediyse iyi; değiştiyse ayrıca incelendi ([Bölüm 4.6](../docs/04-claude-code-sertlestirme.md#46-yabancı-bir-depoyu-açmadan-önce)).

## Kapsam
- [ ] PR yalnız istenen değişikliği içeriyor; ilgisiz dosyaya dokunulmamış.
- [ ] Ajanın açıklaması ile diff örtüşüyor.
