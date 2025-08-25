import os
from functools import wraps
from itertools import product
from time import time
from typing import Hashable, TypeAlias, Union
IndexOrKey: TypeAlias = Union[int, Hashable]

def timer(func):
    """
    简易装饰器函数。

    该函数用于测量被装饰函数的执行时间。

    Args:
        func (callable): 要被测量执行时间的函数。
    
    Returns:
        callable: 被装饰后的函数。

    Example:
        >>> @timer
        ... def my_function():
        ...     pass
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

def rep(old_string: str, char: str, index: int) -> str:
    """
    字符串替换函数。

    该函数用于替换字符串中指定位置的字符。

    Args:
        old_string (str): 原始字符串。
        char (str): 要替换的字符。
        index (int): 要替换的字符的位置。

    Returns:
        str: 替换后的字符串。

    Example:
        >>> rep("hello", "x", 1)
        "hxllo"
    """

    old_string = str(old_string)
    new_string = old_string[:index] + char + old_string[index+1:]
    return new_string

def recursion_dict(value: Union[list, dict], path: IndexOrKey):
    """
    递归访问列表或字典。

    该函数用于递归访问列表或字典中的元素。

    Args:
        value (Union[list, dict]): 要访问的列表或字典。
        path (IndexOrKey): 要访问的元素的路径。

    Returns:
        Union[list, dict]: 访问到的元素。

    Example:
        >>> recursion_list_dict([1, 2, [3, 4]], 2)
        [3, 4]
    """
    return recursion_dict(value[path[0]], path[1:]) if len(path) > 1 else value[path[0]]

def generate_combinations(limits):
    """
    生成所有可能的组合。

    Args:
        limits (list): 每个维度的上限。

    Returns:
        list: 所有可能的组合。

    Example:
        >>> generate_combinations([2, 3])
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
    """

    return [list(comb) for comb in product(*[range(lim) for lim in limits])]

def file_prefix(path: str, text: str):
    """
    指定目录下文件添加前缀。

    Args:
        path (str): 目录路径。
        text (str): 前缀文本。

    Returns:
        None

    Example:
        >>> file_prefix("C:/Users/Admin/Desktop", "prefix_")
    """

    info: tuple = list(os.walk(os.path.normpath(path)))[0]
    
    for name in info[2]:
        os.rename(os.path.join(info[0], name), os.path.join(info[0], text+name))

def file_suffix(path: str, text: str):
    """
    指定目录下文件添加后缀。
    
    Args:
        path (str): 目录路径。
        text (str): 后缀文本。
        
    Returns:
        None
        
    Example:
        >>> file_suffix("C:/Users/Admin/Desktop", ".txt")
    """

    info: tuple = list(os.walk(os.path.normpath(path)))[0]
    
    for name in info[2]:
        os.rename(os.path.join(info[0], name), os.path.join(info[0], "".join([os.path.splitext(name)[0], "" if ("." in text) or (text == "") else ".", text])))

def int_to_bin(number: int, path: str) -> None:
    """
    将整数转换为二进制文件。

    Args:
        number (int): 要转换的整数。
        path (str): 二进制文件的路径。
    
    Returns:
        None

    Example:
        >>> int_to_bin(123456789, "C:/Users/Admin/Desktop/number.bin")
    """
    number_bytes: int = (number.bit_length() + 7) // 8
    byte_data: bytes = number.to_bytes(number_bytes, 'big')
    with open(path, "wb") as file:
        file.write(byte_data)

def bin_to_int(path: str) -> int:
    """
    将二进制文件转换为整数。
    
    Args:
        path (str): 二进制文件的路径。
        
    Returns:
        int: 转换后的整数。
        
    Example:
        >>> bin_to_int("C:/Users/Admin/Desktop/number.bin
        123456789
    """

    with open(path, "rb") as file:
        byte_data = file.read()
    return int.from_bytes(byte_data, 'big')

def replace(string: str, raw: str, rep: str) -> str:
    """
    替换字符串中的子字符串。
    Args:
        string (str): 原始字符串。
        raw (str): 要替换的子字符串。
        rep (str): 替换后的子字符串。

    Returns:
        str: 替换后的字符串。

    Example:
        >>> replace("hello world", "world", "python")
        "hello python"
    """

    if not raw:
        return string
    
    result: list = list()
    start: int = 0
    len_string: int = len(string)
    len_raw: int = len(raw)
    
    while start < len_string:
        pos = string.find(raw, start)
        if pos == -1:
            result.append(string[start:])
            break
        result.append(string[start:pos])
        result.append(rep)
        start = pos + len_raw
    return "".join(result)