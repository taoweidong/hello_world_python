"""
单元测试学习模块
"""
import unittest


def add(a, b):
    """加法函数"""
    return a + b


def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


class Calculator:
    """计算器类"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def get_history(self):
        """获取历史记录"""
        return self.history.copy()


class TestAddFunction(unittest.TestCase):
    """测试加法函数"""
    
    def test_positive_numbers(self):
        """测试正数相加"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_negative_numbers(self):
        """测试负数相加"""
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-5, 3), -2)
    
    def test_zero(self):
        """测试与零相加"""
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)


class TestDivideFunction(unittest.TestCase):
    """测试除法函数"""
    
    def test_normal_division(self):
        """测试正常除法"""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 3), 2.333333, places=5)
    
    def test_division_by_zero(self):
        """测试除零异常"""
        with self.assertRaises(ValueError):
            divide(10, 0)
        
        # 另一种写法
        with self.assertRaisesRegex(ValueError, "除数不能为零"):
            divide(5, 0)


class TestCalculator(unittest.TestCase):
    """测试计算器类"""
    
    def setUp(self):
        """每个测试方法执行前调用"""
        self.calc = Calculator()
    
    def tearDown(self):
        """每个测试方法执行后调用"""
        # 清理工作（如果需要）
        pass
    
    def test_add(self):
        """测试加法"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        self.assertIn("2 + 3 = 5", self.calc.get_history())
    
    def test_subtract(self):
        """测试减法"""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
        self.assertIn("5 - 3 = 2", self.calc.get_history())
    
    def test_history(self):
        """测试历史记录"""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("1 + 2 = 3", history)
        self.assertIn("5 - 3 = 2", history)


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    suite = unittest.TestSuite()
    
    # 添加测试用例
    suite.addTest(unittest.makeSuite(TestAddFunction))
    suite.addTest(unittest.makeSuite(TestDivideFunction))
    suite.addTest(unittest.makeSuite(TestCalculator))
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    # 运行测试
    run_tests()