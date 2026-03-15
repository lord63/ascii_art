#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def test_chart_with_negative_values():
    data = [1, -4]
    chart = Chart(data=data, width=18, height=10, padding=2, point_char='1',
                  negative_point_char='0', axis_char='|')
    expected_output = '\n'.join(
        [
            "                ",
            "  4 |           ",
            "    |   0       ",
            "    |   0       ",
            "    |   0       ",
            "    | 1 0       ",
            "  0 . . . . .   ",
            "                "
        ]
    )
    assert expected_output == chart.render()


def test_chart_with_all_negative_values():
    data = [-1, -4]
    chart = Chart(data=data, width=18, height=10, padding=2, point_char='1',
                  negative_point_char='0', axis_char='|')
    expected_output = '\n'.join(
        [
            "                ",
            "  4 |           ",
            "    |   0       ",
            "    |   0       ",
            "    |   0       ",
            "    | 0 0       ",
            "  0 . . . . .   ",
            "                "
        ]
    )
    assert expected_output == chart.render()
