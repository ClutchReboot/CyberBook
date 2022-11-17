import os


def read_wordlist(file=None, wordlist: list = None):
    """
    Quick way to load a new wordlist from a file.
    :param file: Wordlist location
    :param wordlist: Append file contents to existing wordlist.
    :return: List of words
    """

    if not wordlist:
        wordlist = []

    if file and not os.path.isfile(file):
        raise FileNotFoundError(f"Cannot locate file {file}. Please ensure it exists.")

    with open(file, 'r') as f:
        for file_line in f:
            # skip line if starts with a comment
            if file_line.startswith("#"):
                continue
            wordlist.append(file_line.strip())
    return wordlist
