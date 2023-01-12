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

def list_dir(dir_path:str):
    return [os.path.join(dir_path, x) for x in os.listdir(dir_path)]