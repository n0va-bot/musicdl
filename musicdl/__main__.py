from sys import argv
from musicdl.download import download
from musicdl.metadata import search

def main():
    url = argv[1]
    title, artist, album = download(url)
    results = search(title, artist, album)

if __name__ == '__main__':
    main()