#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art import Bar


def test_bar():
    data = {
        "cats": 6,
        "ferrets": 15,
        "dogs": 2,
    }
    bar = Bar(data, bar_char="=", width=20, sort=True)
    expected_output = '\n'.join(
        [
            '',
            'ferrets | ==================== | 15',
            '   cats | ========             | 6',
            '   dogs | ===                  | 2',
            ''
        ]
    )
    assert expected_output == bar.render()
