
from random import choice
from time import strftime, localtime

def cat() -> str:

    """生成随机猫猫表情"""

    cats: list = [
        "=^..^=",
        "(=｀ェ´=)",
        "/ᐠ｡ꞈ｡ᐟ\\",
        "ฅ^•ﻌ•^ฅ",
        "(=◉ᆽ◉=)",
        "≽ܫ≼",
        "₍˄·͈༝·͈˄₎",
    ]

    text = " 喵~"

    return choice(cats) + text

def music_disc() -> str:

    """获得随机MC唱片"""
    
    discs: list = [
        "C418 - 13",
        "C418 - cat",
        "C418 - blocks",
        "C418 - chirp",
        "C418 - far",
        "C418 - mall",
        "C418 - mellohi",
        "C418 - stal",
        "C418 - strad",
        "C418 - ward",
        "C418 - 11",
        "C418 - wait",
        "Lena Raine - Pigstep",
        "Lena Raine - otherside",
        "Samuel Åberg - 5",
        "Aaron Cherof - Relic",
        "Aaron Cherof - Precipice",
        "Lena Raine - Creator",
        "Lena Raine - Creator(Music Box)",
        "Amos Roddy - Tears"
    ]

    get_disc: str = choice(discs)
    text: str = ""

    if get_disc == "Lena Raine - otherside":
        text = "（音乐之声！————用唱片机的音乐声为草甸增添生机。）"

    return get_disc + text


def __helloinit__():
    print(f"Hello, Infinitive!  Time: {strftime("%Y-%m-%d %X", localtime())}")

