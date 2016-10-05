#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art.chart import Chart


class Histogram:
    def __init__(self, data, bin_num=50, width=130, height=30, padding=3,
                 point_char=u'█', negative_point_char=u'░', axis_char=u'.'):
        self.data = data
        self.bin_num = bin_num
        self.padding = padding
        self.width = width
        self.height = height
        self.point_char = point_char
        self.negative_point_char = negative_point_char
        self.axis_char = axis_char

    def render(self):
        bins = self._make_bins()
        chart = Chart(bins, self.width, self.height, self.padding,
                      self.point_char, self.negative_point_char,
                      self.axis_char)
        return chart.render()

    def _make_bins(self):
        max_data = max(self.data)
        min_data = min(self.data)
        bins = [0] * self.bin_num
        for i in self.data:
            p = (i - min_data) / (max_data - min_data)
            b = max(0, (int(self.bin_num * p) ^ 0) - 1)
            bins[b] = bins[b] + 1
        return bins
