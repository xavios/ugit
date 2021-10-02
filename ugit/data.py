import os
import hashlib

GIT_DIR = '.ugit'
TYPE_CONTENT_SEPARATOR = b'\x00'


def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data, type_='blob'):
    object = type_.encode() + TYPE_CONTENT_SEPARATOR + data
    oid = hashlib.sha1(object).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(object)
    return oid


def get_object(oid, expected='blob'):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        object = f.read()
    type_, _, content = object.partition(TYPE_CONTENT_SEPARATOR)
    type_ = type_.decode()
    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content
