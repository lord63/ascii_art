#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art import Chart


def positive_values():
    """Chart with only positive values using default settings."""
    data = [
        1, 3, 6, 10, 15, 21, 18, 14, 9, 5,
        2, 4, 8, 13, 20, 25, 22, 17, 11, 6,
        3, 7, 12, 18, 24, 28, 26, 20, 13, 7,
    ]
    chart = Chart(data)
    print(chart.render())


def with_negative_values():
    """Chart with mixed positive and negative values, and custom appearance."""
    data = [
        1, 5, 5, 13, 3, 2, 0, 2, 34, 22,
        15, 12, 8, 4, 3, 6, 18, -5, -15, -11,
        -23, -3, 10, 18, 23, 17, 4, 5, 6, 3,
        12, 10, 7, -4, 17, 30, 27, 25, 23, 16,
        14, 12, 8, 6, 4, 2,
    ]
    chart = Chart(data, width=120, height=40, padding=2,
                  point_char='█', negative_point_char='░', axis_char='|')
    print(chart.render())


if __name__ == "__main__":
    positive_values()
    with_negative_values()
