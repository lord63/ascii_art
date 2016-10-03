#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import

from ascii_art.chart import Chart


class Histogram(object):
    def __init__(self, data, bin_num=50):
        self.data = data
        self.bin_num = bin_num

    def render(self):
        bins = self._make_bins()
        return Chart(bins).render()

    def _make_bins(self):
        max_data = max(self.data)
        min_data = min(self.data)
        bins = [0] * self.bin_num
        for i in self.data:
            p = (i - min_data) / (max_data - min_data)
            b = max(0, (int(self.bin_num * p) ^ 0) - 1)
            bins[b] = bins[b] + 1
        return bins
