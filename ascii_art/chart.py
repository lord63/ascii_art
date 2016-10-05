#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Chart:
    def __init__(self, data, width=130, height=30, padding=3,
                 point_char=u'█', negative_point_char=u'░', axis_char=u'.'):
        self.data = data
        self.padding = padding
        self.width = width - padding * 2
        self.height = height - padding * 2
        self.point_char = point_char
        self.negative_point_char = negative_point_char
        self.axis_char = axis_char

    def render(self):
        self._prepare()
        self._draw_skeleton()
        self._draw_y_axis()
        self._draw_x_axis()
        self._plot_data()
        return self.skeleton

    def _prepare(self):
        self.max = max(self.data)
        self.label = str(self.max)
        self.label_width = len(self.label)
        self.label_padding = 1
        self.char_height = self.height
        self.char_width = self.width - self.label_width - self.label_padding

    def _draw_skeleton(self):
        self.skeleton = [[' '] * self.width for _ in range(self.height)]

    def _draw_y_axis(self):
        label_with_padding = self.label_width + self.label_padding
        zero_position = self.label_width - self.label_padding
        for y in range(self.height):
            self.skeleton[y][label_with_padding] = self.axis_char
        self.skeleton[0][:self.label_width] = self.label
        self.skeleton[self.height - 1][zero_position] = '0'

    def _draw_x_axis(self):
        label_with_padding = self.label_width + self.label_padding
        while label_with_padding < self.width - 2:
            self.skeleton[self.height - 1][label_with_padding] = '.'
            label_with_padding += 1
            self.skeleton[self.height - 1][label_with_padding] = ' '
            label_with_padding += 1

    def _plot_data(self):
        x = self.label_width + self.label_padding + 2
        for d in self.data:
            p = d / self.max
            y = round((self.height - 2) * p)
            c = self.negative_point_char if y < 0 else self.point_char
            y = abs(y)
            while y:
                y = y - 1
                self.skeleton[abs(y - self.height) - 2][x] = c
            x = x + 2
        self._add_padding()
        self._matrix_to_string()

    def _matrix_to_string(self):
        self.skeleton = '\n'.join([''.join(line) for line in self.skeleton])

    def _add_padding(self):
        line_width = len(self.skeleton[0])
        blank_line = [' '] * line_width

        # On Y axis.
        self.skeleton.insert(0, blank_line)
        self.skeleton.append(blank_line)

        # On X axis.
        self.skeleton = [[' '] * self.padding + line for line in self.skeleton]
