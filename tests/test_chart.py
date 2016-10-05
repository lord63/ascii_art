#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from ascii_art import Chart


def test_chart():
    data = [1, 2, 3, 4]
    chart = Chart(data=data, width=18, height=10, padding=2, point_char='1',
                  negative_point_char='0', axis_char='|')
    expected_output = '\n'.join(
        [
            "                ",
            "  4 |           ",
            "    |       1   ",
            "    |     1 1   ",
            "    |   1 1 1   ",
            "    | 1 1 1 1   ",
            "  0 . . . . .   ",
            "                "
        ]
    )
    assert expected_output == chart.render()
