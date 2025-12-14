"""
Python 基本语法学习模块
包括Python的基本语法规则、缩进、注释等基础知识
"""


def python_syntax_overview():
    """Python语法概述"""
    print("Python语法特点:")
    print("1. 使用缩进来表示代码块，而不是大括号{}")
    print("2. 每行一条语句，不需要分号结尾")
    print("3. 大小写敏感")
    print("4. 以#开头的行是注释")


def indentation_example():
    """缩进示例"""
    print("缩进示例:")
    x = 10
    if x > 5:
        print("  x 大于 5")
        if x > 8:
            print("    x 也大于 8")
    else:
        print("  x 小于等于 5")
    
    # 正确的缩进方式
    print("正确缩进:")
    for i in range(3):
        print(f"  循环第 {i} 次")


def comments_example():
    """注释示例"""
    # 这是一个单行注释
    print("这是代码行")
    
    """
    这是一个多行注释
    可以跨越多行
    通常用于文档字符串
    """
    
    '''
    这也是多行注释
    使用三个单引号
    '''


def naming_conventions():
    """命名约定"""
    print("Python命名约定:")
    print("1. 变量名: snake_case (小写字母和下划线)")
    print("2. 常量名: UPPER_CASE (大写字母和下划线)")
    print("3. 类名: PascalCase (每个单词首字母大写)")
    print("4. 函数名: snake_case (小写字母和下划线)")
    print("5. 私有成员: _开头")
    print("6. 特殊方法: __开头和结尾 (如 __init__)")


def line_continuation():
    """行连接"""
    # 使用反斜杠连接行
    long_string = "这是一个很长的字符串，为了代码可读性，" + \
                  "我们将其分成多行书写"
    print(long_string)
    
    # 在括号内自动连接
    numbers = (1 + 2 + 3 +
               4 + 5 + 6)
    print(f"numbers = {numbers}")
    
    # 列表也可以自动连接
    items = [
        "苹果",
        "香蕉", 
        "橙子"
    ]
    print(f"items = {items}")


if __name__ == "__main__":
    print("=== Python基本语法 ===")
    python_syntax_overview()
    print("\n=== 缩进示例 ===")
    indentation_example()
    print("\n=== 注释示例 ===")
    comments_example()
    print("\n=== 命名约定 ===")
    naming_conventions()
    print("\n=== 行连接 ===")
    line_continuation()