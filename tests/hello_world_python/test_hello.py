# -*- coding: utf-8 -*-
"""Test hello"""
import unittest
from unittest.mock import patch

from hello_world_python.hello import Hello


class TestHello(unittest.TestCase):
    """Test Hello类的功能"""

    def test_init_sets_name_property(self):
        """
        TC001：验证当提供普通字符串时，name属性是否正确设置
        给定：一个名称字符串"John"
        当：创建Hello实例时
        则：实例的name属性应等于给定的名称
        """
        name = "John"
        hello = Hello(name)
        self.assertEqual(hello.name, name)

    @patch('hello_world_python.hello.print')
    def test_say_hello_outputs_correct_message(self, mock_print):
        """
        TC002：验证打印输出是否正确格式化
        给定：一个名称"John"
        当：调用say_hello方法
        则：应打印"hello, John"
        """
        name = "John"
        expected_output = f'hello, {name}'

        hello = Hello(name)
        hello.say_hello()

        mock_print.assert_called_once_with(expected_output)

    def test_add_returns_sum_of_two_positive_integers(self):
        """
        TC003：验证正整数相加是否正确
        给定：a=2, b=3
        当：调用add方法
        则：应返回5
        """
        result = Hello.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_returns_sum_of_two_negative_integers(self):
        """
        TC004：验证负整数相加是否正确
        给定：a=-2, b=-3
        当：调用add方法
        则：应返回-5
        """
        result = Hello.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_returns_correct_sum_when_one_is_positive_and_the_other_is_negative_1(self):
        """
        TC005：验证正负相加是否正确（结果为正）
        给定：a=5, b=-2
        当：调用add方法
        则：应返回3
        """
        result = Hello.add(5, -2)
        self.assertEqual(result, 3)

    def test_add_returns_correct_sum_when_one_is_positive_and_the_other_is_negative_2(self):
        """
        TC006：验证正负相加是否正确（结果为负）
        给定：a=2, b=-5
        当：调用add方法
        则：应返回-3
        """
        result = Hello.add(2, -5)
        self.assertEqual(result, -3)

    def test_add_returns_correct_sum_when_both_are_zero(self):
        """
        TC007：验证零相加是否正确
        给定：a=0, b=0
        当：调用add方法
        则：应返回0
        """
        result = Hello.add(0, 0)
        self.assertEqual(result, 0)
