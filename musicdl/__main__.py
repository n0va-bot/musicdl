from sys import argv
import musicdl.metadata as metadata

def main():
    url = argv[1]
    print(url)
    result = metadata.search("How do you do (nightcore)")
    import json
    json.dump(result, open("result.json", "w"), indent=4)

if __name__ == '__main__':
    main()