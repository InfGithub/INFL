
import os, json, zipfile
from functools import wraps
from time import time
from itertools import product
from io import BytesIO
from . import translate


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



def json_translate(path: str, output_path: str, source_lang: str = "en", target_lang: str = "zh", model: str = "deepseek-r1:14b", temperature: int = 0.3, encoding="utf-8", max_context: int = 20, abouttext: str = None):
    """翻译json值对"""

    path = os.path.abspath(path)
    output_path = os.path.join(os.path.abspath(output_path), os.path.basename(path))

    with open(path, "r+", encoding=encoding) as file:
        data: dict = json.load(file)

    data_items = data.items()
    data_length: int = len(data_items)
    for index, [key, value] in enumerate(data_items):
        print(f"进度：{index+1}/{data_length} | 当前翻译条目：{key}")
        
        data[key] = translate.translate(text=value,
                                        source_lang=source_lang, target_lang=target_lang, model=model, temperature=temperature, max_context=max_context, abouttext=abouttext)
        print(f"-"*96)
    with open(output_path, "w+", encoding=encoding) as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))
