import musicbrainzngs

musicbrainzngs.set_useragent(
    "MusicDL",
    "0.1",
    "https://git.krzak.org/N0VA/musicdl"
)

def search(title: str, artist: str = None, album: str = None):
    result = musicbrainzngs.search_recordings(
        f"track:({title}) artist:({artist}) release:({album})",
        1
    )["recording-list"][0]

    result = musicbrainzngs.get_recording_by_id(result["id"])

    return result