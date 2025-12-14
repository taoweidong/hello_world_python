"""
Python 函数学习模块
包括函数定义、参数传递、作用域等概念
"""


def basic_function():
    """基本函数定义示例"""
    def greet():
        print("Hello, World!")
    
    print("基本函数:")
    greet()


def function_with_parameters(name, age=18):
    """带参数的函数示例"""
    print(f"带参数函数:")
    print(f"  你好, 我是 {name}, 今年 {age} 岁")


def function_with_return(a, b):
    """带返回值的函数示例"""
    print("带返回值函数:")
    result = a + b
    print(f"  {a} + {b} = {result}")
    return result


def variable_arguments(*args, **kwargs):
    """可变参数函数示例"""
    print("可变参数函数:")
    print(f"  位置参数: {args}")
    print(f"  关键字参数: {kwargs}")


def scope_examples():
    """作用域示例"""
    global_var = "我是全局变量"
    
    def inner_function():
        local_var = "我是局部变量"
        print("作用域示例:")
        print(f"  {global_var}")  # 可以访问全局变量
        print(f"  {local_var}")   # 局部变量
    
    inner_function()
    # print(local_var)  # 这会报错，因为局部变量无法在函数外访问


def lambda_examples():
    """Lambda 表达式示例"""
    # 简单的 lambda 函数
    add = lambda x, y: x + y
    print("Lambda 表达式:")
    print(f"  Lambda 加法: {add(3, 5)}")
    
    # 在高阶函数中使用 lambda
    numbers = [1, 3, 2, 4, 5]
    sorted_numbers = sorted(numbers, key=lambda x: -x)  # 降序排列
    print(f"  降序排列: {sorted_numbers}")


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
    
    print("装饰器示例:")
    say_hello("Python")


def recursive_function(n):
    """递归函数示例"""
    if n <= 1:
        return 1
    return n * recursive_function(n - 1)


def function_annotations(a: int, b: int) -> int:
    """函数注解示例"""
    return a + b


def higher_order_functions():
    """高阶函数示例"""
    # 函数作为参数
    def apply_operation(x, y, operation):
        return operation(x, y)
    
    def add(x, y):
        return x + y
    
    def multiply(x, y):
        return x * y
    
    print("高阶函数:")
    result1 = apply_operation(5, 3, add)
    result2 = apply_operation(5, 3, multiply)
    print(f"  5 + 3 = {result1}")
    print(f"  5 * 3 = {result2}")
    
    # 使用lambda表达式
    result3 = apply_operation(5, 3, lambda x, y: x ** y)
    print(f"  5 ^ 3 = {result3}")


def closure_examples():
    """闭包示例"""
    def outer_function(x):
        def inner_function(y):
            return x + y
        return inner_function
    
    print("闭包示例:")
    add_five = outer_function(5)
    result = add_five(3)
    print(f"  5 + 3 = {result}")


if __name__ == "__main__":
    print("=== 基本函数 ===")
    basic_function()
    
    print("\n=== 带参数函数 ===")
    function_with_parameters("张三")
    function_with_parameters("李四", 25)
    
    print("\n=== 带返回值函数 ===")
    result = function_with_return(10, 20)
    
    print("\n=== 可变参数函数 ===")
    variable_arguments(1, 2, 3, name="张三", age=20)
    
    print("\n=== 作用域 ===")
    scope_examples()
    
    print("\n=== Lambda 表达式 ===")
    lambda_examples()
    
    print("\n=== 装饰器 ===")
    decorator_examples()
    
    print("\n=== 递归函数 ===")
    factorial_5 = recursive_function(5)
    print(f"  5! = {factorial_5}")
    
    print("\n=== 函数注解 ===")
    annotated_result = function_annotations(10, 20)
    print(f"  10 + 20 = {annotated_result}")
    print(f"  函数注解: {function_annotations.__annotations__}")
    
    print("\n=== 高阶函数 ===")
    higher_order_functions()
    
    print("\n=== 闭包 ===")
    closure_examples()