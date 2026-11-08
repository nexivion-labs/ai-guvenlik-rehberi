# 15. Tuzak kur, zinciri kır

[← İçindekiler](../README.md)

Rehberin önceki bölümleri saldırganı kapıda durdurmayı anlatır. Bu bölüm iki soruyu cevaplar: kapı yine de açılırsa bunu **erkenden** nasıl anlarsınız, ve saldırının hangi halkasını kırmak size yeter? Vakamızda bilgisayar dokuz gün boyunca enfekte kaldı; bu sürenin kısalması, kapıyı hiç açtırmamak kadar değerlidir.

---

## 15.1 Saldırı tek hamle değil, bir zincirdir

Bir saldırı birbirine dayanan halkalardan oluşur. Savunmacının her halkayı durdurması gerekmez; **tek bir halkayı kırmak zinciri boşa çıkarır.** Yapay zekâ ajanıyla çalışan bir geliştirici için halkalar ve kırma noktaları şöyledir:

| Halka | Saldırgan ne yapar | Sizde karşılığı | Kim görür, kim keser |
|---|---|---|---|
| Keşif | Açık profilinize, depolarınıza, hangi aracı kullandığınıza bakar | Herkese açık depolar, sosyal medya paylaşımları | Sırları ve iç yapıyı herkese açık depolardan uzak tutan siz |
| İlk giriş | Sahte eklenti, paket ya da "ücretsiz kredi" vaadiyle gelen kurulum komutu | Editör eklentileri, `npm`/`pip` paketleri, tek satırlık kurulumlar | [Bölüm 1](01-kurmadan-once.md)'deki kurulum disiplini |
| Yetki | Sizin kullanıcı yetkinizle çalışır, ajanın erişebildiği her şeye erişir | Ajanın izinleri, diskteki anahtarlar ve oturum dosyaları | [Bölüm 4](04-claude-code-sertlestirme.md): izinler, sandbox, sır yönetimi |
| Kalıcılık | Bilgisayar her açıldığında geri gelir | Açılışta çalışan programlar, kabuk başlangıç dosyaları, ajanın talimat ve kanca dosyaları | Haftalık fark kontrolü (15.4) |
| Dışarı çıkış | Topladığını dışarı gönderir, yeni komut alır | Dışarıya giden bağlantılar | Dışa giden trafiği izleyen bir güvenlik duvarı (15.5) |
| Etki | Hesabınızı kullanır, kodunuzu başka yere gönderir, kullanım hakkınızı tüketir | Sağlayıcıdaki oturumlar, kullanım ve fatura | Harcama uyarısı ve oturum listesine düzenli bakış ([Bölüm 9](09-hesap-ve-oturum-guvenligi.md)) |

**15 dakikalık alıştırma:** Bu tabloyu kendi ortamınız için doldurun. "Kim görür, kim keser" sütununda boş kalan satır, ilk işinizdir.

## 15.2 Kanarya sırları: yanlış alarm üretmeyen tuzak

Meşru hiçbir işin dokunmadığı sahte bir sır, dokunulduğu anda ihlalin kanıtıdır. Bu yüzden kanarya, güvenlik araçlarının çoğundan farklı olarak **yanlış alarm üretmez**: o anahtarı kullanan ya sizin bilgisayarınızı ele geçirmiştir ya da ajanınızı.

Uygulaması:

