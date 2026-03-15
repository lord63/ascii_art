#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art import Histogram

DATA = [
    1, 5, 5, 13, 3, 2, 0, 2, 34, 22,
    15, 12, 8, 4, 3, 6, 18, 10, 18, 23,
    17, 4, 5, 6, 3, 12, 10, 7, 17, 30,
    27, 25, 23, 16, 14, 12, 8, 6, 4, 2,
]


def default_bins():
    """Default bin count (50): fine-grained distribution view."""
    histogram = Histogram(DATA)
    print(histogram.render())


def coarse_bins():
    """Fewer bins (10): coarser view, trends stand out more clearly."""
    histogram = Histogram(DATA, bin_num=10, width=80, height=20)
    print(histogram.render())


def fine_bins():
    """More bins (20) with custom size: detailed distribution."""
    histogram = Histogram(DATA, bin_num=20, width=100, height=25)
    print(histogram.render())


if __name__ == "__main__":
    default_bins()
    coarse_bins()
    fine_bins()
