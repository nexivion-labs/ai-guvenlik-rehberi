# 8. Senaryolar: önle, fark et, müdahale et

[← İçindekiler](../README.md)

Her senaryo aynı yapıdadır: **ne olur**, **nasıl önlenir**, **nasıl fark edilir**, **olursa ne yapılır**. Senaryolar gerçek olaylardan ve sık görülen hatalardan seçildi; listede olmayan bir durum yaşarsanız [katkı](../CONTRIBUTING.md) olarak ekleyin.

| # | Senaryo | Öncelik |
|---|---|---|
| S1 | [Ajan bir sırrı commit'ledi ve push etti](#s1-ajan-bir-sırrı-commitledi-ve-push-etti) | P0 |
| S2 | [Ekip arkadaşının yapay zekâ hesabı ele geçirildi](#s2-ekip-arkadaşının-yapay-zekâ-hesabı-ele-geçirildi) | P0 |
| S3 | [Bilgi hırsızı tarayıcı oturumlarını çaldı](#s3-bilgi-hırsızı-tarayıcı-oturumlarını-çaldı) | P0 |
| S4 | [İki adımlı doğrulamanın bağlı olduğu telefon kayboldu](#s4-iki-adımlı-doğrulamanın-bağlı-olduğu-telefon-kayboldu) | P1 |
| S5 | [Klonlanan depodaki talimat dosyası ajanı yönlendirdi](#s5-klonlanan-depodaki-talimat-dosyası-ajanı-yönlendirdi) | P0 |
| S6 | [Ajan geri alınamayan bir işlem yaptı](#s6-ajan-geri-alınamayan-bir-işlem-yaptı) | P1 |
| S7 | [Onaylı bir MCP sunucusu güncellemeyle zararlıya dönüştü](#s7-onaylı-bir-mcp-sunucusu-güncellemeyle-zararlıya-dönüştü) | P1 |
| S8 | [Ajanın talimat dosyasına zararlı bir kural eklendi](#s8-ajanın-talimat-dosyasına-zararlı-bir-kural-eklendi) | P1 |
| S9 | [CI iş akışından sır sızdı](#s9-ci-iş-akışından-sır-sızdı) | P0 |
| S10 | [CI'daki ajan bir issue ile yönlendirildi](#s10-cidaki-ajan-bir-issue-ile-yönlendirildi) | P1 |
| S11 | [Olay müşteri ya da çalışan verisine dokundu](#s11-olay-müşteri-ya-da-çalışan-verisine-dokundu) | P0 |
| S12 | [Alarm yanlış çıktı](#s12-alarm-yanlış-çıktı) | P2 |
| S13 | [Dizüstü bilgisayar kayboldu ya da çalındı](#s13-dizüstü-bilgisayar-kayboldu-ya-da-çalındı) | P0 |
| S14 | [Ajan uydurma bir paket kurdu](#s14-ajan-uydurma-bir-paket-kurdu) | P1 |
| S15 | [Ayrılan ekip üyesinin erişimi kaldı](#s15-ayrılan-ekip-üyesinin-erişimi-kaldı) | P1 |

---

## S1. Ajan bir sırrı commit'ledi ve push etti

**Ne olur:** Ajan bir hatayı düzeltirken `.env` dosyasını, bir test dosyasına gömülü anahtarı ya da bir yapılandırma çıktısını commit'e ekler ve push eder. Herkese açık depolarda sızan anahtarlar dakikalar içinde otomatik tarayıcılar tarafından bulunur.

**Önleme**
- `.env*`, `*.pem`, `*.key`, `secrets/` `.gitignore`'da olsun.
- GitHub'da secret scanning ve **push protection** açık olsun ([Bölüm 7.3](07-ekip-politikasi.md#73-github-kuruluşu-için-asgari-ayarlar)).
- `git push` ajanda onaya bağlı olsun ([Bölüm 4.4](04-claude-code-sertlestirme.md#44-izinleri-bilinçli-verin)); ajanın commit'lerini push etmeden önce `git diff --staged` ile okuyun.
- Yerelde bir pre-commit sır tarayıcısı (ör. gitleaks) çalıştırın.

**Fark etme**
- GitHub secret scanning uyarısı ya da sağlayıcıdan gelen "anahtarınız herkese açık bir depoda bulundu" e-postası.
- `git log -p` içinde anahtar biçiminde dizeler.

**Müdahale**
1. **Önce anahtarı iptal edin ve yenisini üretin.** Geçmişi temizlemek tek başına yetmez; anahtar zaten kopyalanmış olabilir.
2. Sağlayıcının kullanım kayıtlarında, sızma anından sonraki yetkisiz kullanımı kontrol edin.
3. Sonra geçmişi temizleyin (`git filter-repo` ya da BFG) ve ekibe yeniden klonlamasını söyleyin. Fork'lar ve önbellekler temizlenmez; bu yüzden 1. adım esastır.
4. [Olay kaydına](../sablonlar/olay-kaydi.md) yazın.

## S2. Ekip arkadaşının yapay zekâ hesabı ele geçirildi

**Ne olur:** Vakamızdaki durum. Saldırgan bir ekip üyesinin oturumunu kullanarak ajan çalıştırır; ekibin depolarına erişimi olan bağlı GitHub hesabı üzerinden kod yazar ya da veri çeker.

**Önleme**
- Herkesin kendi hesabı ve kendi anahtarı olsun; paylaşılan hesap yok ([Bölüm 7.1](07-ekip-politikasi.md#71-beş-kural)).
- Varsayılan dal koruması: ajanın ya da tek bir kişinin `main`'e doğrudan yazması mümkün olmasın.
- Bağlı uygulamaların (GitHub ↔ yapay zekâ hesabı) yetkisi gereken depolarla sınırlı olsun.

**Fark etme**
- Kişinin yazmadığı commit'ler, PR'lar ya da beklenmeyen saatlerde çalışan CI.
- Yapay zekâ hesabında tanınmayan oturum, beklenmeyen kullanım artışı.

**Müdahale**
1. Kişiyi suçlamadan kuruluş erişimini geçici olarak kaldırın ([Bölüm 2](02-olay-aninda.md)).
2. Kişinin bağlı GitHub yetkisini ve token'larını iptal edin; olay aralığındaki commit'leri ve PR'ları listeleyin ve gözden geçirin. Şüpheli commit'leri geri alın (`git revert`), geçmişi silmeyin.
3. Olay aralığında kişinin erişebildiği bütün depo sırlarını (Actions secrets, deploy anahtarları) yenileyin.
4. Kişinin bilgisayarı için [Bölüm 2](02-olay-aninda.md) ve [Bölüm 3](03-claude-ile-adli-inceleme.md)'ü uygulayın.

## S3. Bilgi hırsızı tarayıcı oturumlarını çaldı

**Ne olur:** "Kırılmış" bir program, sahte bir güncelleme ya da zararlı bir eklenti, tarayıcıdaki çerezleri, kayıtlı şifreleri ve açık oturumları toplayıp gönderir. Saldırgan bu oturumlarla şifre ve iki adımlı doğrulama sormadan hesaplara girer. Ağustos 2026'da Claude hesaplarına yönelik dalga tam olarak buydu ([Bölüm 9](09-hesap-ve-oturum-guvenligi.md)).

**Önleme**
- [Bölüm 1](01-kurmadan-once.md): korsan yazılım ve resmî olmayan kaynaklardan kurulum yok.
- İş hesapları için eklentisiz ayrı tarayıcı profili; tarayıcıda şifre saklanmaz.
- Hassas konsollarda iş bitince çıkış.

**Fark etme**
- Birden fazla hizmette aynı anda tanınmayan oturumlar ya da zorunlu çıkışlar.
- Güvenlik aracında "Trojan:…Stealer" türü tespitler (vakamızda dokuz gün boyunca vardı).

**Müdahale**
1. Bilgisayarı ağdan ayırın; o bilgisayarda hiçbir hesaba girmeyin ([Bölüm 2](02-olay-aninda.md)).
2. Temiz cihazdan **bütün** hesaplarda tüm oturumlardan çıkış yapın; yalnız fark ettiğiniz hesapta değil. Bilgi hırsızı tarayıcıdaki her şeyi alır.
3. Tarayıcıda kayıtlı bütün şifreleri değiştirin; önce e-posta.
4. Bilgisayarı temizlemeden (tam format) yeniden oturum açmayın; yoksa yeni oturumlar da çalınır.

## S4. İki adımlı doğrulamanın bağlı olduğu telefon kayboldu

**Ne olur:** Doğrulama uygulaması, SMS ve çoğu zaman e-posta aynı telefondadır. Telefon kaybolur ya da çalınırsa hem hesaplarınıza giremezsiniz hem de telefonu bulan kişi bazı hesaplara erişebilir.

**Önleme**
- Her hesapta kurtarma kodları telefondan ve bilgisayardan bağımsız bir yerde ([Bölüm 9.2](09-hesap-ve-oturum-guvenligi.md#92-ikinci-adım-yöntemleri-güçlüden-zayıfa)).
- En az iki ikinci adım yöntemi (ör. passkey + yedek güvenlik anahtarı).
- Telefonda güçlü ekran kilidi; SIM kartında PIN.

**Fark etme**
- Telefonun kaybolması zaten fark edilir; önemli olan ilk saatte harekete geçmek.

**Müdahale**
1. Operatörü arayıp hattı dondurun (SIM kopyalamaya karşı).
2. Telefonu uzaktan kilitleyin ya da silin (Bul / Find My).
3. Temiz bir cihazdan, kurtarma kodlarıyla e-postaya girin; telefonu güvenilir cihazlardan çıkarın, oturumlarını sonlandırın.
4. Sonra GitHub, yapay zekâ hesabı ve diğerlerinde aynısını yapın; yeni telefonda iki adımlı doğrulamayı yeniden kurun ve **yeni** kurtarma kodları üretin.

## S5. Klonlanan depodaki talimat dosyası ajanı yönlendirdi

**Ne olur:** Bir eğitim videosundan ya da bir iş ilanının "ödev" deposundan bir proje klonlarsınız ve ajana "bunu kur ve çalıştır" dersiniz. Depodaki `CLAUDE.md`, `.cursorrules` ya da README, kurulumun parçası gibi görünen bir betik çalıştırmayı söyler; `.claude/settings.json` içindeki bir hook ya da `.mcp.json` içindeki bir sunucu, siz fark etmeden kod çalıştırır. Sahte iş görüşmesi ödevleri geliştiricilere karşı bilinen bir saldırı yöntemidir.

**Önleme**
- Yabancı depoyu önce ajansız açın ve [Bölüm 4.6](04-claude-code-sertlestirme.md#46-yabancı-bir-depoyu-açmadan-önce)'daki dosyaları okuyun.
- Tanımadığınız depoları ayrı bir sanal makinede ya da Dev Container'da, sırsız bir ortamda çalıştırın.
- Proje MCP sunucularını toptan onaylamayın; VS Code'da klasörü Kısıtlı Kip'te açın.

**Fark etme**
- Ajanın görevle ilgisiz bir adresten dosya indirmek, ev klasörünüzü taramak ya da ortam değişkenlerini okumak istemesi.
- Güvenlik kapısı hook'unun ([Bölüm 4.7](04-claude-code-sertlestirme.md#47-kendi-hooklarınızla-bir-güvenlik-ağı-kurun)) bir komutu engellemesi.

**Müdahale**
1. Ajan oturumunu durdurun; depoda ya da sistemde bir şey çalıştıysa [Bölüm 2](02-olay-aninda.md)'yi uygulayın.
2. Çalışan komutları ajan geçmişinden çıkarın; o ortamda bulunan anahtarları yenileyin.
3. Depoyu GitHub'a "Report abuse" ile bildirin.

## S6. Ajan geri alınamayan bir işlem yaptı

**Ne olur:** Ajan bir sorunu "çözmek" için veritabanı tablosunu siler, bir dalı zorla push eder, bulut kaynağını kapatır ya da migration'ı üretimde çalıştırır. Kötü niyet gerekmez; yanlış anlaşılmış bir görev yeter. OWASP bu sınıfı "araçların kötüye kullanımı" (ASI02) ve "zincirleme hatalar" (ASI08) olarak sayar.

**Önleme**
- Ajanın çalıştığı ortamda **üretim kimlik bilgisi bulunmasın**. Geliştirme ve üretim anahtarları ayrı olsun ([Bölüm 9.4](09-hesap-ve-oturum-guvenligi.md#94-api-anahtarları)).
- Yıkıcı komutlar `ask` ya da `deny` listesinde ([Bölüm 4.4](04-claude-code-sertlestirme.md#44-izinleri-bilinçli-verin)); dal koruması açık.
- Yedekler düzenli alınsın ve geri yükleme **denenmiş** olsun. Denenmemiş yedek, yedek değildir ([Bölüm 11](11-yedekleme-ve-kurtarma.md)).

**Fark etme**
- Ajan çıktısında `DROP`, `DELETE FROM` (WHERE'siz), `--force`, `terraform destroy`, `kubectl delete` gibi ifadeler.

**Müdahale**
1. Ajanı durdurun; zararın daha fazla yayılmasını engelleyin (ör. ilgili servisi bakım kipine alın).
2. Ajanın oturum geçmişinden tam olarak hangi komutların çalıştığını çıkarın.
3. Yedekten geri yükleyin; kayıp aralığını belgeleyin.
4. Geriye bakışta, bu işlemin neden onaysız çalışabildiğini bulun ve izin kurallarını düzeltin.

## S7. Onaylı bir MCP sunucusu güncellemeyle zararlıya dönüştü

**Ne olur:** Aylardır kullandığınız bir MCP sunucusu yeni bir sürüm yayımlar. Yeni sürüm, araç açıklamasına gizli bir talimat ekler ya da işlediği verinin bir kopyasını dışarı gönderir. `npx paket@latest` ile başlatıyorsanız güncelleme sizden habersiz gelir.

**Önleme**
- Sürümü sabitleyin; güncellemeyi bilinçli ve inceleyerek yapın ([Bölüm 5.4](05-istem-enjeksiyonu-ve-mcp.md#54-mcp-sunucuları)).
- npm'de `min-release-age` ile yeni sürümleri birkaç gün bekletin ([Bölüm 6.1](06-tedarik-zinciri.md#61-npm)).
- Sunucuya yalnız gereken kapsamda token verin; e-posta, ödeme gibi hassas sunucuları ayrı tutun.

**Fark etme**
- `/mcp` ile görülen araç listesinde ya da açıklamalarda değişiklik.
- Sunucunun beklenmeyen alan adlarına bağlanması (sandbox ağ onayı, güvenlik duvarı kayıtları).

**Müdahale**
1. Sunucuyu yapılandırmadan çıkarın; verdiğiniz token'ı iptal edin.
2. Sunucunun çalıştığı süre boyunca eriştiği verileri belirleyin (ör. gönderilen e-postalar, okunan depolar).
3. Paketi npm'e "Report malware" ile bildirin; ekibe duyurun ve onaylı listeden kaldırın.

## S8. Ajanın talimat dosyasına zararlı bir kural eklendi

**Ne olur:** Ajan bir web sayfasını ya da issue'yu okurken içindeki gizli talimatla `CLAUDE.md` dosyasına "her commit'ten önce şu betiği çalıştır" gibi bir satır ekler. Oturum biter, satır kalır ve sonraki her oturumda çalışır.

**Önleme**
- Talimat dosyaları sürüm kontrolünde; değişiklikleri onaya bağlı ([Bölüm 5.3](05-istem-enjeksiyonu-ve-mcp.md#53-kalıcı-zehirlenme-ajanın-belleği)).
- Dış içerik okutulan oturumlarda dosya düzenleme yetkisi dar.

**Fark etme**
- `git status` ya da `git diff` çıktısında sizin istemediğiniz bir talimat dosyası değişikliği.
- Ajanın görevle ilgisiz bir adımı "proje kuralı" diye gerekçelendirmesi.

**Müdahale**
1. Eklenen satırı silin ve commit'leyin; satırın hangi oturumda, hangi içerik okunurken eklendiğini bulun.
2. Satır eklendikten sonraki oturumlarda ajanın o kurala göre ne yaptığını gözden geçirin; bir komut çalıştıysa [Bölüm 2](02-olay-aninda.md)'ye geçin.
3. Kaynağı (web sayfası, issue, MCP sunucusu) engel listesine alın ve ekibe duyurun.

## S9. CI iş akışından sır sızdı

**Ne olur:** Sabitlenmemiş bir eylemin yeni sürümü sırları günlüğe yazar ya da dışarı gönderir; veya `pull_request_target` ile çalışan bir iş akışı fork'tan gelen kodu ana deponun sırlarıyla çalıştırır. Sızan sırlar arasında npm yayın token'ı varsa saldırgan sizin adınıza zararlı sürüm yayımlayabilir ve olay kendi kullanıcılarınıza yayılır.

**Önleme**
- [Bölüm 6.4](06-tedarik-zinciri.md#64-github-actions): `permissions: {}`, SHA ile sabitleme, `pull_request_target` yok, `persist-credentials: false`, OIDC.
- Yayın token'ları yalnız yayın iş akışında ve korumalı bir ortamda (environment, onaylı) bulunsun.

**Fark etme**
- İş akışı günlüklerinde maskelenmemiş değerler, beklenmeyen ağ bağlantıları, sizin tetiklemediğiniz çalıştırmalar.
- Paket kayıt defterinde sizin yayımlamadığınız bir sürüm.

**Müdahale**
1. Etkilenen iş akışlarını devre dışı bırakın (Actions → iş akışı → Disable).
2. O iş akışının erişebildiği **bütün** sırları yenileyin; yalnız sızdığını gördüğünüzü değil.
3. Zararlı sürüm yayımlandıysa kayıt defterinde kaldırın ya da "deprecate" edin ve kullanıcılarınıza duyurun.
4. Günlükleri silmeden önce indirip delil olarak saklayın.

## S10. CI'daki ajan bir issue ile yönlendirildi

**Ne olur:** Issue ya da yorumla tetiklenen bir ajan, issue metnindeki gizli talimatla depo sırlarını bir PR'a ya da yoruma yazar, iş akışı dosyasını değiştirir veya ilgisiz bir değişiklik açar.

**Önleme**
- Ajan yalnız yazma yetkili kişilerce tetiklenebilsin ([Bölüm 6.4](06-tedarik-zinciri.md#cida-ajan-çalıştırıyorsanız)).
- Ajanın iş akışında üretim sırrı yok; izinler en dar; ajanın PR'ları insan onayı olmadan birleşmiyor.

**Fark etme**
- Ajanın görevle ilgisiz dosyalara (özellikle `.github/workflows/`) dokunması, yorumlarda sır biçiminde dizeler.

**Müdahale**
1. Ajanın iş akışını devre dışı bırakın; açtığı PR'ları ve yorumları silmeden gizleyin.
2. İş akışının erişebildiği sırları yenileyin.
3. Tetikleyen issue'yu ve hesabı GitHub'a bildirin.

## S11. Olay müşteri ya da çalışan verisine dokundu

**Ne olur:** Ele geçirilen bilgisayarda, depoda ya da ajanın erişebildiği bir veritabanında kişisel veri vardı (müşteri listesi, iletişim bilgileri, sağlık ya da finans verisi). Olay artık yalnız teknik değil, hukuki bir olaydır.

**Önleme**
- Geliştirme ortamında gerçek kişisel veri kullanmayın; maskelenmiş ya da sentetik veri kullanın.
- Ajanın erişebildiği yerlerde kişisel veri bulunmasın ([çekirdek kural 3](00-cekirdek-kurallar.md)).
- Hangi sistemde hangi kişisel verinin bulunduğunu bir yerde yazın.

**Fark etme**
- Olay incelemesinde ([Bölüm 3](03-claude-ile-adli-inceleme.md)) erişilen dosya, depo ya da veritabanlarının kişisel veri içerdiğinin anlaşılması.

**Müdahale**
1. Hangi verinin, kaç kişiye ait olduğunu ve erişimin kesin mi olası mı olduğunu yazılı hâle getirin.
2. **Hemen bir hukukçuya danışın.** 6698 sayılı KVKK'nın 12/5 maddesi veri sorumlusuna ihlali "en kısa sürede" Kurula ve ilgili kişilere bildirme yükümlülüğü getirir; Kişisel Verileri Koruma Kurulu'nun 24.01.2019 tarih ve 2019/10 sayılı kararı bu süreyi **ihlalin öğrenilmesinden itibaren en geç 72 saat** olarak yorumlar. 72 saat içinde bildirilemezse gecikmenin gerekçesi de bildirimle birlikte açıklanır. Bildirim kvkk.gov.tr'deki Veri İhlali Bildirim Formu ile yapılır. Süre, ihlal doğrulandığında değil **öğrenildiğinde** başlar; bu yüzden olay kaydındaki saatler önemlidir. Güncel yükümlülüğü hukukçunuzla doğrulayın.
3. Etkilenen kişilere bildirim gerekip gerekmediğine hukukçuyla birlikte karar verin.
4. Bütün kararları ve gerekçelerini [olay kaydına](../sablonlar/olay-kaydi.md) yazın.

## S12. Alarm yanlış çıktı

**Ne olur:** Tanınmayan oturum aslında sizin yeni telefonunuzdu; şüpheli eklenti zararsız çıktı. Müdahale başlatılmıştı.

**Yapılacaklar**
1. Yanlış alarm olduğunu **kanıtla** kapatın (ör. oturumun IP'si ve cihazı sizinkiyle eşleşiyor); "galiba" ile kapatmayın.
2. Yenilediğiniz anahtarları geri almayın; yenilenmiş anahtar her zaman iyidir.
3. Olay kaydına "yanlış alarm" olarak yazın ve neden alarm verdiğini not edin. Aynı belirti tekrar ederse hızlı karar verebilmek için.
4. Kimseyi alarm verdiği için eleştirmeyin. Erken bildirim, [Bölüm 7](07-ekip-politikasi.md)'nin dördüncü kuralıdır.

## S13. Dizüstü bilgisayar kayboldu ya da çalındı

**Ne olur:** İçinde açık oturumlar, `~/.claude/.credentials.json`, SSH anahtarları, tarayıcıda kayıtlı şifreler ve oturum dökümleri olan bir bilgisayar başkasının eline geçer. Disk şifreli değilse her şey okunabilir; şifreliyse ama bilgisayar uyku kipindeyse ve ekran kilidi zayıfsa yine okunabilir.

**Önleme**
- **Tam disk şifreleme** her bilgisayarda açık: Windows'ta BitLocker (kurtarma anahtarı şirket hesabında ya da parola yöneticisinde, bilgisayarda değil), macOS'ta FileVault, Linux'ta LUKS.
- Kısa süreli otomatik ekran kilidi ve güçlü oturum parolası; uyku yerine kapatma alışkanlığı, özellikle seyahatte.
- Uzaktan bulma ve silme açık (Find My, Windows'ta Cihazımı Bul ya da MDM).
- Bilgisayarda duran her anahtarın [envanteri](../sablonlar/onayli-araclar.md) olsun; olay anında neyi iptal edeceğinizi bilirsiniz.

**Fark etme**
- Kayıp zaten fark edilir; kritik olan ilk saatte hareket etmek.

**Müdahale**
1. Uzaktan kilitle ya da sil.
2. [Olay anında, ilk saat](02-olay-aninda.md)'in tamamı: o bilgisayarda bulunan **her** oturum ve anahtar ele geçirilmiş sayılır (disk şifreli olsa bile; "muhtemelen açamazlar" bir güvenlik varsayımı değildir).
3. SSH anahtarını sunuculardan ve GitHub'dan kaldırın; bilgisayara özel Claude Code yetkisini silin.
4. Şirket bilgisayarıysa yönetime ve gerekiyorsa polise bildirin; kişisel veri içeriyorsa [S11](#s11-olay-müşteri-ya-da-çalışan-verisine-dokundu).

## S14. Ajan uydurma bir paket kurdu

**Ne olur:** Ajan, var olmayan bir paket adı üretir ve `npm install` ya da `pip install` ile kurmaya çalışır. Ad daha önce bir saldırgan tarafından kaydedilmişse kurulum başarılı olur ve zararlı kod çalışır ([Bölüm 14.1](14-ajanin-yazdigi-kod.md#141-sayılar)).

**Önleme**
- Kurulum komutları onaya bağlı; ajan paketi göstermeden kurmaz ([örnek CLAUDE.md](../ornekler/CLAUDE.md.ornek)).
- `.npmrc`'de `min-release-age` ve betik engeli ([Bölüm 6.1](06-tedarik-zinciri.md#61-npm)): yeni kaydedilmiş zararlı paket bekleme süresine takılır, kurulum betiği çalışmaz.
- Sandbox açık: kurulum betiği çalışsa bile ağ ve dosya sınırı var.

**Fark etme**
- Kurulumdan sonra tanımadığınız ağ bağlantıları, yeni süreçler, Temp'te yeni çalıştırılabilir dosyalar ([Bölüm 10](10-platform-basvuru-karti.md)).
- Paket kayıt defterinde paket sayfasının birkaç günlük olması, deposuz ve açıklamasız olması.

**Müdahale**
1. Paket adını kayıt defterinde kontrol edin: gerçekten yok mu, yoksa yeni kayıtlı şüpheli bir paket mi? İkincisiyse bilgisayarı ele geçirilmiş sayın ve [Bölüm 2](02-olay-aninda.md)'ye geçin.
2. `node_modules` / sanal ortamı silmeden önce paketin içeriğini (özellikle `package.json` betiklerini) delil olarak kopyalayın.
3. Paketi kayıt defterine bildirin ("Report malware").

## S15. Ayrılan ekip üyesinin erişimi kaldı

**Ne olur:** Biri ekipten ayrılır; GitHub'dan çıkarılır ama paylaşılan bir API anahtarını, bir deploy anahtarını ya da ekip yapay zekâ hesabındaki bir oturumu bilmeye devam eder. Kötü niyet şart değil: eski bilgisayarındaki bir ajan oturumu hâlâ geçerli olabilir, ya da o bilgisayar daha sonra ele geçirilebilir.

**Önleme**
- Paylaşılan anahtar yok; her kişinin kendi kimliği ([Bölüm 7.1](07-ekip-politikasi.md#71-beş-kural)). Ayrılışta yalnız o kişinin anahtarları iptal edilir.
- [Ayrılış listesi](07-ekip-politikasi.md#77-biri-ayrıldığında) işe giriş kadar ciddiye alınır ve aynı gün tamamlanır.

**Fark etme**
- Kişi ayrıldıktan sonra onun adına görünen oturum, commit ya da API kullanımı.
- Aylık kontrolde ([liste](../kontrol-listeleri/aylik-kontrol.md)) kuruluş üyeleri ve yetkili uygulamalar gözden geçirilirken.

**Müdahale**
1. Kalan erişimi hemen kapatın; kişiyle açık bir dille konuşun (çoğu durumda unutulmuş bir yetkidir).
2. Kişinin ayrılışından sonra o erişimle yapılmış işlem var mı diye günlükleri inceleyin.
3. Ayrılış listesinde neden eksik kaldığını bulun ve listeyi düzeltin.
