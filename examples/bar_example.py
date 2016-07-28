#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from ascii_art.bar import Bar


def example_one():
    data = {
        "cats": 6,
        "ferrets": 15,
        "dogs": 2,
        "koalas": 0
    }
    b = Bar(data)
    print(b.render())


def example_two():
    data = {
        "ferrets": 20,
        "cats": 12,
        "dogs": 30,
        "koalas": 3
    }
    b = Bar(data, bar_char="=", width=20, sort=True)
    print(b.render())


def example_three():
    def transform_money(money):
        if isinstance(money, int):
            str_money = str(money)
            if len(str_money) == 4:
                currency = "thousand"
            elif len(str_money) == 3:
                currency = "hundred"
            else:
                currency = ""
            return "{} {} yuan".format(str_money[0], currency)
        else:
            if "thousand" in money:
                currency = 1000
            elif "hundred" in money:
                currency = 100
            else:
                currency = 1
            num = int(money.split(' ')[0])
            return num * currency

    data = {
        "phone": transform_money("5 thousand yuan"),
        "earphone": transform_money("3 hundred yuan"),
        "apple": transform_money("5 yuan")
    }
    b = Bar(data, bar_char="*", width=40, sort=True, map_func=transform_money)
    print(b.render())


if __name__ == "__main__":
    example_one()
    print("\n")
    example_two()
    print("\n")
    example_three()
