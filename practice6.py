import datetime
import re
from collections import Counter
from typing import Any, Union


def safe_pawns(pawns: set[str]) -> int:
    safe_count = 0
    for pawn in pawns:
        forward_pawn1 = chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1)
        forward_pawn2 = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)
        if forward_pawn1 in pawns or forward_pawn2 in pawns:
            safe_count += 1
    return safe_count


def sun_angle(time: str) -> Union[float, str]:
    time_list = time.split(":")
    hour = int(time_list[0].lstrip("0"))
    min = int(time_list[1])
    if hour >= 18 and min >= 1 or hour < 6:
        return "I don't see the sun!"
    return round((hour - 6) * 15, 1) + min * 0.25


def split_list(items: list[int]) -> list[list[Any]]:
    return (
        [items[: len(items) // 2], items[len(items) // 2 :]]
        if len(items) % 2 == 0
        else [items[: (len(items) + 1) // 2], items[(len(items) + 1) // 2 :]]
    )


def all_the_same(elements: list[Any]) -> bool:
    return len(Counter(elements)) <= 1


def date_time(time: str) -> str:
    date_list = [int(i) for i in re.split("[. :]", time)]
    print(date_list)
    date = datetime.datetime(
        year=date_list[2],
        month=date_list[1],
        day=date_list[0],
    )
    return f"{date_list[0]} {date.strftime('%B')} {date_list[2]} year {date_list[3]} {'hours'if date_list[3] != 1 else 'hour'} {date_list[4]} {'minutes'if date_list[4] != 1 else 'minute'}"


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str):
    words = code.split("   ")
    result: list[str] = []
    appended_word = ""
    words_list_2d = [word.split(" ") for word in words]

    for word_list in words_list_2d:
        for word in word_list:
            appended_word += MORSE[word]
        result.append(appended_word)
        appended_word = ""

    return " ".join(result).capitalize()


def words_order(text: str, words: list[str]) -> bool:
    word_list = text.split()
    result_list: list[str] = []
    for i in range(len(word_list)):
        if word_list[i] in words and not word_list[i] in result_list:
            result_list.append(word_list[i])
    return result_list == words if words[0] != words[-1] or len(words) == 1 else False


if __name__ == "__main__":
    print(
        words_order("hi world world im here hi world world im here", ["world", "here"])
    )
