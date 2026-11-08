#!/usr/bin/env python3
"""Claude Code için örnek PreToolUse güvenlik kapısı.

Bash araç çağrılarını çalışmadan önce kontrol eder. Riskli bir kalıp görürse
çağrıyı engeller (çıkış kodu 2) ve nedenini stderr üzerinden Claude'a bildirir.

Bu bir güvenlik duvarı değil, ikinci bir göz: kalıp listesi atlatılabilir.
Asıl sınır sandbox ve izin kurallarıdır. Ayrıntı: docs/04-claude-code-sertlestirme.md

Kurulum (.claude/settings.json):
  "hooks": {
    "PreToolUse": [
      {"matcher": "Bash",
       "hooks": [{"type": "command",
                  "command": "python3 \\"$CLAUDE_PROJECT_DIR/.claude/hooks/guvenlik_kapisi.py\\""}]}
    ]
  }

Elle test:
  echo '{"tool_name":"Bash","tool_input":{"command":"cat .env"}}' | python3 guvenlik_kapisi.py; echo $?
"""
import json
import re
import sys

# (düzenli ifade, Claude'a gösterilecek açıklama)
KURALLAR = [
    (r"(^|[\s/'\"])\.env(?!\.(example|sample|template)\b)(\.[\w-]+)?($|[\s'\"])",
     ".env dosyalarına dokunulmaz (.env.example hariç). Gerekli değişken adını kullanıcıya sor."),
    (r"(id_rsa|id_ed25519|\.ssh/|\.aws/credentials|\.credentials\.json|~/\.npmrc|\$HOME/\.npmrc|\.pypirc)",
     "Kimlik bilgisi dosyalarına erişim engellendi."),
    (r"(curl|wget|iwr|Invoke-WebRequest)[^|;&]*\|\s*(sudo\s+)?(sh|bash|zsh|python3?|iex|Invoke-Expression)\b",
     "İnternetten indirilen bir betik doğrudan çalıştırılamaz. Önce indirip kullanıcıya göster."),
    (r"base64\s+(-d|--decode)[^|;&]*\|\s*(sh|bash|zsh|python3?)\b",
     "Base64 çözülüp doğrudan çalıştırılan komutlar engellendi."),
    (r"\bgit\s+push\b.*(--force\b|-f\b|--force-with-lease\b)",
     "Zorla push engellendi. Kullanıcıdan açık onay iste."),
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f[a-zA-Z]*\s+(/|~|\$HOME)(\s|$)",
     "Kök ya da ev klasörünü silen komut engellendi."),
    (r"\b(printenv|env)\b\s*($|\|)",
     "Bütün ortam değişkenlerini dökmek sırları açığa çıkarabilir. Yalnız gereken değişkeni sor."),
    (r"\bgit\s+(commit|push)\b.*--no-verify\b",
     "Pre-commit/pre-push kontrollerini atlamak engellendi. Kontrolün neden başarısız olduğunu açıkla."),
]


def main() -> int:
    try:
        veri = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Girdi okunamazsa engelle: korumanın sessizce devre dışı kalmasındansa iyidir.
        print("Güvenlik kapısı girdiyi okuyamadı; komut engellendi.", file=sys.stderr)
        return 2

    if veri.get("tool_name") != "Bash":
        return 0
    komut = (veri.get("tool_input") or {}).get("command", "")

    for desen, aciklama in KURALLAR:
        if re.search(desen, komut, flags=re.IGNORECASE):
            print(f"Engellendi: {aciklama}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
