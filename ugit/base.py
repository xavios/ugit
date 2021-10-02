import os

from . import data


def write_tree(directory='.'):
    with os.scandir(directory) as curr_dir:
        entries = []
        for item in curr_dir:
            item_full_path = f'{directory}/{item.name}'
            if is_ignored(item_full_path):
                continue
            elif item.is_file(follow_symlinks=False):
                type_ = 'blob'
                with open(item, 'rb') as file:
                    oid = data.hash_object(file.read())
            elif item.is_dir(follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree(item_full_path)
            entries.append((item.name, oid, type_))
    branch = ''.join(f'{type_} {oid} {name}\n'
                     for name, oid, type_
                     in sorted(entries))
    return data.hash_object(branch.encode(), 'tree')


def is_ignored(path):
    return '.ugit' in path.split('/')
