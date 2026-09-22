import sys
import yt_dlp

# Downloads a single video, or every video on a channel/playlist.
# For members-only / paid videos, pass --cookies-from-browser via COOKIES env,
# e.g. COOKIES=chrome  (yt-dlp uses your logged-in session).
def download(link: str):
    opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'ignoreerrors': True,  # keep going if one paid/blocked video fails
    }
    import os
    if os.environ.get('COOKIES'):
        opts['cookiesfrombrowser'] = (os.environ['COOKIES'],)
    if os.environ.get('COOKIEFILE'):
        opts['cookiefile'] = os.environ['COOKIEFILE']
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([link])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        download(sys.argv[1])
    else:
        print('No link')
