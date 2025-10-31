import yt_dlp

def download(url: str) -> tuple[str | None, str | None, str | None]:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    ydl = yt_dlp.YoutubeDL(ydl_opts) #type: ignore
    # get data
    info = ydl.extract_info(url, download=False)
    title = info['title'] if 'title' in info else None
    artist = info['creator'] if 'creator' in info else None
    album = None

    # download
    #ydl.download(url)

    return title, artist, album