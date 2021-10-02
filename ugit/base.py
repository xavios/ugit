import os

from . import data


def write_tree(directory='.'):
    with os.scandir(directory) as curr_dir:
        for item in curr_dir:
            item_full_path = f'{directory}/{item.name}'
            if is_ignored(item_full_path):
                continue
            elif item.is_file(follow_symlinks=False):
                print(item_full_path)
            elif item.is_dir(follow_symlinks=False):
                write_tree(item_full_path)


def is_ignored(path):
    return '.ugit' in path.split('/')
