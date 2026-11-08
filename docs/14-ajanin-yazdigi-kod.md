# 14. Ajanın yazdığı kodun güvenliği

[← İçindekiler](../README.md) · Kontrol listesi: [kontrol-listeleri/ajan-kodu-inceleme.md](../kontrol-listeleri/ajan-kodu-inceleme.md)

Buraya kadar ajanın **çalıştığı ortamı** korumayı anlattık. Bu bölüm ajanın **ürettiği şeyi** ele alır: ajanın yazdığı kod, önerdiği bağımlılık ve açtığı PR. Vakamızda saldırgan ajana kod yazdırdı; ama saldırgan olmadan da ajanın kodu güvenlik açığı taşıyabilir ve bu çok daha sık olur.

---

## 14.1 Sayılar

- **Güvensiz varsayılanlar:** Veracode'un 2025 raporu, 100'den fazla modeli 80 görevde test etti; modeller güvenli ve güvensiz yazım arasında seçim yapabildiğinde **%45** oranında güvensiz olanı seçti. Siteler arası betik çalıştırmaya (XSS) karşı koruma %86, günlük enjeksiyonuna karşı koruma %88 oranında başarısızdı. Rapor, bunun model büyüdükçe düzelmediğini de not eder.
- **Uydurma paketler:** USENIX Security 2025'teki çalışma (Spracklen ve ark.), 16 modelden 576.000 kod örneği üretti; önerilen paket referanslarının **%19,7'si** hiçbir kayıt defterinde yoktu (205.474 benzersiz uydurma ad). Daha kötüsü, bu adlar rastgele değil: aynı istem on kez tekrarlandığında uydurma adların %43'ü her seferinde yeniden çıktı. Temmuz 2026'da daha yeni modellerle yapılan bağımsız bir tekrar (arXiv ön baskısı; özet: [secure.com, 24 Temmuz 2026](https://www.secure.com/news/ai-coding-tools-invent-same-fake-packages)), beş farklı modelin aynı 127 sahte adı ürettiğini buldu.

İkinci bulgu bir saldırı türüne dönüştü: **slopsquatting** (terim: Seth Larson, Python Software Foundation, Nisan 2025). Saldırgan, modellerin tutarlı biçimde uydurduğu adları npm ya da PyPI'de önceden kaydeder ve içine zararlı kod koyar. Ocak 2026'da `react-codeshift` adlı uydurma bir paket, ajan "skill" dosyaları yoluyla 237 depoya yayıldı (CSA araştırma notu, kaynaklarda). Ajan bağımlılığı **kendi başına** kuruyorsa, insanın "bu paket gerçek mi?" diye bakacağı an ortadan kalkar.

## 14.2 Beş kural

1. **Ajanın önerdiği her yeni bağımlılığı siz doğrulayın.** Paket adını kayıt defterinde arayın; yayıncıya, indirme sayısına, ilk yayın tarihine ve depo bağlantısına bakın. Birkaç haftalık, tek bakımcılı, deposuz bir paket uyarı işaretidir. Bu adımı ajana bırakmayın; ajan "paket var" derken de uyduruyor olabilir. [Bölüm 6.5](06-tedarik-zinciri.md#65-ajanın-bağımlılık-eklemesine-kural-koyun)'teki `CLAUDE.md` kuralı ve `npm install` için `ask` kuralı bunun içindir.
2. **Güvenlik gereksinimini isteme yazın.** Ajan, söylenmezse güvenli yolu seçmek zorunda hissetmez. "Kullanıcı girdisini parametreli sorguyla işle", "çıktıyı HTML'e yazarken kaçış uygula", "dosya yolunu proje köküyle sınırla" gibi somut cümleler, sonucu ölçülebilir biçimde değiştirir. Projenin `CLAUDE.md` dosyasına kalıcı güvenlik kuralları koyun ([örnek](../ornekler/CLAUDE.md.ornek)).
3. **Ajanın kodu, dışarıdan gelen PR gibi incelenir.** Yazan "kendi aracınız" diye güven artmaz. Özellikle: girdi doğrulama, kimlik doğrulama ve yetki kontrolleri, SQL/komut/HTML enjeksiyonu, dosya yolu birleştirme, hata mesajlarında sızan bilgi, "geçici" olarak kapatılmış bir kontrol (`verify=False`, `// TODO: remove`, `--no-verify`).
4. **Statik analiz ve bağımlılık taraması CI'da zorunlu olsun.** Veracode'un testinde modellerin %86'sı XSS korumasını atladı; bu tür hataları insan incelemesi de her zaman yakalamaz, araç yakalar. Dil için bir SAST (ör. CodeQL, Semgrep), bağımlılıklar için SCA (ör. `npm audit`, Dependabot uyarıları, `pip-audit`), sırlar için bir tarayıcı (ör. gitleaks). Ajanın PR'ı bu kontrolleri geçmeden birleşmez.
5. **Testleri de inceleyin.** Ajan, geçmeyen testi "düzeltmek" için testi gevşetebilir ya da silebilir. PR'da silinen ya da `skip` edilen test, kodun kendisi kadar dikkat ister. [Güvenlik kapısı hook'u](../ornekler/hooks/guvenlik_kapisi.py) `git commit --no-verify` ve `git push --no-verify` ile pre-commit/pre-push kontrollerinin atlanmasını engeller.

## 14.3 Ajanın sık yaptığı güvenlik hataları

| Hata | Nerede görülür | Ne sormalı |
|---|---|---|
| Dize birleştirerek SQL / kabuk komutu | Veritabanı sorguları, `subprocess`, `exec` | Parametreli mi? Kullanıcı girdisi komuta nasıl giriyor? |
| HTML'e kaçışsız yazma | Şablonlar, `innerHTML`, e-posta gövdeleri | Çerçevenin otomatik kaçışı devre dışı mı? |
| Günlüğe ham kullanıcı girdisi | `logger.info(f"...{user_input}")` | Satır sonu ve kontrol karakterleri temizleniyor mu? |
| Sertifika doğrulamayı kapatma | `verify=False`, `rejectUnauthorized: false`, `-k` | "Testte çalışsın diye" kapatıldıysa üretime gidiyor mu? |
| Geniş CORS, açık yönetici uç noktası | `Access-Control-Allow-Origin: *`, `/admin` kimliksiz | Kim erişebilir? |
| Sırrı koda gömme | "Örnek" anahtar, test token'ı | Gerçek mi? Gerçekse [S1](08-senaryolar.md#s1-ajan-bir-sırrı-commitledi-ve-push-etti). |
| Zayıf rastgelelik ve eski kriptografi | `random` ile token, MD5/SHA-1 ile parola | Kriptografik rastgelelik ve güncel algoritma kullanılıyor mu? |
| Geçici dosya ve yol birleştirme | `/tmp/` + kullanıcı adı, `os.path.join(root, user_path)` | `..` ile kökten çıkılabiliyor mu? |
| Uydurma ya da yanlış paket | `import`, `package.json`, `requirements.txt` | Paket gerçekten var mı, doğru paket mi? |

## 14.4 Ajan ile ajanı denetlemek

Ajana kendi kodunu "güvenlik gözüyle incele" demek işe yarar ama yeterli değildir: aynı model aynı kör noktalara sahiptir. İşe yarayan düzen: üretimi yapan oturumdan **ayrı** bir oturumda, yalnız inceleme görevi verilmiş bir ajan (farklı sistem istemi, tercihen salt okunur izinler) PR'ı okur ve yukarıdaki tabloyu sorar. Sonra statik analiz, sonra insan. Üçü birden olduğunda ajanla yazılan kod, insanla yazılan koddan daha az değil, daha çok incelenmiş olur.

---

**Kaynaklar:** Veracode, 2025 GenAI Code Security Report (https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/); Spracklen ve ark., "We Have a Package for You!", USENIX Security 2025; Cloud Security Alliance, Slopsquatting araştırma notu (Nisan–Mayıs 2026, https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419/).
