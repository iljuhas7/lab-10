#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sl = "аоиеёэыуюя"
    su = sl.upper()
    g = set(sl + su)

    while True:
        i = 0
        text = input("Введит текст: ")

        for pro in g:
            i = i + text.count(pro)

        print(i)
