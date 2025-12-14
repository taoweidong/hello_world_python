"""
生成器和迭代器学习模块
"""
import itertools


def basic_iterators():
    """基本迭代器"""
    # 列表是可迭代对象
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)
    
    print("使用迭代器:")
    try:
        while True:
            item = next(iterator)
            print(f"  {item}")
    except StopIteration:
        print("  迭代结束")
    
    # 使用for循环自动处理StopIteration
    print("使用for循环:")
    for num in numbers:
        print(f"  {num}")


def generator_functions():
    """生成器函数"""
    def count_up_to(max_num):
        """计数到指定数字的生成器"""
        count = 1
        while count <= max_num:
            yield count
            count += 1
    
    def fibonacci():
        """斐波那契数列生成器"""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    print("计数生成器:")
    counter = count_up_to(5)
    for num in counter:
        print(f"  {num}")
    
    print("斐波那契数列(前10个):")
    fib = fibonacci()
    for _ in range(10):
        print(f"  {next(fib)}")


def generator_expressions():
    """生成器表达式"""
    # 类似列表推导式，但使用圆括号
    squares = (x**2 for x in range(10))
    print("生成器表达式(平方数):")
    for square in squares:
        print(f"  {square}")
    
    # 生成器表达式内存效率更高
    # 创建一个大的数据集进行对比
    large_list = [x for x in range(1000000)]      # 列表推导式
    large_generator = (x for x in range(1000000)) # 生成器表达式
    
    print(f"列表大小: {len(large_list)}")
    print(f"生成器类型: {type(large_generator)}")
    # 注意：不能直接获取生成器的长度，需要消耗它


def itertools_examples():
    """itertools模块示例"""
    # 无限迭代器
    print("无限计数器(前5个):")
    counter = itertools.count(start=10, step=2)
    for i, num in enumerate(counter):
        if i >= 5:
            break
        print(f"  {num}")
    
    # 有限迭代器
    print("重复元素:")
    repeater = itertools.repeat('Python', 3)
    for item in repeater:
        print(f"  {item}")
    
    # 组合函数
    letters = ['A', 'B', 'C']
    numbers = [1, 2]
    
    print("笛卡尔积:")
    product = itertools.product(letters, numbers)
    for item in product:
        print(f"  {item}")
    
    print("排列(2个元素):")
    permutations = itertools.permutations(letters, 2)
    for item in permutations:
        print(f"  {item}")
    
    print("组合(2个元素):")
    combinations = itertools.combinations(letters, 2)
    for item in combinations:
        print(f"  {item}")


class CustomIterator:
    """自定义迭代器类"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


def custom_iterator_example():
    """自定义迭代器示例"""
    data = ['苹果', '香蕉', '橙子']
    custom_iter = CustomIterator(data)
    
    print("自定义迭代器:")
    for item in custom_iter:
        print(f"  {item}")


if __name__ == "__main__":
    print("=== 基本迭代器 ===")
    basic_iterators()
    
    print("\n=== 生成器函数 ===")
    generator_functions()
    
    print("\n=== 生成器表达式 ===")
    generator_expressions()
    
    print("\n=== itertools模块 ===")
    itertools_examples()
    
    print("\n=== 自定义迭代器 ===")
    custom_iterator_example()