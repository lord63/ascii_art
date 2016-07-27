#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from ascii_art.bar import Bar


def example_one():
    data = {
        "cats": 6,
        "ferrets": 15,
        "dogs": 12,
        "koalas": 0
    }
    b = Bar(data)
    print(b.render())


if __name__ == "__main__":
    example_one()
