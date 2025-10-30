def download(url: str):
    if "youtu" in url:
        from musicdl.youtube import download
        return download(url)