# Kurmadan önce: tek sayfalık kontrol listesi

Yazdırın, masanıza asın. Bir tane bile "hayır" varsa kurmayın. Ayrıntılar: [Bölüm 1](../docs/01-kurmadan-once.md).

**Araç / eklenti / paket adı:** ______________________ **Tarih:** __________ **Kontrol eden:** __________

## Kaynak
- [ ] Resmî kaynaktan geliyor (Marketplace, npm, PyPI, resmî site ya da resmî GitHub deposu). DM, Discord, YouTube açıklaması, WhatsApp değil.
- [ ] Yayıncı doğrulanmış; ad taklit değil (harf değişikliği, `-pro`, `-free` eki yok).
- [ ] "Kırılmış", "bedava", "sınırsız token" vaadi yok.
- [ ] Eklenti kimliği (`yayıncı.ad`) resmî kaynaktakiyle birebir aynı (Open VSX dahil).

## Kimlik ve geçmiş
- [ ] Hesap/depo yeni değil, birden fazla katkıcı var, ani yıldız artışı yok.
- [ ] "ad + malware/virus/trojan/stealer" araması temiz.
- [ ] Son sürüm beklenmedik değil; değişiklik notu kodla uyumlu.

## Kod
- [ ] `preinstall` / `install` / `postinstall` betikleri okundu ve anlaşıldı.
- [ ] `activationEvents` içinde `*` ya da `onStartupFinished` yok (ya da neden olduğu açık).
- [ ] Süreç başlatma, dosya indirme, Temp'e `.exe` yazma, `eval`, uzun base64 yok ya da açıklanabilir.
- [ ] Dosya boyutu normal; kod karartılmış değil.
- [ ] `curl | sh` ya da `irm | iex` çalıştırılmadı; betik önce okundu.

## Tarama ve deneme
- [ ] SHA-256 VirusTotal'da arandı (dosya yüklenmedi). Hash: ______________________
- [ ] Önce ayrı ortamda (VM, ayrı kullanıcı, Dev Container, Windows Sandbox) denendi.

## Bilgisayar
- [ ] Tam disk şifreleme açık (BitLocker / FileVault / LUKS); kurtarma anahtarı bilgisayar dışında.

## Yetki
- [ ] Yalnız proje klasörüne erişim; Workspace Trust açık.
- [ ] Sırlar düz dosyada değil; ajanın okuması engelli.
- [ ] Ekip bilgisayarıysa onaylı listeye eklendi.

## Kurduktan sonra (ilk 7 gün)
- [ ] Güvenlik aracının geçmişi her gün kontrol edildi.
- [ ] Açılışta çalışanlar ve yeni süreçler kontrol edildi.
