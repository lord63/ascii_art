#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ascii_art import Bar


def basic():
    """Default settings: default width, bar char, and no sorting."""
    data = {
        "cats": 6,
        "ferrets": 15,
        "dogs": 2,
        "koalas": 0,
    }
    bar = Bar(data)
    print(bar.render())


def sorted_by_value():
    """Sort bars by value descending, with a custom bar char and width."""
    data = {
        "ferrets": 20,
        "cats": 12,
        "dogs": 30,
        "koalas": 3,
    }
    bar = Bar(data, bar_char="=", width=20, sort=True)
    print(bar.render())


def with_map_func():
    """Use map_func to format displayed values (e.g. bytes → human-readable)."""
    def fmt_bytes(n):
        for unit in ("B", "KB", "MB", "GB"):
            if n < 1024:
                return f"{n:.0f} {unit}"
            n /= 1024
        return f"{n:.0f} TB"

    data = {
        "images": 2_400_000_000,
        "videos": 800_000_000,
        "docs":    15_000_000,
        "logs":     3_000_000,
    }
    bar = Bar(data, width=40, sort=True, map_func=fmt_bytes)
    print(bar.render())


if __name__ == "__main__":
    basic()
    sorted_by_value()
    with_map_func()
