# Standart eşlemesi

[← İçindekiler](../README.md) · [Çekirdek kurallar](00-cekirdek-kurallar.md)

Bu rehber bir standart değildir; ama önerileri, sektörde kabul görmüş çerçevelerle uyumlu olacak şekilde yazıldı. Bu sayfa, ekip içinde ya da bir denetimde "bu öneri nereden geliyor?" sorusuna cevap vermek için.

## OWASP Top 10 for Agentic Applications (2026)

OWASP GenAI Security Project tarafından 9 Aralık 2025'te yayımlandı. Otonom ajanlara özgü on risk sınıfını tanımlar.

| Kod | Risk | Rehberde nerede |
|---|---|---|
| ASI01 | Ajan hedefinin ele geçirilmesi (okunan içerik yoluyla yönlendirme) | [Bölüm 5](05-istem-enjeksiyonu-ve-mcp.md) |
| ASI02 | Araçların kötüye kullanımı | [Bölüm 4.4](04-claude-code-sertlestirme.md), [Bölüm 5.4](05-istem-enjeksiyonu-ve-mcp.md#54-mcp-sunucuları) |
| ASI03 | Kimlik ve yetki istismarı | [Bölüm 9](09-hesap-ve-oturum-guvenligi.md), [Bölüm 2](02-olay-aninda.md), [Bölüm 4.1–4.3](04-claude-code-sertlestirme.md) |
| ASI04 | Tedarik zinciri (eklenti, paket, MCP sunucusu, uydurma paket) | [Bölüm 1](01-kurmadan-once.md), [Bölüm 6](06-tedarik-zinciri.md), [Bölüm 14](14-ajanin-yazdigi-kod.md) |
| ASI05 | Beklenmeyen kod çalıştırma | [Bölüm 4.5](04-claude-code-sertlestirme.md), [Bölüm 4.6](04-claude-code-sertlestirme.md) |
| ASI06 | Bellek ve bağlam zehirlenmesi | [Bölüm 5.3](05-istem-enjeksiyonu-ve-mcp.md#53-kalıcı-zehirlenme-ajanın-belleği), [Bölüm 4.6](04-claude-code-sertlestirme.md) |
| ASI07 | Ajanlar arası güvensiz iletişim | Kapsam dışı (çoklu ajan sistemleri kuranlar için ayrı rehber gerekir) |
| ASI08 | Zincirleme hatalar | [Bölüm 4.4](04-claude-code-sertlestirme.md) (geri alınamayan işlemlere onay) |
| ASI09 | İnsan–ajan güveninin istismarı | [Çekirdek kural 10](00-cekirdek-kurallar.md), [Bölüm 3.6](03-claude-ile-adli-inceleme.md) |
| ASI10 | Denetimden çıkmış ajan | [Bölüm 2](02-olay-aninda.md) (ajan oturumunu durdurma), [Bölüm 7](07-ekip-politikasi.md) |

## OWASP Top 10 for LLM Applications (2025)

| Kod | Risk | Rehberde nerede |
|---|---|---|
| LLM01 | İstem enjeksiyonu | [Bölüm 5](05-istem-enjeksiyonu-ve-mcp.md) |
| LLM02 | Hassas bilgi ifşası | [Bölüm 13](13-veri-nereye-gidiyor.md), [Bölüm 4.3](04-claude-code-sertlestirme.md), [Bölüm 4.8](04-claude-code-sertlestirme.md) |
| LLM03 | Tedarik zinciri | [Bölüm 6](06-tedarik-zinciri.md) |
| LLM05 | Çıktının güvensiz işlenmesi | [Bölüm 14](14-ajanin-yazdigi-kod.md), [Bölüm 5.2](05-istem-enjeksiyonu-ve-mcp.md) |
| LLM06 | Aşırı yetki (excessive agency) | [Bölüm 4.4](04-claude-code-sertlestirme.md) |

## OWASP MCP Top 10 (beta)

OWASP'ın MCP'ye özgü risk listesi Kasım 2026 itibarıyla beta aşamasındadır; kodlar değişebilir.

| Kod | Risk | Rehberde nerede |
|---|---|---|
| MCP03 | Araç zehirlenmesi (açıklama zehirlenmesi, gölgeleme, sonradan değişme) | [Bölüm 5.4](05-istem-enjeksiyonu-ve-mcp.md#54-mcp-sunucuları) |
| — | Token yönetimi ve sır ifşası | [Bölüm 5.4](05-istem-enjeksiyonu-ve-mcp.md#54-mcp-sunucuları) (token kapsamı, düz metin yapılandırma) |
| — | Aşırı yetki | [Bölüm 5.4](05-istem-enjeksiyonu-ve-mcp.md#54-mcp-sunucuları) (MCP izin kuralları) |

## NIST Cybersecurity Framework 2.0 ve SP 800-61 Rev. 3

NIST SP 800-61 Rev. 3 (Nisan 2025), olay müdahalesini CSF 2.0'ın altı işleviyle ilişkilendirir. Olay müdahalesi yalnız "Müdahale" adımı değildir; hazırlık (Yönet, Tanımla, Koru) olmadan iyi müdahale olmaz.

| CSF 2.0 işlevi | Ne demek | Rehberde nerede |
|---|---|---|
| **GV** Yönet | Politika, roller, sorumluluk | [Bölüm 7](07-ekip-politikasi.md) |
| **ID** Tanımla | Varlık ve tedarikçi envanteri, risk | [Onaylı araçlar](../sablonlar/onayli-araclar.md), [Bölüm 1](01-kurmadan-once.md) |
| **PR** Koru | Kimlik, erişim, platform güvenliği | [Bölüm 9](09-hesap-ve-oturum-guvenligi.md), [Bölüm 4](04-claude-code-sertlestirme.md), [Bölüm 6](06-tedarik-zinciri.md) |
| **DE** Tespit | Sürekli izleme, olay analizi | [Bölüm 1.6](01-kurmadan-once.md), [Aylık kontrol](../kontrol-listeleri/aylik-kontrol.md) |
| **RS** Müdahale | Olay yönetimi, analiz, bildirim, sınırlama | [Bölüm 2](02-olay-aninda.md), [Bölüm 3](03-claude-ile-adli-inceleme.md), [Bildirim şablonu](../sablonlar/olay-bildirimi.md) |
| **RC** Kurtar | Kurtarma planı, iletişim | [Bölüm 11](11-yedekleme-ve-kurtarma.md), [Bölüm 2, ilk gün ve bir hafta sonra](02-olay-aninda.md) |

## CIS Kritik Güvenlik Kontrolleri (v8), Uygulama Grubu 1

CIS Kontrolleri'nin IG1 seviyesi, küçük kuruluşlar için "temel siber hijyen" olarak tanımlanır. Rehberin kapsadığı başlıca korumalar:

| CIS kontrolü | Rehberde nerede |
|---|---|
| 1–2 Varlık ve yazılım envanteri | [Onaylı araçlar](../sablonlar/onayli-araclar.md) |
| 3 Veri koruma | [S11](08-senaryolar.md), [Bölüm 4.3](04-claude-code-sertlestirme.md) |
| 4 Güvenli yapılandırma | [Bölüm 4](04-claude-code-sertlestirme.md), [Bölüm 6](06-tedarik-zinciri.md) |
| 5–6 Hesap ve erişim yönetimi | [Bölüm 9](09-hesap-ve-oturum-guvenligi.md), [Bölüm 7.7](07-ekip-politikasi.md) |
| 11 Veri kurtarma | [Bölüm 11](11-yedekleme-ve-kurtarma.md) |
| 10 Zararlı yazılım savunması | [Bölüm 1.6](01-kurmadan-once.md), [Bölüm 10](10-platform-basvuru-karti.md) |
| 16 Uygulama yazılımı güvenliği | [Bölüm 14](14-ajanin-yazdigi-kod.md) |
| 14 Güvenlik farkındalığı | Bu rehberin kendisi, [Bölüm 7.6](07-ekip-politikasi.md) |
| 17 Olay müdahalesi (17.7 tatbikat) | [Bölüm 2](02-olay-aninda.md), [Tatbikat şablonu](../sablonlar/masa-basi-tatbikat.md) |

## Bilinçli olarak kapsam dışı

- Kendi ajan ürününü geliştirenler için uygulama güvenliği (çoklu ajan, bellek mimarisi, model güvenliği).
- Kurumsal EDR/SIEM kurulumu ve profesyonel adli imaj alma.
- Hukuki danışmanlık (KVKK için yalnız yönlendirme yapılır).

## Kaynaklar

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- OWASP MCP Top 10 (beta): https://owasp.org/www-project-mcp-top-10/
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- NIST SP 800-61 Rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- CIS Critical Security Controls: https://www.cisecurity.org/controls/cis-controls-list
