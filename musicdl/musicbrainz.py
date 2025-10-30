import musicbrainzngs

musicbrainzngs.set_useragent(
    "MusicDL",
    "0.1",
    "https://git.krzak.org/N0VA/musicdl"
)

def search(title: str, artist: str = None, album: str = None):
    result = musicbrainzngs.search_recordings(
        query=title,
        artist=artist,
        release=album,
        limit=1
    )

    return result