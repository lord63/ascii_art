#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art import Bar


def test_bar_sorted():
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


def test_bar_no_sort():
    # Insertion order is preserved when sort=False (default)
    data = {"b": 5, "a": 10}
    bar = Bar(data, width=10, bar_char="=")
    result = bar.render()
    lines = [l for l in result.split('\n') if l.strip()]
    assert lines[0].strip().startswith('b')
    assert lines[1].strip().startswith('a')


def test_bar_with_map_func():
    data = {"a": 100, "b": 50}
    bar = Bar(data, width=10, map_func=lambda x: f"${x}")
    result = bar.render()
    assert "$100" in result
    assert "$50" in result


def test_bar_zero_value():
    # A value of 0 should render an empty bar (no bar chars)
    data = {"a": 10, "b": 0}
    bar = Bar(data, width=10, bar_char="#")
    result = bar.render()
    b_line = [l for l in result.split('\n') if ' b |' in l or 'b |' in l][0]
    bar_section = b_line.split('|')[1]
    assert '#' not in bar_section


def test_bar_small_value_guard():
    # When a nonzero value rounds to 0 bars, it must show at least 1 bar char.
    # width=10, max=100, tiny=4 → p=0.04, round(0.4)=0 → guard triggers → shown=1
    data = {"big": 100, "tiny": 4}
    bar = Bar(data, width=10, bar_char="#")
    result = bar.render()
    tiny_line = [l for l in result.split('\n') if 'tiny |' in l][0]
    bar_section = tiny_line.split('|')[1]
    assert '#' in bar_section


def test_bar_custom_bar_char():
    data = {"x": 10}
    bar = Bar(data, width=5, bar_char="*")
    result = bar.render()
    assert "x | ***** | 10" in result


def test_bar_single_item():
    data = {"only": 42}
    bar = Bar(data, width=8, bar_char="-")
    result = bar.render()
    assert "only | -------- | 42" in result
