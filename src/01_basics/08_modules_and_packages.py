"""
Python 模块与包学习模块
包括模块导入、包结构、标准库使用等概念
"""
import math
import random
import datetime
import os
import sys


def module_basics():
    """模块基础"""
    print("模块基础:")
    print(f"  数学模块 PI: {math.pi}")
    print(f"  数学模块 sqrt(16): {math.sqrt(16)}")
    print(f"  随机模块 randint(1, 10): {random.randint(1, 10)}")
    
    # 当前日期时间
    now = datetime.datetime.now()
    print(f"  当前时间: {now}")


def importing_techniques():
    """导入技巧"""
    print("\n导入技巧:")
    
    # 1. 导入整个模块
    import math
    print(f"  import math: {math.cos(0)}")
    
    # 2. 导入模块并给它一个别名
    import math as m
    print(f"  import math as m: {m.cos(0)}")
    
    # 3. 从模块中导入特定函数
    from math import sin
    print(f"  from math import sin: {sin(0)}")
    
    # 4. 从模块中导入特定函数并给它一个别名
    from math import cos as cosine
    print(f"  from math import cos as cosine: {cosine(0)}")
    
    # 5. 导入模块中的所有内容（不推荐）
    from math import *
    print(f"  from math import *: {tan(0)}")


def standard_library_examples():
    """标准库示例"""
    print("\n标准库示例:")
    
    # 数学运算
    print("  数学运算:")
    print(f"    ceil(4.2): {math.ceil(4.2)}")
    print(f"    floor(4.8): {math.floor(4.8)}")
    print(f"    fabs(-10): {math.fabs(-10)}")
    print(f"    pow(2, 3): {math.pow(2, 3)}")
    print(f"    log(10): {math.log(10)}")
    
    # 随机数
    print("  随机数:")
    print(f"    random(): {random.random()}")  # 0-1之间的随机数
    print(f"    randint(1, 10): {random.randint(1, 10)}")
    print(f"    choice([1, 2, 3, 4, 5]): {random.choice([1, 2, 3, 4, 5])}")
    
    # 日期时间
    print("  日期时间:")
    today = datetime.date.today()
    print(f"    今天: {today}")
    now = datetime.datetime.now()
    print(f"    现在: {now}")
    print(f"    格式化时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 系统相关
    print("  系统相关:")
    print(f"    Python版本: {sys.version}")
    print(f"    平台: {sys.platform}")
    print(f"    当前工作目录: {os.getcwd()}")


def creating_modules():
    """创建模块"""
    print("\n创建模块:")
    print("  模块就是一个包含Python代码的.py文件")
    print("  模块可以包含函数、类、变量和可执行语句")
    print("  使用 import 语句导入模块")
    print("  模块首次导入时会被执行")


def package_structure():
    """包结构"""
    print("\n包结构:")
    print("  包是一种组织模块的方式")
    print("  包就是一个包含 __init__.py 文件的目录")
    print("  可以使用点号(.)来访问包中的模块")
    print("  例如: import package.module")


def sys_path_examples():
    """sys.path示例"""
    print("\nsys.path示例:")
    print("  Python会在sys.path列出的目录中查找模块")
    for i, path in enumerate(sys.path[:3]):  # 只显示前3个路径
        print(f"    {i+1}. {path}")
    print("    ...")


def module_searching():
    """模块搜索"""
    print("\n模块搜索:")
    print("  Python按照以下顺序搜索模块:")
    print("  1. 当前目录")
    print("  2. PYTHONPATH环境变量指定的目录")
    print("  3. 标准库目录")
    print("  4. 第三方库目录")


def reload_module():
    """重新加载模块"""
    print("\n重新加载模块:")
    print("  importlib.reload() 可以重新加载已导入的模块")
    print("  主要用于开发过程中，当模块被修改后需要重新加载时")


def main():
    """主函数"""
    print("=== Python 模块与包 ===")
    module_basics()
    importing_techniques()
    standard_library_examples()
    creating_modules()
    package_structure()
    sys_path_examples()
    module_searching()
    reload_module()


if __name__ == "__main__":
    main()