# 10. Platform başvuru kartı

[← İçindekiler](../README.md)

Rehberin farklı bölümlerinde geçen kontrollerin Windows, macOS ve Linux karşılıkları tek yerde. Buradaki **bütün komutlar yalnız okur**; hiçbir şeyi silmez, değiştirmez ya da durdurmaz. Yine de çalıştırmadan önce ne yaptığını okuyun.

> Komutlar Kasım 2026 itibarıyla güncel işletim sistemi sürümleri için yazıldı. Linux'taki `systemctl`, `ls` ve `sha256sum` komutları bir test ortamında denendi; `ss` (iproute2 paketi) ve `crontab` o ortamda kurulu değildi, çoğu masaüstü dağıtımında varsayılan olarak gelir. Windows ve macOS komutları yalnız sözdizimi olarak kontrol edildi; hata görürseniz [bildirin](../CONTRIBUTING.md).

---

## 10.1 Hangi platformda ne var?

| | Windows | macOS | Linux | WSL2 |
|---|---|---|---|---|
| Yerleşik zararlı yazılım koruması | Microsoft Defender (geçmişi görülebilir) | XProtect (arka planda, kullanıcıya geçmiş göstermez) | Yok (kurulması gerekir) | Windows tarafındaki Defender |
| Claude Code sandbox | Yok (WSL2 kullanın) | Var | Var (`bubblewrap`, `socat`) | Var |
| Claude Code kimlik bilgisi | `%USERPROFILE%\.claude\.credentials.json` | Anahtar Zinciri | `~/.claude/.credentials.json` | `~/.claude/.credentials.json` (WSL içinde) |
| VS Code eklenti klasörü | `%USERPROFILE%\.vscode\extensions` | `~/.vscode/extensions` | `~/.vscode/extensions` | Uzak eklentiler `~/.vscode-server/extensions` |

**macOS ve Linux kullanıcıları için not:** Vakamızda dokuz gün boyunca uyarı veren Defender'ın bu platformlarda doğrudan bir karşılığı yok. Bu, "Mac'e virüs bulaşmaz" demek değildir; Ağustos 2026'daki Claude oturum hırsızlığında Mac'leri hedef alan bir bilgi hırsızı (Atomic Stealer) da vardı. Bu platformlarda [Bölüm 1](01-kurmadan-once.md)'deki kurulum disiplini ve aşağıdaki açılış öğesi kontrolleri daha da önemlidir.

## 10.2 Kurulu editör eklentilerini listeleme

Bütün platformlarda aynı:

```bash
code --list-extensions --show-versions
# Cursor için:
cursor --list-extensions --show-versions
```

Çıktıyı [onaylı listeyle](../sablonlar/onayli-araclar.md) karşılaştırın. Bir eklentinin ne zaman kurulduğunu görmek için eklenti klasöründeki dizinlerin tarihlerine bakın (yukarıdaki tablo).

## 10.3 Açılışta çalışanlar (kalıcılık)

Zararlı yazılım bilgisayar yeniden başladığında da çalışmak için kendini buralara yazar.

**Windows (PowerShell):**

```powershell
# Başlangıçta çalışan komutlar
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User
# Run anahtarları
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run','HKLM:\Software\Microsoft\Windows\CurrentVersion\Run' -ErrorAction SilentlyContinue
# Microsoft dışı zamanlanmış görevler
Get-ScheduledTask | Where-Object { $_.TaskPath -notlike '\Microsoft\*' } | Select-Object TaskName, TaskPath, State
```

**macOS (Terminal):**

```bash
ls -la ~/Library/LaunchAgents /Library/LaunchAgents /Library/LaunchDaemons
launchctl list | grep -v com.apple
# Oturum açma öğeleri ve arka plan öğeleri (macOS 13+). DİKKAT: yönetici şifresi ister;
# yalnız AYLIK KONTROLDE kullanın, ele geçirilmiş şüphesi olan bilgisayarda şifre yazmayın.
# sudo sfltool dumpbtm
crontab -l
```

**Linux:**

```bash
systemctl --user list-unit-files --state=enabled
ls -la ~/.config/autostart /etc/xdg/autostart 2>/dev/null
crontab -l 2>/dev/null
ls -la /etc/cron.d /etc/cron.daily 2>/dev/null
```

Ayrıca bütün platformlarda kabuk başlangıç dosyalarına bakın: `~/.bashrc`, `~/.zshrc`, `~/.profile`, `~/.zprofile`; Windows'ta `$PROFILE`.

## 10.4 Dışarıya açık bağlantılar

```powershell
# Windows
Get-NetTCPConnection -State Established | Select-Object LocalPort, RemoteAddress, RemotePort, OwningProcess, @{n='Process';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

```bash
# macOS
lsof -nP -i -sTCP:ESTABLISHED
# Linux
ss -tunap
```

## 10.5 Güvenlik aracının geçmişi

```powershell
# Windows: Defender'ın son tespitleri ve durumu
Get-MpThreatDetection | Sort-Object InitialDetectionTime -Descending | Select-Object -First 20 InitialDetectionTime, ThreatID, Resources
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
```

Grafik arayüzde: Windows Güvenliği → Virüs ve tehdit koruması → Koruma geçmişi.

macOS ve Linux'ta ek bir güvenlik aracı kurduysanız onun kendi geçmiş ekranına bakın.

## 10.6 Dosya hash'i

```powershell
Get-FileHash .\dosya -Algorithm SHA256       # Windows
```

```bash
shasum -a 256 dosya                          # macOS
sha256sum dosya                              # Linux
```

---

**İlgili:** [Bölüm 1.6 Kurduktan sonra](01-kurmadan-once.md) · [Bölüm 3 adli inceleme istemleri](03-claude-ile-adli-inceleme.md) · [Aylık kontrol](../kontrol-listeleri/aylik-kontrol.md)
