#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 3


if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "h", "m", "o", "r"}
    b = {"j", "k", "o", "u", "y"}
    c = {"g", "h", "j"}
    d = {"g", "j", "g"}

    x = (a.intersection(c)).union(d.intersection(b))
    print(f"x = {x}")

    y = (a.intersection(b)).union(d.difference(c))
    print(f"y = {y}")
