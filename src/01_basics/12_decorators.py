"""
Python 装饰器学习模块
包括装饰器的定义、使用和自定义装饰器
"""
import functools
import time


def basic_decorator():
    """基本装饰器"""
    print("基本装饰器:")
    
    def my_decorator(func):
        def wrapper():
            print("  函数执行前")
            func()
            print("  函数执行后")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("  Hello, World!")
    
    say_hello()


def decorator_with_parameters():
    """带参数的装饰器"""
    print("\n带参数的装饰器:")
    
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"  调用函数 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"  函数 {func.__name__} 执行完毕")
            return result
        return wrapper
    
    @my_decorator
    def greet(name, greeting="Hello"):
        print(f"  {greeting}, {name}!")
        return f"{greeting}, {name}!"
    
    result = greet("张三", greeting="你好")
    print(f"  返回值: {result}")


def functools_wraps_example():
    """functools.wraps示例"""
    print("\nfunctools.wraps示例:")
    
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  装饰器增强: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    @my_decorator
    def example_function():
        """这是一个示例函数"""
        print("  示例函数执行")
    
    example_function()
    print(f"  函数名: {example_function.__name__}")
    print(f"  函数文档: {example_function.__doc__}")


def timer_decorator():
    """计时装饰器"""
    print("\n计时装饰器:")
    
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"  {func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    @timer
    def slow_function():
        time.sleep(0.1)  # 模拟耗时操作
        return "完成"
    
    result = slow_function()
    print(f"  函数结果: {result}")


def retry_decorator():
    """重试装饰器"""
    print("\n重试装饰器:")
    
    def retry(max_attempts=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise e
                        print(f"  第{attempt + 1}次尝试失败: {e}")
                        time.sleep(0.1)
                return None
            return wrapper
        return decorator
    
    @retry(max_attempts=3)
    def unreliable_function():
        import random
        if random.random() < 0.7:  # 70%概率失败
            raise Exception("随机失败")
        return "成功"
    
    try:
        result = unreliable_function()
        print(f"  函数结果: {result}")
    except Exception as e:
        print(f"  最终失败: {e}")


def class_decorator():
    """类装饰器"""
    print("\n类装饰器:")
    
    class CountCalls:
        def __init__(self, func):
            self.func = func
            self.count = 0
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"  函数 {self.func.__name__} 被调用了 {self.count} 次")
            return self.func(*args, **kwargs)
    
    @CountCalls
    def say_hi():
        print("  Hi!")
    
    say_hi()
    say_hi()
    say_hi()


def property_decorator():
    """property装饰器"""
    print("\nproperty装饰器:")
    
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            """半径属性"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value < 0:
                raise ValueError("半径不能为负数")
            self._radius = value
        
        @property
        def area(self):
            """计算面积"""
            return 3.14159 * self._radius ** 2
    
    circle = Circle(5)
    print(f"  半径: {circle.radius}")
    print(f"  面积: {circle.area:.2f}")
    
    circle.radius = 10
    print(f"  新半径: {circle.radius}")
    print(f"  新面积: {circle.area:.2f}")


def multiple_decorators():
    """多个装饰器"""
    print("\n多个装饰器:")
    
    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<b>{result}</b>"
        return wrapper
    
    def italic(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<i>{result}</i>"
        return wrapper
    
    @bold
    @italic
    def get_text():
        return "Hello World"
    
    result = get_text()
    print(f"  装饰结果: {result}")
    print("  注意装饰器的应用顺序是从下到上")


def decorator_factory():
    """装饰器工厂"""
    print("\n装饰器工厂:")
    
    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(3)
    def greet(name):
        print(f"  Hello, {name}!")
    
    greet("Python")


def practical_examples():
    """实用示例"""
    print("\n实用示例:")
    
    # 缓存装饰器
    def memoize(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                print(f"  缓存命中: {args}")
                return cache[args]
            result = func(*args)
            cache[args] = result
            print(f"  计算并缓存: {args}")
            return result
        return wrapper
    
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("  斐波那契数列计算:")
    result = fibonacci(10)
    print(f"  fibonacci(10) = {result}")


if __name__ == "__main__":
    print("=== Python 装饰器 ===")
    basic_decorator()
    decorator_with_parameters()
    functools_wraps_example()
    timer_decorator()
    retry_decorator()
    class_decorator()
    property_decorator()
    multiple_decorators()
    decorator_factory()
    practical_examples()