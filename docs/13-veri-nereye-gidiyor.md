# 13. Veri nereye gidiyor? Ajanlar, tarayıcı ve gizlilik

[← İçindekiler](../README.md)

Bu rehberin çoğu "saldırgan içeri girmesin" diye yazıldı. Bu bölüm başka bir soruya bakar: **saldırgan olmasa bile, ajan kullanırken verileriniz nereye gidiyor ve bunu nasıl kontrol edersiniz?** Üç konu: ajanın sağlayıcıya gönderdiği veri, diskte bıraktığı iz ve tarayıcıda çalışan ajanlar.

---

## 13.1 Ajan ne gönderir?

Sandbox olsun olmasın, ajanın **okuduğu her dosya ve yazdığınız her istem** sağlayıcının API'sine gider; yalıtım bunu değiştirmez (Anthropic'in kendi belgesi bunu açıkça söyler). Buradan iki kural çıkar:

1. **Ajana göstermek istemediğiniz şeyi proje klasöründe tutmayın.** Yasak kuralları ve sandbox okumayı sınırlar ama kesin sınır, verinin orada olmamasıdır ([çekirdek kural 3](00-cekirdek-kurallar.md)).
2. **Müşteri verisi, kişisel veri, gizlilik sözleşmesi kapsamındaki kod** için hangi hesap türünü kullandığınız önemlidir. Claude Code için kamuya açık belgelere göre:

