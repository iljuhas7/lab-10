#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "g", "h", "k", "y"}
    b = {"a", "b", "k", "n", "u"}
    c = {"i", "j", "o", "y", "z"}
    d = {"a", "b", "f", "g", "y", "z"}

    x = (a.union(b)).intersection(d)
    print(f"x = {x}")

    an = u.difference(a)
    bn = u.difference(b)
    cn = u.difference(c)

    y = (an.intersection(d)).union(cn.difference(bn))
    print(f"y = {y}")
