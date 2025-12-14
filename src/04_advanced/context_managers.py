"""
上下文管理器学习模块
"""
import contextlib


class FileHandler:
    """自定义文件处理器 - 上下文管理器"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文"""
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """退出上下文"""
        if self.file:
            print(f"关闭文件: {self.filename}")
            self.file.close()
        
        # 处理异常
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_value}")
            # 返回False表示不抑制异常，True表示抑制异常
            return False
        
        print("文件操作完成，无异常")
        return True


def basic_context_manager():
    """基本上下文管理器使用"""
    # 使用内置的文件上下文管理器
    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write("Hello, Context Manager!")
    
    with open('example.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"文件内容: {content}")
    
    # 清理文件
    import os
    if os.path.exists('example.txt'):
        os.remove('example.txt')


def custom_context_manager():
    """自定义上下文管理器"""
    # 使用自定义的上下文管理器
    with FileHandler('test.txt', 'w') as f:
        f.write("测试自定义上下文管理器")
        # 故意引发异常来测试异常处理
        # raise ValueError("测试异常处理")
    
    # 清理文件
    import os
    if os.path.exists('test.txt'):
        os.remove('test.txt')


@contextlib.contextmanager
def my_context(name):
    """使用contextmanager装饰器创建上下文管理器"""
    print(f"进入上下文: {name}")
    try:
        yield name
    except Exception as e:
        print(f"捕获异常: {e}")
        raise
    finally:
        print(f"退出上下文: {name}")


def decorator_context_manager():
    """装饰器方式的上下文管理器"""
    with my_context("测试上下文") as ctx:
        print(f"在上下文中执行: {ctx}")
    
    # 测试异常处理
    try:
        with my_context("异常测试上下文") as ctx:
            print(f"在上下文中执行: {ctx}")
            raise ValueError("测试异常")
    except ValueError:
        print("异常已被处理")


@contextlib.contextmanager
def suppress_errors(*exceptions):
    """抑制特定异常的上下文管理器"""
    try:
        yield
    except exceptions:
        pass


def suppress_context_manager():
    """异常抑制示例"""
    with suppress_errors(ZeroDivisionError):
        result = 1 / 0
        print(f"这个不会被打印: {result}")
    
    print("即使有除零错误，程序仍继续执行")


if __name__ == "__main__":
    print("=== 基本上下文管理器 ===")
    basic_context_manager()
    
    print("\n=== 自定义上下文管理器 ===")
    custom_context_manager()
    
    print("\n=== 装饰器方式的上下文管理器 ===")
    decorator_context_manager()
    
    print("\n=== 异常抑制上下文管理器 ===")
    suppress_context_manager()