import musicdl.musicbrainz as musicbrainz
import musicdl.song as Song

def search(title: str | None, artist: str | None = None, album: str | None = None) -> Song:
    results = musicbrainz.search(title, artist, album)

    return results