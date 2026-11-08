# 12. Bulutta ve konteynerde çalışan ajanlar

[← İçindekiler](../README.md)

Rehberin büyük kısmı ajanın **sizin bilgisayarınızda** çalıştığını varsayar. Üç durumda öyle değildir: ajan Anthropic'in yönettiği bir sanal makinede çalışır (Claude Code on the web), GitHub'ın sanal makinesinde çalışır (Codespaces) ya da sizin kurduğunuz bir konteynerde çalışır (Dev Container). Yalıtım bu durumlarda daha güçlüdür; ama "bulutta çalışıyor, güvende" varsayımı da yanlıştır. Her birinin kendi sınırı ve kendi tuzağı vardır.

---

## 12.1 Yalıtım seviyeleri

Anthropic'in kendi belgesi seviyeleri hafiften ağıra şöyle sıralar; hepsi için aynı uyarıyı yapar: **yalıtım, bir ihlalin etkisini azaltır, riski ortadan kaldırmaz.** Ve yalıtım, modele ne gönderildiğini değiştirmez: ajanın okuduğu dosyalar sandbox olsun olmasın sağlayıcıya gider.

| Seviye | Ne sarar | Ne sarmaz |
|---|---|---|
| Yerleşik Bash sandbox'ı (`/sandbox`) | Kabuk komutları ve alt süreçleri | Claude'un dosya araçları, hook'lar, MCP sunucuları ([Bölüm 4.5](04-claude-code-sertlestirme.md#45-sandboxı-açın)) |
| Sandbox runtime (`@anthropic-ai/sandbox-runtime`) | Claude Code sürecinin tamamı: dosya araçları, hook'lar, MCP dahil | Sizin bilgisayarınızda, aynı kullanıcıyla çalışmaya devam eder |
| Dev Container / özel konteyner | Sürecin tamamı + ayrı dosya sistemi | Konteynere bağladığınız (mount) klasörler ve geçirdiğiniz ortam değişkenleri |
| Ayrı sanal makine (Claude Code on the web, Codespaces) | Her şey; ayrı çekirdek | Sanal makineye verdiğiniz kimlik bilgileri ve ağ izinleri |

