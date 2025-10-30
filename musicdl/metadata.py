import musicdl.musicbrainz as musicbrainz

def search(title: str, artist: str = None, album: str = None):
    results = musicbrainz.search(title, artist, album)

    return results