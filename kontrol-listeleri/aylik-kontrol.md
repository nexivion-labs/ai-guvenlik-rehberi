# Aylık kontrol (30 dakika)

Her ayın ilk iş günü. Ayrıntılar: [Bölüm 7](../docs/07-ekip-politikasi.md).

**Ay:** __________ **Kontrol eden:** __________

## Bilgisayar (herkes, kendi bilgisayarında)
- [ ] Güvenlik aracının geçmişi (Windows Güvenliği → Koruma geçmişi ya da eşdeğeri) okundu. Tekrarlayan tespit var mı?
- [ ] Açılışta çalışanlar ve zamanlanmış görevler: tanınmayan yok.
- [ ] Kurulu editör eklentileri onaylı listeyle karşılaştırıldı; kullanılmayanlar kaldırıldı.
- [ ] Tarayıcı eklentileri gözden geçirildi.
- [ ] İşletim sistemi, editör ve ajan araçları güncel.

## Yapay zekâ araçları
- [ ] Claude (ya da kullanılan sağlayıcı) etkin oturumlar: tanınmayan yok.
- [ ] Claude Code yetkileri: kullanılmayan cihazlarınki silindi.
- [ ] API anahtarları: kullanılmayanlar iptal edildi; süresi uzun olanlar yenilendi.
- [ ] Kullanım ve fatura ekranında beklenmedik artış yok.
- [ ] `/permissions` ile `allow` listesi gözden geçirildi; geniş kurallar silindi.
- [ ] MCP sunucuları onaylı listeyle karşılaştırıldı; sürümleri sabit.
- [ ] Eski oturum dökümleri (`~/.claude/projects/` ve diğer ajanların geçmişi) temizlendi.
- [ ] Tarayıcı ajanı kullanılıyorsa site izinleri ve eklenti sürümü gözden geçirildi.

## GitHub
- [ ] Oturumlar, token'lar, SSH anahtarları ve yetkili uygulamalar: tanınmayan ya da kullanılmayan yok.
- [ ] Kuruluş üyeleri ve dış işbirlikçiler güncel.
- [ ] Secret scanning uyarıları kapatıldı ya da ele alındı.

## Ekip (güvenlik sorumlusu)
- [ ] Onaylı araçlar listesi güncellendi.
- [ ] [Beş ölçüt](../docs/07-ekip-politikasi.md#74-ölçün-beş-sayı) yazıldı; kötüye giden varsa bir eylem açıldı.
- [ ] Son tatbikatın üzerinden 6 aydan fazla geçtiyse tarih belirlendi.
- [ ] Son geri yükleme tatbikatının üzerinden 3 aydan fazla geçtiyse tarih belirlendi ([Bölüm 11.3](../docs/11-yedekleme-ve-kurtarma.md#113-geri-yükleme-tatbikatı-üç-ayda-bir-30-dakika)).
- [ ] Bu ay olan olay ya da yakın kaçışlar kaydedildi; rehbere eklenecek ders var mı?
