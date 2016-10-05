#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter


class Bar:
    def __init__(self, data, width=60, bar_char='#', sort=False,
                 map_func=lambda x: x):
        self.data = data
        self.width = width
        self.bar_char = bar_char
        self.sort = sort
        self.map_func = map_func
        self._prepare_data()

    def _prepare_data(self):
        self.max_key_len = max([len(key) for key in self.data.keys()])
        self.max_val = max(self.data.values())
        self.items = self.data.items()
        if self.sort:
            self.items = sorted(self.items, key=itemgetter(1), reverse=True)

    def render(self):
        result = ''
        for k, v in self.items:
            p = v / self.max_val
            shown = round(self.width * p)
            shown = shown + 1 if shown == 0 and v != 0 else shown
            blank = self.width - shown
            bar = self.bar_char * (shown) + ' ' * (blank)
            result += "{:>{}s} | {} | {}\n".format(
                k, self.max_key_len, bar, self.map_func(v)
            )
        return '\n' + result
