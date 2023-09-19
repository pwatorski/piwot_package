

from typing import Any, Dict, List, Tuple, Union


def make_init_arg_strings(name:str, var_type:Union[str, type], value=None, add_value:bool=True, add_self:bool=True, value_as_name:bool=True):
    if type(var_type) != str:
        if type(var_type) == type:
            var_type = var_type.__name__
        else:
            var_type = type(var_type).__name__
    ret_str = f'{name}:{var_type}'
    if value_as_name:
        value = name
    if add_value:
        ret_str += f'={value}'
    if add_self:
        ret_str = 'self.' + ret_str
    return  ret_str

def unpack_attribute(attribute:Union[Union[str, type], Tuple[Union[str, type]]]):
    if type(attribute) == tuple:
        return attribute[0], attribute[1], True
    return attribute, None, False


def make_class_from_attributes(
        class_name:str='new_class', 
        attributes:Dict[str, Union[Union[str, type], Tuple[Union[str, type], Any]]]={}, 
        body_only_attributes:Dict[str, Union[Union[str, type], Tuple[Union[str, type], Any]]]={}, 
        header_only_attributes:Dict[str, Union[Union[str, type], Tuple[Union[str, type], Any]]]={}, 
        header_with_values:bool=True):
    
    header_args = []
    body_args = []

    for k, a in attributes.items():
        t, v, *_ = unpack_attribute(a)
        header_args.append(make_init_arg_strings(k, t, v, add_value=header_with_values, add_self=False))
        body_args.append(make_init_arg_strings(k, t, v, value_as_name=True, add_self=True))
    
    for k, a in body_only_attributes.items():
        t, v, *_ = unpack_attribute(a)
        body_args.append(make_init_arg_strings(k, t, v, value_as_name=False, add_self=True))
    
    for k, a in header_only_attributes.items():
        t, v, *_ = unpack_attribute(a)
        header_args.append(make_init_arg_strings(k, t, v, add_value=header_with_values, add_self=False))

    header_args_str = ', '.join(header_args)
    if len(body_args) == 0:
        body_args = ['\t\tpass']
    body_args_str = '\n'.join(f'\t\t{x}' for x in body_args)

    return f"class {class_name}:\n\tdef __init__(self, {header_args_str}) -> None:\n{body_args_str}"

def body_arg_to_header_arg(body_arg:str, add_equal_null:bool=False):
    pass

def header_args_from_body_args(body_args:str, add_equal_null:bool=False):
    pass