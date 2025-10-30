class Song():
    def __init__(
            self,
            title: str,
            artist: str,
            album: str,
            album_artist: str,
            track_number: str,
            cover: str
            ) -> None:

        self.title = title
        self.artist = artist
        self.album = album
        self.album_artist = album_artist
        self.track_number = track_number
        self.cover = cover