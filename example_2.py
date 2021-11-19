#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = set(input("Введите первую строку: "))
    B = set(input("Введите вторую строку: "))

    print(f"A = {A}")
    print(f"B = {B}")

    print(f"A & B = {A & B}")
    print(f"A - B = {A - B}")
    print(f"A ^ B = {A ^ B}")
