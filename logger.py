from typing import Literal
from time import strftime, localtime

log_path: str = "latest.log"
log_level: str = "INFO"

levels: list[str] = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
type LevelType = Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]

levels_value: dict[str, int] = {l: i for i, l in enumerate(levels)}
file_handle = open(log_path, mode="a", encoding="utf-8", buffering=1)

def log(*texts: object,
        level: LevelType = "INFO",
        thread: str = "Main", **kwargs) -> None:

    if levels_value[level] < levels_value[log_level]:
        return

    info: str = " ".join([t.__str__() for t in texts])
    text: str = f"[{strftime("%H:%M:%S", localtime())}] [{thread}/{level}]: {info}"
    file_handle.write(text + "\n")

    print(text, **kwargs)