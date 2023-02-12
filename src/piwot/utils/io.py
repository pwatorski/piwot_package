import io
import json
import os
from typing import List, Union
from collections.abc import Iterable
import typing
from piwot.utils.time import get_timestamp_simple

def check_file_dir(path:str, extention:str='.txt'):
    if not path:
        path = './'
    if os.path.isdir(path):
        path = os.path.join(path, f'{get_timestamp_simple(long=True)}{extention}')
    else:
        directory, file_name = os.path.split(path)
        if directory and directory != './':
            os.makedirs(directory, exist_ok=True)
    return path

def read_txt(path:str, encoding:str='utf8'):
    with open(path, 'r', encoding=encoding) as fi:
        return fi.read()

def write_txt(data:Union[str, typing.Iterable[str]], path:str, add_new_line:bool=False, encoding:str='utf8'):
    path = check_file_dir(path, extention='.txt')
    with open(path, 'w', encoding=encoding) as fo:
        if isinstance(data, str):
            fo.write(data)
        if isinstance(data, Iterable):
            if add_new_line:
                fo.writelines(f'{x}\n' for x in data)
            else:
                fo.writelines(str(x) for x in data)
        else:
            fo.write(f'{data}')

def read_json(path:str, encoding:str='utf8', as_str:bool=False):
    with open(path, 'r', encoding=encoding) as fi:
        if as_str:
            return json.loads(fi)
        return json.load(fi)

def write_json(data, path:str=None, encoding:str='utf8', indent:int=4, to_str:bool=False):
    path = check_file_dir(path, extention='.json')
    if to_str:
        return json.dumps(data, indent=indent)

    with open(path, 'w', encoding=encoding) as fo:
        json.dump(data, fo, indent=indent)

def listdir_fast(dir_path:str):
    if not dir_path:
        dir_path = './'
    return [os.path.join(dir_path, x) for x in os.listdir(dir_path)]

def get_newest_file_in_dir(dir_path:str):
    if not dir_path:
        dir_path = './'
    return max([os.path.join(dir_path, x) for x in os.listdir(dir_path)], key=os.path.getctime)

def listdir(dir_path:str, no_dirs:bool=False, no_files:bool=False, sort_mode:str='none', reverse:bool=False)-> List[str]:
    """Lists a provided directory.

    Args:
        dir_path (str): Directory to list.
        no_dirs (bool, optional): Excludes directories. Defaults to False.
        no_files (bool, optional): Excludes files. Defaults to False.
        sort_mode (str, optional): Possible modes: 'none', 'size', 'time', 'alpha'. Defaults to 'none'.
        reverse (bool, optional): Reverses the result. Defaults to False.

    Returns:
        List[str]: Full paths of objects in the specified directory.
    """

    if not dir_path:
        dir_path = './'

    path_gen = (os.path.join(dir_path, x) for x in os.listdir(dir_path))

    paths = (p for p in path_gen if (not no_dirs and os.path.isdir(p)) or (not no_files and os.path.isfile(p)))
    sort_mode = sort_mode.lower()
    if sort_mode == 'time':
        return sorted(paths, key=os.path.getctime, reverse=reverse)
    
    if sort_mode == 'size':
        return sorted(paths, key=os.path.getsize, reverse=reverse)
    
    if sort_mode == 'alpha':
        return sorted(paths, reverse=reverse)
        
    if reverse:
        return list(reversed(paths))
    return list(paths)