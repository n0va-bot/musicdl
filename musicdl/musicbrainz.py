import musicbrainzngs
from musicdl.song import Song

musicbrainzngs.set_useragent(
    "MusicDL",
    "0.1",
    "https://git.krzak.org/N0VA/musicdl"
)

def search(title: str | None, artist: str | None = None, album: str | None = None) -> Song:
    result = musicbrainzngs.search_recordings(
        query=title,
        artist=artist,
        release=album,
        limit=1
    )

    title: str = result['recording-list'][0]['title']
    artist: str = result['recording-list'][0]['artist-credit'][0]['artist']['name']
    album: str = result['recording-list'][0]['release-list'][0]['title']
    album_artist: str = result['recording-list'][0]['release-list'][0]['artist-credit'][0]['artist']['name']
    track_number = 0

    for track in result['recording-list'][0]['release-list'][0]["medium-list"][0]["track-list"]:
        if track["title"] == title:
            track_number = track['number']
            break
    
    return Song(title, artist, album, album_artist, track_number)