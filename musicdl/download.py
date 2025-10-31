def download(url: str) -> tuple[str | None, str | None, str | None]:
    if "youtu" in url:
        from musicdl.youtube import download
        return download(url)
    

    return None, None, None