| Hesap türü | Eğitimde kullanım | Saklama |
|---|---|---|
| Bireysel (Pro/Max), eğitim izni **açık** (Ağustos 2025'ten beri varsayılan soru) | Evet | 5 yıla kadar |
| Bireysel, eğitim izni **kapalı** (claude.ai → Ayarlar → Gizlilik) | Hayır | 30 gün |
| Ticari şartlar (API, Team/Enterprise) | Hayır (ayrıca katılmadıkça) | 30 gün; sıfır veri saklama (ZDR) anlaşmasıyla sunucuda hiç |

Ekip için şirket işi yapıyorsanız bireysel hesap yerine ticari hesap kullanın ve bireysel hesaplarda eğitim iznini kontrol edin. Bu tablo sağlayıcının politikasına bağlıdır ve değişebilir; kaynağı [Claude Code veri kullanımı belgesidir](https://code.claude.com/docs/en/data-usage).

### Gereksiz trafiği kapatın

Claude Code, istem ve cevap dışında da bazı veriler gönderir: kullanım ölçümleri (kod ya da dosya yolu içermez), hata raporları, anketler ve `/bug` ile **tam konuşma geçmişi** (bu komut kodu da gönderir ve kendi saklama süresi vardır; yanlışlıkla çalıştırmayın). Hepsini tek değişkenle kapatabilirsiniz:

```json
{
  "env": {
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
  }
}
```

Yalnız ölçümleri kapatmak için `DISABLE_TELEMETRY=1`, hata raporlarını kapatmak için `DISABLE_ERROR_REPORTING=1`. Bedrock, Vertex ve Foundry üzerinden kullanımda ölçümler varsayılan olarak kapalıdır.

## 13.2 Diskte kalan iz

Claude Code her oturumun tam dökümünü yerel diske yazar (`~/.claude/projects/` altında JSONL dosyaları). Bu dosyalar düz metindir, şifreli değildir ve içinde ajana gösterdiğiniz her şey vardır: sırlar, müşteri verisi, hata mesajlarındaki iç adresler. Bu üç durumda sorun olur:

- **Bilgisayar ele geçirildiğinde.** Bilgi hırsızı tarayıcı çerezleriyle birlikte bu klasörü de alabilir. [Bölüm 4.8](04-claude-code-sertlestirme.md#48-oturum-geçmişi-de-bir-sırdır).
- **Yedekleme ve eşitlemede.** Ev klasörünü bulutla eşitliyorsanız oturum dökümleri de gider.
- **Bilgisayar devredildiğinde.** Eski bilgisayarı birine verirken ya da format atmadan satarken.

Ne yapılır: eşitleme ve yedek dışlama listelerine `~/.claude/projects/` ekleyin; ayda bir eski dökümleri silin; hassas projelerde oturum bitince dökümü elle silin. Üçüncü taraf kaynaklarda dökümlerin hiç yazılmaması için `CLAUDE_CODE_SKIP_PROMPT_HISTORY=1` değişkeni anılıyor, ancak bunu resmî belgede **doğrulayamadık**; kullanmadan önce kendi sürümünüzde deneyin (bir oturum açın, `~/.claude/projects/` altında yeni dosya oluşmadığını kontrol edin). Diğer ajanlar da benzer klasörler tutar (ör. Cursor ve Copilot sohbet geçmişleri); her aracın belgesinden yerini öğrenin.

## 13.3 Ekran paylaşımı ve kayıtlar

Ajanla çalışırken ekran paylaşmak ya da kayıt almak yeni bir sızıntı yoludur: ajanın çıktısında bir anahtar, bir müşteri e-postası ya da iç bir URL görünebilir. Canlı yayın, eğitim videosu ve pair programming oturumlarında:

- Ajanı sırsız bir demo projesinde çalıştırın.
- Terminalde `env`, `printenv`, `.env` içeriği ve `git log -p` gibi komutlardan kaçının (güvenlik kapısı hook'u bunların bir kısmını zaten engeller).
- Kaydı yayımlamadan önce izleyin; bir kez yayımlanan anahtar iptal edilmelidir, karartılması yetmez.

## 13.4 Tarayıcıda çalışan ajanlar

Tarayıcı eklentisi olarak çalışan ajanlar (ör. Claude in Chrome) sayfaları okur, tıklar, form doldurur. Bu, [istem enjeksiyonunun](05-istem-enjeksiyonu-ve-mcp.md) en açık yüzeyidir: ajan, ziyaret ettiği her sayfanın içeriğini okur ve o sayfa saldırgana aitse talimat da okumuş olur. Anthropic, kendi eklentisini duyururken bunu açıkça yazdı: önlemler olmadan yapılan kırmızı takım testlerinde saldırılar başarılı oldu, önlemlerle oran düştü ama sıfırlanmadı. Ocak 2026'da bağımsız araştırmacılar, eklentinin eski bir sürümünde herhangi bir web sayfasının tıklama gerektirmeden ajana istem gönderebildiği bir zincir buldu; Anthropic 1.0.41 sürümünde kapattı.

Kurallar:

- **Site izinlerini dar tutun.** Eklentiye yalnız gerçekten iş yaptırdığınız sitelerde izin verin; "her sitede" izni vermeyin. Team/Enterprise'da yöneticiler site izin ve engel listesi tanımlayabilir.
- **Tarayıcı ajanı için ayrı bir tarayıcı profili.** Bankacılık, e-posta ve yönetici panelleri ajanın erişebildiği profilde açık olmasın. Ajan JavaScript çalıştırma izni olan bir sitede, tarayıcının o sayfada görebildiği her şeyi (oturum dahil) görebilir.
- **Otonom kipi kapalı tutun.** Geri alınamayan işlemlerde (satın alma, silme, gönderme) onay sorması açık kalsın.
- **Eklentiyi güncel tutun** ve kurulu sürümü ayda bir kontrol edin; güvenlik düzeltmeleri sürümle gelir.
- **Çıktı filtresi güvenlik sınırı değildir.** Anthropic'in yardım sayfası bunu kendisi söyler; filtre bir savunma katmanıdır, tek başına güvenilmez.
- Tarayıcı ajanı da bir **tarayıcı eklentisidir**; [Bölüm 1](01-kurmadan-once.md)'in kaynak ve yayıncı kontrolleri geçerlidir. Mağazada aynı adı taşıyan taklitlere dikkat edin.

---

**Kaynaklar:** Claude Code veri kullanımı (https://code.claude.com/docs/en/data-usage); Anthropic, Piloting Claude for Chrome (https://www.anthropic.com/news/claude-for-chrome); Koi Security'nin "ShadowPrompt" bulgusu (Ocak 2026, eklenti 1.0.41'de düzeltildi).
