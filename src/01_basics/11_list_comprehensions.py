"""
Python 列表推导式学习模块
包括列表推导式、字典推导式、集合推导式等
"""


def list_comprehensions():
    """列表推导式"""
    print("列表推导式:")
    
    # 基本列表推导式
    squares = [x**2 for x in range(10)]
    print(f"  平方数列表: {squares}")
    
    # 带条件的列表推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"  偶数的平方: {even_squares}")
    
    # 使用if-else的列表推导式
    even_odd_labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(10)]
    print(f"  奇偶标签: {even_odd_labels}")
    
    # 嵌套列表推导式
    matrix = [[i*3 + j for j in range(1, 4)] for i in range(3)]
    print(f"  3x3矩阵: {matrix}")
    
    # 展平嵌套列表
    flattened = [num for row in matrix for num in row]
    print(f"  展平后的矩阵: {flattened}")


def dict_comprehensions():
    """字典推导式"""
    print("\n字典推导式:")
    
    # 基本字典推导式
    square_dict = {x: x**2 for x in range(5)}
    print(f"  平方数字典: {square_dict}")
    
    # 带条件的字典推导式
    even_square_dict = {x: x**2 for x in range(10) if x % 2 == 0}
    print(f"  偶数平方字典: {even_square_dict}")
    
    # 从列表创建字典
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    dict_from_lists = {k: v for k, v in zip(keys, values)}
    print(f"  从列表创建字典: {dict_from_lists}")
    
    # 反转字典
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    reversed_dict = {v: k for k, v in original_dict.items()}
    print(f"  反转字典: {reversed_dict}")


def set_comprehensions():
    """集合推导式"""
    print("\n集合推导式:")
    
    # 基本集合推导式
    squares_set = {x**2 for x in range(10)}
    print(f"  平方数集合: {squares_set}")
    
    # 带条件的集合推导式
    odd_set = {x for x in range(20) if x % 2 == 1}
    print(f"  奇数集合: {odd_set}")
    
    # 从字符串创建集合
    unique_chars = {char for char in "hello world"}
    print(f"  字符串唯一字符: {unique_chars}")


def nested_comprehensions():
    """嵌套推导式"""
    print("\n嵌套推导式:")
    
    # 创建二维列表
    matrix_2d = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"  乘法矩阵: {matrix_2d}")
    
    # 复杂的嵌套推导式
    words = ["hello", "world", "python"]
    # 获取所有单词中长度大于2的字符
    chars = [char for word in words for char in word if len(word) > 2]
    print(f"  长单词中的字符: {chars}")


def comparison_with_traditional_loops():
    """与传统循环的比较"""
    print("\n与传统循环的比较:")
    
    # 传统方式创建列表
    squares_traditional = []
    for x in range(10):
        squares_traditional.append(x**2)
    print(f"  传统方式: {squares_traditional}")
    
    # 推导式方式
    squares_comprehension = [x**2 for x in range(10)]
    print(f"  推导式方式: {squares_comprehension}")
    
    # 传统方式过滤列表
    even_squares_traditional = []
    for x in range(10):
        if x % 2 == 0:
            even_squares_traditional.append(x**2)
    print(f"  传统过滤: {even_squares_traditional}")
    
    # 推导式过滤方式
    even_squares_comprehension = [x**2 for x in range(10) if x % 2 == 0]
    print(f"  推导式过滤: {even_squares_comprehension}")


def performance_considerations():
    """性能考虑"""
    print("\n性能考虑:")
    print("  1. 推导式通常比等效的循环更快")
    print("  2. 推导式的可读性更好，特别是对于简单的操作")
    print("  3. 对于复杂逻辑，传统循环可能更清晰")
    print("  4. 推导式会一次性创建整个列表，对于大数据集可能占用较多内存")


def advanced_examples():
    """高级示例"""
    print("\n高级示例:")
    
    # 条件表达式与推导式结合
    numbers = [-4, -2, 0, 2, 4]
    processed = [x if x >= 0 else -x for x in numbers]
    print(f"  处理后的数字: {processed}")
    
    # 使用函数的推导式
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in range(2, 30) if is_prime(x)]
    print(f"  30以内的质数: {primes}")
    
    # 复杂数据结构处理
    students = [
        {"name": "张三", "age": 20, "score": 85},
        {"name": "李四", "age": 22, "score": 92},
        {"name": "王五", "age": 19, "score": 78}
    ]
    
    # 获取高分学生姓名
    high_scorers = [student["name"] for student in students if student["score"] > 80]
    print(f"  高分学生: {high_scorers}")
    
    # 创建姓名到分数的映射
    name_score_map = {student["name"]: student["score"] for student in students}
    print(f"  姓名分数映射: {name_score_map}")


def generator_expressions():
    """生成器表达式（与推导式的区别）"""
    print("\n生成器表达式:")
    
    # 列表推导式（立即计算）
    list_comp = [x**2 for x in range(5)]
    print(f"  列表推导式: {list_comp}")
    
    # 生成器表达式（惰性计算）
    gen_exp = (x**2 for x in range(5))
    print(f"  生成器表达式对象: {gen_exp}")
    print(f"  生成器表达式结果: {list(gen_exp)}")
    
    print("  区别:")
    print("    1. 列表推导式使用方括号[]，生成器表达式使用圆括号()")
    print("    2. 列表推导式立即创建整个列表，生成器表达式惰性计算")
    print("    3. 生成器表达式节省内存，适合处理大量数据")


if __name__ == "__main__":
    print("=== Python 推导式 ===")
    list_comprehensions()
    dict_comprehensions()
    set_comprehensions()
    nested_comprehensions()
    comparison_with_traditional_loops()
    performance_considerations()
    advanced_examples()
    generator_expressions()