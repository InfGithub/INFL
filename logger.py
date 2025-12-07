
from typing import Literal
from time import strftime, localtime

_log_path: str = "latest.log"

with open(_log_path, mode="w+", encoding="utf-8") as log_file:
    log_file.close()

def init(log_path: str = "latest.log"):
    global _log_path
    _log_path = log_path
    with open(log_path, mode="w+", encoding="utf-8") as log_file:
        ...

def log(*texts: object,
        level: Literal["TRACE", "DEBUG", "INFO","WARN", "ERROR", "FATAL"] = "INFO",
        thread: str = "Main", **kwargs) -> tuple[object]:
    global _log_path

    text: str = f"[{strftime("%H:%M:%S", localtime())}] [{thread}/{level\
        }]: {" ".join([t.__str__() for t in texts])}"
    with open(_log_path, mode="a", encoding="utf-8") as log_file:
        log_file.write(text + "\n")

    print(text, **kwargs)
    return texts