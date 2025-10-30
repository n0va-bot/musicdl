import yt_dlp

def download(url: str):
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
    title = info['title']
    artist = info['creator']
    album = None

    # download
    #ydl.download(url)

    return title, artist, album