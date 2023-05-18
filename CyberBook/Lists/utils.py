import urllib.parse


def add_null_bytes(traversal_list: list, null_bytes: list):
    return [f"{direct}{null_byte}" for direct in traversal_list for null_byte in null_bytes]


def add_payload(traversal_list: list, payloads: list):
    return [f"{direct}{payload}" for direct in traversal_list for payload in payloads]


def add_web_file(traversal_list: list, web_files: list):
    return [f"{file}/{direct}" for direct in traversal_list for file in web_files]


def full_url_encoder(unencoded: str | list):

    def encoder(plain_text: str) -> str:
        url_encode = urllib.parse.quote(plain_text)
        return url_encode.replace('.', '%2E')

    if isinstance(unencoded, str):
        return encoder(plain_text=unencoded)

    return [encoder(plain_text=traverse) for traverse in unencoded]
