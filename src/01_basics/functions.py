"""
函数学习模块
包括函数定义、参数传递、作用域等概念
"""


def basic_function():
    """基本函数定义示例"""
    def greet():
        print("Hello, World!")
    
    greet()


def function_with_parameters(name, age=18):
    """带参数的函数示例"""
    print(f"你好, 我是 {name}, 今年 {age} 岁")


def function_with_return(a, b):
    """带返回值的函数示例"""
    return a + b


def variable_arguments(*args, **kwargs):
    """可变参数函数示例"""
    print("位置参数:", args)
    print("关键字参数:", kwargs)


def scope_examples():
    """作用域示例"""
    global_var = "我是全局变量"
    
    def inner_function():
        local_var = "我是局部变量"
        print(global_var)  # 可以访问全局变量
        print(local_var)   # 局部变量
    
    inner_function()
    # print(local_var)  # 这会报错，因为局部变量无法在函数外访问


def lambda_examples():
    """Lambda 表达式示例"""
    # 简单的 lambda 函数
    add = lambda x, y: x + y
    print(f"Lambda 加法: {add(3, 5)}")
    
    # 在高阶函数中使用 lambda
    numbers = [1, 3, 2, 4, 5]
    sorted_numbers = sorted(numbers, key=lambda x: -x)  # 降序排列
    print(f"降序排列: {sorted_numbers}")


def decorator_examples():
    """装饰器示例"""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("函数执行前")
            result = func(*args, **kwargs)
            print("函数执行后")
            return result
        return wrapper
    
    @my_decorator
    def say_hello(name):
        print(f"Hello, {name}!")
    
    say_hello("Python")


if __name__ == "__main__":
    print("=== 基本函数 ===")
    basic_function()
    
    print("\n=== 带参数函数 ===")
    function_with_parameters("张三")
    function_with_parameters("李四", 25)
    
    print("\n=== 带返回值函数 ===")
    result = function_with_return(10, 20)
    print(f"加法结果: {result}")
    
    print("\n=== 可变参数函数 ===")
    variable_arguments(1, 2, 3, name="张三", age=20)
    
    print("\n=== 作用域 ===")
    scope_examples()
    
    print("\n=== Lambda 表达式 ===")
    lambda_examples()
    
    print("\n=== 装饰器 ===")
    decorator_examples()