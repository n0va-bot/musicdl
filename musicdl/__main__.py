from sys import argv
from musicdl.download import download
from musicdl.metadata import search

def main():
    url = argv[1]
    title, artist, album = download(url)
    result = search(title, artist, album)
    print(result.title, result.artist, result.album, result.album_artist, result.track_number)

if __name__ == '__main__':
    main()