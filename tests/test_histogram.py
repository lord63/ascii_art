#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

from ascii_art import Histogram


def test_histogram():
    histogram = Histogram([1, 2, 1, 3], bin_num=4, width=20, height=10)
    expected_output = '\n'.join(
        [
            '                 ',
            '   2 .           ',
            '     . █         ',
            '     . █ █   █   ',
            '   0 . . . . .   ',
            '                 '
        ]
    )
    assert expected_output == histogram.render()
