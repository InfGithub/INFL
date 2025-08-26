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

def split_string(s: str, k: int) -> list[str]:
    """
    分割字符串。

    Args:
        s (str): 原始字符串。
        k (int): 分割长度。

    Returns:
        list[str]: 分割后的字符串列表。

    Example:
        >>> split_string("helloworld", 3)
        ["h", "ell", "owo", "rld"]
    """
    if len(s) % k != 0:
        morelens: int = len(s) % k
        return [s[:morelens], *split_string(s[morelens:], 4)]
    if len(s) >= k:
        return [s[i: i+k] for i in range(0, len(s), k)]
    return list()

class chinese_number:
    """
    中文数字类。

    请调用其中的方法。
    """

    basic_numbers: list[str] = [
        "零", "一", "二", "三", "四",
        "五", "六", "七", "八", "九"
    ]
    unit_numbers: list[str] = [
        "", "万", "亿",
        "兆", "京", "垓", "秭",
        "穰", "沟", "涧", "正",
        "载", "极", "恒河沙", "阿僧祇",
        "那由他", "不可思议", "无量", "大数",
        "不可说", "不可计", "不可称", "不可量"
    ]
    else_units: dict[str, str] = {
        "minus": "负",
        "point": "点",
        "zero": "零",
        "one": "一",
        "ten": "十",
        "hundred": "百",
        "thousand": "千",
    }
    unit_numbers_uppercase: dict[int, str] = {
        "一": "壹", "二": "贰",
        "三": "叁", "四": "肆",
        "五": "伍", "六": "陆",
        "七": "柒", "八": "捌",
        "九": "玖", "十": "拾",
        "百": "佰", "千": "仟",
        "万": "萬","亿": "億"
    }


    def party(part: str) -> str:
        """
        处理四位数字。

        Args:
            part (str): 四位数字。

        Returns:
            str: 处理后的字符串。

        Example:
            >>> party("1234")
            "一千二百三十四"
        """
        need_zero: bool = False
        result: str = str()
        part = part.zfill(4)

        for i, n in enumerate(part):
            if n != "0":
                if need_zero:
                    result += chinese_number.else_units["zero"]
                    need_zero = False
                if i == 2 and n == "1":
                    if result == "":
                        result += chinese_number.else_units["ten"]
                    else:
                        result += chinese_number.basic_numbers[int(n)] + chinese_number.else_units["ten"]
                else:
                    result += chinese_number.basic_numbers[int(n)]
                    if i != 3:
                        match i:
                            case 0:
                                result += chinese_number.else_units["thousand"]
                            case 1:
                                result += chinese_number.else_units["hundred"]
                            case 2:
                                result += chinese_number.else_units["ten"]
            else:
                if result != "":
                    if part[i:].count("0") < len(part[i:]):
                        need_zero = True
        return result

    def number_to_chinese(number: str) -> str:
        """
        将数字转换为中文。

        Args:
            number (str): 数字。

        Returns:
            str: 转换后的字符串。

        Example:
            >>> number_to_chinese("1234567890")
            "一千二百三十四万五千六百七十八九"
        """

        if number[0] == "-":
            return chinese_number.else_units["minus"] + chinese_number.number_to_chinese(number[1:])
        
        if "." in number:
            parts = number.split(".")
            return chinese_number.number_to_chinese(parts[0]) + chinese_number.else_units["point"] + "".join([chinese_number.basic_numbers[int(i)] for i in parts[1]])
        
        splited_number: list[str] = split_string(number, 4)
        len_splited_number: int = len(splited_number)
        result: str = "".join([chinese_number.party(item) + chinese_number.unit_numbers[len_splited_number - i - 1] for i, item in enumerate(splited_number)])
        return result

    def uppercase(number: str) -> str:
        """
        将数字转换为大写。

        Args:
            number (str): 数字。

        Returns:
            str: 转换后的字符串。

        Example:
            >>> uppercase("一千二百三十四万五千六百七十八九")
            "壹仟贰佰叁拾肆万伍仟陆佰柒拾捌玖"
        """
        return "".join([chinese_number.unit_numbers_uppercase[i] for i in number])