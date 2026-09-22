# YDownload

Download a single YouTube video, or **every video on a channel** (including
members-only / paid videos you have access to), using `yt-dlp`.

## Requirements

- **Python 3.12** (3.9 fails against current YouTube — old LibreSSL fingerprint)
- **Node.js** (for the PO-token server YouTube now requires)
- `ffmpeg` (to merge video+audio)

Check your Python:
```bash
python3.12 --version   # -> Python 3.12.x
```

## Setup

```bash
# venv + deps
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## PO-token server (required by current YouTube)

YouTube now needs a "PO token" or downloads 403. A local Node server provides it.
It was cloned/built to `~/.local/share/bgutil-pot`. Start it (leave it running):

```bash
node ~/.local/share/bgutil-pot/server/build/main.js &
```

Verify: `curl -s http://127.0.0.1:4416/ping` should return JSON.

If that folder is gone (e.g. fresh machine), rebuild it once:
```bash
git clone https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git ~/.local/share/bgutil-pot
cd ~/.local/share/bgutil-pot/server && npm install && npx tsc
```

## Cookies (only for members-only / paid videos)

Public videos need no cookies. For members-only content you must be a member
and provide your logged-in session. Easiest: export `cookies.txt` with the
"Get cookies.txt LOCALLY" browser extension, save it in this folder.
(Refresh it only if you get "Sign in to confirm" errors.)

## Usage

```bash
# single video (public)
.venv/bin/python app.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# entire channel, public videos
.venv/bin/python app.py "https://www.youtube.com/@BenVallack/videos"

# entire channel INCLUDING your members-only/paid videos
COOKIEFILE=cookies.txt .venv/bin/python app.py "https://www.youtube.com/@BenVallack/videos"

# alternatively pull cookies straight from a browser (quit Chrome first):
COOKIES=chrome .venv/bin/python app.py "https://www.youtube.com/@BenVallack/videos"
```

Files download to the current directory. Members-only videos you don't have
access to are skipped; the rest keep downloading.

## Alias (optional)

```bash
alias yd='cd /Users/onyx/dev/YDownload && COOKIEFILE=cookies.txt .venv/bin/python app.py'
```

## Troubleshooting

- **HTTP 403 on download** — PO-token server not running, or old Python/yt-dlp.
  Start the server; run `.venv/bin/pip install -U --pre "yt-dlp[default]"`.
- **"The page needs to be reloaded"** — usually Python 3.9/LibreSSL. Use 3.12.
- **"Join this channel..."** — that video is members-only; supply `cookies.txt`
  from an account that is a member.