Kural: **Ajanın okuduğu içeriğe ne kadar az güveniyorsanız, o kadar ağır yalıtım seçin.** Kendi kodunuz üzerinde çalışırken yerleşik sandbox yeter; internetten gelen bir depoyu ilk kez açarken sanal makine ya da konteyner kullanın ([S5](08-senaryolar.md#s5-klonlanan-depodaki-talimat-dosyası-ajanı-yönlendirdi)).

## 12.2 Claude Code on the web

Resmî belgelere göre her oturum Anthropic'in yönettiği ayrı bir sanal makinede çalışır; ağ erişimi varsayılan olarak bir izin listesiyle sınırlıdır ve tamamen kapatılabilir ya da belirli alan adlarıyla sınırlanabilir; GitHub token'ınız sandbox'a hiç girmez, içeride yalnız depoya özel kapsamlı bir kimlik bilgisi bulunur ve bir vekil (proxy) bunu gerçek token'ınıza çevirir; oturum sanal makineleri bir süre kullanılmayınca geri alınır.

Bu sizin için ne demek:

- **Bilgisayarınızdaki zararlı yazılım bu oturumu göremez**, ama hesabınızı görebilir. Vakamızdaki gibi oturum bilgisi çalınırsa saldırgan web oturumlarını sizin adınıza başlatabilir. [Bölüm 9](09-hesap-ve-oturum-guvenligi.md) burada da geçerlidir.
- **Ağ izin listesini daraltın.** Varsayılan liste paket kayıt defterlerini kapsar; projeniz başka bir yere bağlanmıyorsa listeyi küçültün ya da ağı kapatın. İstem enjeksiyonunun dışarı veri gönderme yolu buradan kapanır ([tehlikeli üçlü](05-istem-enjeksiyonu-ve-mcp.md#tehlikeli-üçlü)).
- **Depoya sır koymayın.** Sanal makinede ajan depoyu klonlar; depoda duran bir `.env` oradadır. Bulut oturumu, sırları depodan uzak tutma kuralını gevşetmez.
- **Uzaktan kontrol oturumları farklıdır.** Web arayüzünün sizin bilgisayarınızdaki Claude Code'a bağlandığı kipte sanal makine yoktur; her şey yerelde çalışır ve bu rehberin yerel bölümleri geçerlidir.
- **Kuruluşunuz oturumları kendi altyapısına yönlendiriyorsa** yalıtım, ağ çıkışı ve git kimlik bilgileri sizin sorumluluğunuzdadır; yukarıdaki güvenceler Anthropic'in barındırdığı ortam içindir.

## 12.3 GitHub Codespaces ve Dev Container

Codespaces her codespace'i yeni bir sanal makinede çalıştırır ve her yeniden başlatmada güncel bir makineye taşır. Ajanı burada çalıştırmak, bilgisayarınızı korur. Dikkat edilecekler:

- **Yönlendirilen portlar.** Bir portu "public" yaparsanız URL'yi bilen herkes kimlik doğrulamasız erişir. Araştırmacılar bunun zararlı dosya dağıtmak için kullanılabildiğini göstermiştir. Portları özel tutun; kuruluş düzeyinde public port yönlendirmeyi kapatın.
- **Codespaces sırları ortam değişkeni olarak gelir.** Depoya yazma yetkisi olmayan bir kullanıcının codespace'ine sırlar enjekte edilmez; bu iyi bir varsayılandır. Ama yazma yetkisi olan herkes o sırları görür; Codespaces kullanımını belirli kullanıcılarla sınırlayın ve sırların kapsamını depo bazında tutun.
- **`devcontainer.json` koddur.** Yabancı bir depoyu codespace'te açmak, o deponun `devcontainer.json` dosyasındaki `postCreateCommand` gibi komutları çalıştırır. [Bölüm 4.6](04-claude-code-sertlestirme.md#46-yabancı-bir-depoyu-açmadan-önce)'daki dosya listesine bunu da ekleyin.
- **Settings Sync** codespace'e de eklentilerinizi taşır; [Bölüm 1.5](01-kurmadan-once.md) uyarısı burada da geçerlidir.
- **Dev Container'da** Docker soketini (`/var/run/docker.sock`) konteynere bağlamayın; bağlarsanız konteyner ana makineyi yönetebilir ve yalıtım biter. Ana makineden yalnız proje klasörünü bağlayın; ev klasörünü değil.
- **Codespaces IP'lerini güvenlik duvarı izin listesine eklemeyin.** O IP aralığını başka müşteriler de kullanır.

## 12.4 Her üç ortam için ortak kurallar

1. **Atılabilir ortam, atılabilir kimlik bilgisi demektir.** Buluttaki ya da konteynerdeki ajana verdiğiniz her token kısa ömürlü ve dar kapsamlı olsun; ortam silinince token da iptal edilsin.
2. **Üretim anahtarı asla.** Yalıtım ne kadar iyi olursa olsun, ajanın çalıştığı ortamda üretim anahtarı bulunmasın ([S6](08-senaryolar.md#s6-ajan-geri-alınamayan-bir-işlem-yaptı)).
3. **Çıktıyı yine okuyun.** Ortam yalıtılmış olsa da ajanın açtığı PR sizin deponuza girer. İnceleme adımı kalkmaz.
4. **Denetim günlüğünü açık tutun.** Codespaces oluşturma/silme ve izin değişiklikleri GitHub audit log'unda görünür; olay anında [dışa aktarın](02-olay-aninda.md#3-github).

---

**Kaynaklar:** Claude Code güvenlik ve sandbox ortamları belgeleri (https://code.claude.com/docs/en/security, https://code.claude.com/docs/en/sandbox-environments); Anthropic mühendislik yazısı, Claude Code sandboxing (https://www.anthropic.com/engineering/claude-code-sandboxing); GitHub, Security in GitHub Codespaces (https://docs.github.com/en/codespaces/reference/security-in-github-codespaces).
