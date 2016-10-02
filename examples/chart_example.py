#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from ascii_art.chart import Chart


def example_one():
    data = [
        1, 5, 5, 13, 3, 2, 0, 2, 34, 22,
        15, 12, 8, 4, 3, 6, 18, -5, -15, -11,
        -23, -3, 10, 18, 23, 17, 4, 5, 6, 3,
        12, 10, 7, -4, 17, 30, 27, 25, 23, 16,
        14, 12, 8, 6, 4, 2
    ]
    c = Chart(data)
    print(c.render())


if __name__ == "__main__":
    example_one()
