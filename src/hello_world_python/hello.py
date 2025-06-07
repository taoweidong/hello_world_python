# -*- coding: utf-8 -*-
"""Test hello"""


class Hello:
    """hello"""

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """
        say hello
        """
        print('hello, %s' % self.name)

    @classmethod
    def add(cls, a: int, b: int) -> int:
        return a + b
