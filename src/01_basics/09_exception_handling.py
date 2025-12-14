"""
Python 异常处理学习模块
包括异常的捕获、处理和自定义异常
"""
import traceback


def basic_exception_handling():
    """基本异常处理"""
    print("基本异常处理:")
    
    # 捕获特定异常
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("  捕获到除零错误")
    
    # 捕获多种异常
    try:
        value = int("abc")
    except ValueError:
        print("  捕获到值错误")
    except TypeError:
        print("  捕获到类型错误")
    
    # 捕获所有异常
    try:
        # 一些可能出错的代码
        result = 10 / 0
    except Exception as e:
        print(f"  捕获到异常: {e}")


def exception_with_else_finally():
    """带else和finally的异常处理"""
    print("\n带else和finally的异常处理:")
    
    try:
        number = int("123")
    except ValueError:
        print("  发生值错误")
    else:
        print(f"  没有异常，转换结果: {number}")
    finally:
        print("  finally块总是会执行")
    
    # 有异常的情况
    try:
        number = int("abc")
    except ValueError:
        print("  发生值错误")
    else:
        print(f"  没有异常，转换结果: {number}")
    finally:
        print("  finally块总是会执行")


def raising_exceptions():
    """抛出异常"""
    print("\n抛出异常:")
    
    def validate_age(age):
        if age < 0:
            raise ValueError("年龄不能为负数")
        if age > 150:
            raise ValueError("年龄不能超过150")
        return True
    
    try:
        validate_age(-5)
    except ValueError as e:
        print(f"  抛出异常: {e}")
    
    try:
        validate_age(200)
    except ValueError as e:
        print(f"  抛出异常: {e}")


def custom_exceptions():
    """自定义异常"""
    print("\n自定义异常:")
    
    class CustomError(Exception):
        """自定义异常类"""
        def __init__(self, message, error_code=None):
            super().__init__(message)
            self.error_code = error_code
    
    def process_data(data):
        if not data:
            raise CustomError("数据不能为空", error_code=1001)
        if len(data) > 100:
            raise CustomError("数据量过大", error_code=1002)
        return len(data)
    
    # 测试自定义异常
    try:
        result = process_data([])
    except CustomError as e:
        print(f"  自定义错误: {e}, 错误代码: {e.error_code}")
    
    try:
        result = process_data(list(range(150)))
    except CustomError as e:
        print(f"  自定义错误: {e}, 错误代码: {e.error_code}")


def exception_hierarchy():
    """异常层次结构"""
    print("\n异常层次结构:")
    print("  BaseException")
    print("   +-- SystemExit")
    print("   +-- KeyboardInterrupt")
    print("   +-- GeneratorExit")
    print("   +-- Exception")
    print("        +-- StopIteration")
    print("        +-- ArithmeticError")
    print("        |    +-- FloatingPointError")
    print("        |    +-- OverflowError")
    print("        |    +-- ZeroDivisionError")
    print("        +-- AttributeError")
    print("        +-- LookupError")
    print("        |    +-- IndexError")
    print("        |    +-- KeyError")
    print("        +-- ValueError")
    print("        +-- TypeError")
    print("        +-- ...")


def traceback_examples():
    """追踪异常"""
    print("\n追踪异常:")
    
    def function_a():
        function_b()
    
    def function_b():
        function_c()
    
    def function_c():
        raise ValueError("在function_c中发生的错误")
    
    try:
        function_a()
    except ValueError:
        print("  捕获到异常，打印追踪信息:")
        traceback.print_exc()


def assert_examples():
    """断言示例"""
    print("\n断言示例:")
    
    def divide(a, b):
        assert b != 0, "除数不能为零"
        return a / b
    
    try:
        result = divide(10, 2)
        print(f"  10 / 2 = {result}")
    except AssertionError as e:
        print(f"  断言失败: {e}")
    
    try:
        result = divide(10, 0)
        print(f"  10 / 0 = {result}")
    except AssertionError as e:
        print(f"  断言失败: {e}")


def context_manager_for_exceptions():
    """使用上下文管理器处理异常"""
    print("\n使用上下文管理器处理异常:")
    
    class ExceptionHandler:
        def __enter__(self):
            print("  进入上下文")
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is not None:
                print(f"  捕获到异常: {exc_type.__name__}: {exc_value}")
                return True  # 抑制异常
            return False  # 不抑制异常
    
    with ExceptionHandler():
        print("  在上下文中执行正常代码")
    
    with ExceptionHandler():
        print("  在上下文中执行异常代码")
        raise ValueError("测试异常")


def best_practices():
    """异常处理最佳实践"""
    print("\n异常处理最佳实践:")
    print("  1. 只捕获你能够处理的异常")
    print("  2. 避免捕获所有异常，除非你知道自己在做什么")
    print("  3. 使用具体的异常类型而不是通用的Exception")
    print("  4. 记录异常信息以便调试")
    print("  5. 不要忽略异常（空的except块）")
    print("  6. 使用finally块清理资源")
    print("  7. 自定义异常应该继承自合适的内置异常类")


if __name__ == "__main__":
    print("=== Python 异常处理 ===")
    basic_exception_handling()
    exception_with_else_finally()
    raising_exceptions()
    custom_exceptions()
    exception_hierarchy()
    traceback_examples()
    assert_examples()
    context_manager_for_exceptions()
    best_practices()