1. Ücretsiz bir kanarya servisinden (ör. [canarytokens.org](https://canarytokens.org)) sahte bir bulut erişim anahtarı üretin. Anahtar gerçek görünür ama hiçbir şeye erişmez; biri onu kullanmayı denediğinde size e-posta gelir.
2. Anahtarı bir bilgi hırsızının ya da ele geçirilmiş bir ajanın önce bakacağı yere koyun: ev klasöründeki bulut kimlik dosyası (örneğin `~/.aws/credentials` içinde ayrı bir profil) ya da bir deponun yerel ortam dosyası.
3. Kendi ajanınızın o dosyayı okumasını izin kurallarıyla kapatın ([Bölüm 4.3](04-claude-code-sertlestirme.md#43-sırlara-erişimi-kapatın)). Böylece kendi ajanınız alarmı yanlışlıkla tetiklemez; tetiklenirse kuralı biri aşmış demektir.
4. Uyarı e-postasını, ele geçirilmiş bir bilgisayardan okunmayan bir adrese yönlendirin.

Kanarya gelirse [Olay anında](02-olay-aninda.md) bölümünü kırmızı seviyeden uygulayın. Kanarya hiçbir şeyi engellemez; yalnız **haber verir**, ama vakamızdaki dokuz günün kısalması tam olarak buna bağlıdır.

## 15.3 Görünen kaynak gerçek kaynak değildir

Ele geçirilmiş bir ajan **sizin** oturumunuzla, sizin hesabınızdan iş görür. Kayıtlarda yapan kişi olarak siz görünürsünüz. Bu iki sonuç doğurur:

- **"Bunu ben yapmadım" diyebilmeniz için kayıt gerekir.** Ajanın yaptığı her işlemi ayrı bir dosyaya yazan küçük bir kanca kurun. Claude Code'da `settings.json` içine:

  ```json
  {
    "hooks": {
      "PostToolUse": [
        { "matcher": "*", "hooks": [ { "type": "command", "command": "jq -c '{t: now | todate, arac: .tool_name, oturum: .session_id, girdi: .tool_input}' >> ~/.claude/arac-kaydi.jsonl" } ] }
      ]
    }
  }
  ```

  Bu kayıt `jq` gerektirir ve aracın girdisini olduğu gibi yazar, yani okunan dosyanın yolu ya da yazılan metin kayda girer. Kaydı da bir sır gibi koruyun ve ajanın okumasını kapatın. Bilgisayar ele geçirilirse saldırgan bu dosyayı silebilir; yine de sessiz ilerleyen bir saldırının ilk ipucu çoğu zaman burada çıkar. Ayar adlarını kendi sürümünüzün belgesiyle doğrulayın: https://code.claude.com/docs/en/hooks
- **Talimatın dili saldırganın kimliğini kanıtlamaz.** Vakamızdaki talimatlar Çinceydi; bu, saldırganın nereden geldiği hakkında hiçbir şey kanıtlamaz. Dil, hatta saat dilimi, yanıltmak için seçilmiş olabilir. Olayı anlatırken ve sağlayıcıya bildirirken davranışı anlatın (ne zaman, hangi oturumdan, ne yapıldı); ülke ya da kişi suçlaması yapmayın.

## 15.4 Ajanın talimat dosyaları da bir arka kapıdır

Ajan her açılışta talimat ve hafıza dosyalarını (`CLAUDE.md` ve benzerleri), kanca tanımlarını, MCP sunucu kayıtlarını ve özel komutları okur. Bu dosyalara yazılmış tek bir satır, **şifreleriniz değiştirildikten sonra da** yaşamaya devam eder: her yeni oturum o talimatı yeniden okur.

- Ev klasöründeki ajan ayarlarını (`~/.claude/` altındaki ayar, talimat ve komut dosyaları) haftada bir kontrol edin; mümkünse bunları özel bir depoda sürüm denetimine alın ve farkları okuyun.
- Depo içindeki `CLAUDE.md`, `.claude/`, `.mcp.json`, `.vscode/` ve git kanca dosyalarındaki her değişikliği kod gibi inceleyin; bunlar ajan için koddan daha yetkilidir.
- Tanımadığınız bir dilde yazılmış ya da tanımadığınız bir adrese giden her satırı alarm sayın.

Olay sonrasında temizlik yaparken bu dosyalar da listeye girer; ayrıntı [Bölüm 5](05-istem-enjeksiyonu-ve-mcp.md)'te.

## 15.5 Dışarı giden yol en ucuz halkadır

Komut almak da veri çıkarmak da dışarıya bağlantı ister. Belgelenmiş birçok olayda saldırıyı yakalayan şey, olağan dışı bir saatte olağan dışı bir adrese giden trafik olmuştur.

- Ajanın sandbox'ında ağ erişimini izin listesine çekin ([Bölüm 4.5](04-claude-code-sertlestirme.md#45-sandboxı-açın)).
- Bilgisayarda dışa giden bağlantıları soran bir uygulama güvenlik duvarını bir hafta uyarı kipinde çalıştırın ve "hangi program nereye konuşuyor" listesini çıkarın. Editörünüzün ya da tanımadığınız bir programın tanımadığınız bir adrese gece bağlanması, incelemeye değer bir belirtidir.

## 15.6 Gürültü yem olabilir

Göz önündeki belirti (çöken bir servis, art arda gelen doğrulama istekleri, bir uyarı e-postası) dikkatinizi çekerken asıl iş başka yerde sessizce yürüyebilir. Görünür belirtiyi kapattıktan sonra durmayın: kalıcılık noktalarını (15.4), oturum listesini ve dışa giden trafiği (15.5) yine kontrol edin. Olayı konuştuğunuz kanal da ele geçirilmiş olabilir; ikinci bir kanal belirleyin ([Bölüm 2](02-olay-aninda.md), İletişim).

## 15.7 Geri saldırmayın

Saldırganın sunucusuna, deposuna ya da hesabına karşılık vermek, onu "durdurmak" için bile olsa, hukuken gri bölgededir ve çoğu zaman suçtur. Üstelik yanlış adrese vurabilirsiniz: saldırganlar sık sık başkasının ele geçirilmiş makinesini kullanır. Doğru yol şudur: **tespit edin, delili koruyun, bildirin.** Kötüye kullanılan depoyu ya da hesabı platformun kendi bildirim yoluyla bildirin ([Bölüm 2](02-olay-aninda.md), Bildirim).

---

**Kaynaklar:** Thinkst Canarytokens belgeleri (https://docs.canarytokens.org/guide/); Claude Code kanca belgeleri (https://code.claude.com/docs/en/hooks); NIST SP 800-61 Rev. 3 (olay müdahalesi); MITRE ATT&CK, Persistence ve Exfiltration taktikleri (https://attack.mitre.org).

**Önceki:** [← 14. Ajanın yazdığı kod](14-ajanin-yazdigi-kod.md) · **Sonraki:** [İçindekiler](../README.md)
