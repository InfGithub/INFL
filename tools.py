
import os, json
from functools import wraps
from time import time
from itertools import product


def timer(func):

    """装饰器：简易计时"""

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

    """修改字符串"""

    old_string = str(old_string)
    new_string = old_string[:index] + char + old_string[index+1:]
    return new_string

def iteration_list(list_: list, index: list):

    """递归对列表取值"""
    """print(iteration_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [2, 3]))"""
    """echo: 6"""

    return iteration_list(list_[index[0]], index[1:]) if isinstance(list_[index[0]], list) else list_[index[0]]

def generate_combinations(limits):

    """生成所有可能的组合列表"""
    """When limits = [2, 3]"""
    """[[0,0], [0,1], [0,2],
        [1,0], [1,1], [1,2]]"""

    return [list(comb) for comb in product(*[range(lim) for lim in limits])]

def file_prefix(path: str, text: str):

    """路径下文件增加前缀"""

    info: tuple = list(os.walk(os.path.normpath(path)))[0]
    
    for name in info[2]:
        os.rename(os.path.join(info[0], name), os.path.join(info[0], text+name))

def file_suffix(path: str, text: str):

    """路径下文件修改后缀"""

    info: tuple = list(os.walk(os.path.normpath(path)))[0]
    
    for name in info[2]:
        os.rename(os.path.join(info[0], name), os.path.join(info[0], "".join([os.path.splitext(name)[0], "" if ("." in text) or (text == "") else ".", text])))

def compare(v1: str, v2: str, eq: bool=False):
    """版本号大小比较，eq：是否在相等时返回True"""
    v1: list[int] = [int(i) for i in v1.split(".")]
    v2: list[int] = [int(i) for i in v2.split(".")]

    len_v1: int = len(v1)
    len_v2: int = len(v2)

    max_len: int = max(len_v1, len_v2)
    v1 += [0] * (max_len - len_v1)
    v2 += [0] * (max_len - len_v2)

    if v1==v2:
        return eq

    for a, b in zip(v1, v2):
        if a > b:
            return True
        if a < b:
            return False


def int_to_bin(number: int, path: str) -> None:
    """将整数转换为二进制文件并保存到指定路径。

    number: int - 要转换的整数

    path: str - 保存二进制文件的路径
    """
    number_bytes: int = (number.bit_length() + 7) // 8
    byte_data: bytes = number.to_bytes(number_bytes, 'big')
    with open(path, "wb") as file:
        file.write(byte_data)

def bin_to_int(path: str) -> int:
    """从二进制文件读取整数并返回该整数。
    
    path: str - 二进制文件的路径"""
    with open(path, "rb") as file:
        byte_data = file.read()
    return int.from_bytes(byte_data, 'big')