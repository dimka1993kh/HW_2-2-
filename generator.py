import hashlib

def hash_return(path):
    with open(path, 'r', encoding='utf-8') as document:
        for line in document:
            yield hashlib.md5(line.encode())