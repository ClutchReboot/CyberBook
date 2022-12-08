import os

"""
File System Magic
"""


def find(name, path, file_type: str = None):
    if file_type not in ['file', 'dir', None]:
        raise ValueError(f"input 'file_type' should be of value 'file', 'dir' or 'None'.")

    for root, dirs, files in os.walk(path):
        if file_type == 'file':
            if name in files:
                return os.path.join(root, name)
        elif file_type == 'dir':
            if name in dirs:
                return os.path.join(root, name)
        else:
            if name in dirs or name in files:
                return os.path.join(root, name)


def find_all(name, path, file_type: str = None):
    result = []
    if file_type not in ['file', 'dir', None]:
        raise ValueError(f"input 'file_type' should be of value 'file', 'dir' or 'None'.")

    for root, dirs, files in os.walk(path):
        if file_type == 'file':
            if name in files:
                result.append(os.path.join(root, name))
        elif file_type == 'dir':
            if name in dirs:
                result.append(os.path.join(root, name))
        else:
            if name in dirs or name in files:
                result.append(os.path.join(root, name))
    return result


def read_wordlist(file: str, wordlist: list = None):
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
