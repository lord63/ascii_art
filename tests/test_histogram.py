#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def test_histogram_make_bins_values():
    # [0, 5, 10] with bin_num=3:
    # 0  → p=0.0, b=max(0, 0-1)=0
    # 5  → p=0.5, b=max(0, 1-1)=0
    # 10 → p=1.0, b=max(0, 3-1)=2
    h = Histogram([0, 5, 10], bin_num=3)
    bins = h._make_bins()
    assert bins == [2, 0, 1]
    assert sum(bins) == 3


def test_histogram_make_bins_length():
    h = Histogram(list(range(20)), bin_num=10)
    bins = h._make_bins()
    assert len(bins) == 10
    assert sum(bins) == 20


def test_histogram_make_bins_min_always_in_first_bin():
    # The minimum value always lands in bin 0
    h = Histogram([0, 100], bin_num=5)
    bins = h._make_bins()
    assert bins[0] >= 1


def test_histogram_make_bins_max_in_last_bin():
    # The maximum value lands in the last bin
    h = Histogram([0, 100], bin_num=5)
    bins = h._make_bins()
    assert bins[-1] >= 1


def test_histogram_custom_chars():
    data = [1, 2, 3, 4, 5]
    h = Histogram(data, bin_num=3, width=30, height=15,
                  point_char='X', axis_char='|')
    result = h.render()
    assert 'X' in result
    assert '|' in result


def test_histogram_renders_string():
    h = Histogram(list(range(1, 11)), bin_num=5, width=30, height=10)
    result = h.render()
    assert isinstance(result, str)
    assert len(result) > 0
