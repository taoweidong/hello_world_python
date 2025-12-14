"""
Python 变量和数据类型学习模块
包括数字、字符串、列表、元组、字典、集合等基本数据类型
"""


def numeric_types():
    """数值类型示例"""
    # 整数
    integer_example = 42
    # 浮点数
    float_example = 3.14159
    # 复数
    complex_example = 3 + 4j
    print(f"整数: {integer_example}")
    print(f"浮点数: {float_example}")
    print(f"复数: {complex_example}")


def string_examples():
    """字符串操作示例"""
    # 字符串定义
    s1 = '单引号字符串'
    s2 = "双引号字符串"
    s3 = '''三引号字符串
    可以跨多行'''
    
    # 字符串常用操作
    name = "Python"
    greeting = f"你好, {name}!"  # f-string 格式化
    print(greeting)
    
    # 字符串方法
    text = "  Hello World  "
    print(f"原始文本: '{text}'")
    print(f"去除空格: '{text.strip()}'")
    print(f"转大写: {text.upper()}")
    print(f"转小写: {text.lower()}")
    print(f"替换: {text.replace('World', 'Python')}")


def list_examples():
    """列表操作示例"""
    # 创建列表
    fruits = ['苹果', '香蕉', '橙子']
    numbers = [1, 2, 3, 4, 5]
    
    # 列表操作
    print(f"水果列表: {fruits}")
    print(f"第一个水果: {fruits[0]}")
    print(f"最后一个是: {fruits[-1]}")
    
    # 添加元素
    fruits.append('葡萄')
    print(f"添加葡萄后: {fruits}")
    
    # 列表切片
    print(f"前两个水果: {fruits[:2]}")
    print(f"最后一个水果: {fruits[-1:]}")


def tuple_examples():
    """元组操作示例"""
    # 元组是不可变序列
    coordinates = (10, 20)
    rgb_color = (255, 128, 0)
    
    print(f"坐标: {coordinates}")
    print(f"RGB颜色: {rgb_color}")
    print(f"红色分量: {rgb_color[0]}")


def dict_examples():
    """字典操作示例"""
    # 创建字典
    person = {
        'name': '张三',
        'age': 30,
        'city': '北京'
    }
    
    # 访问和修改
    print(f"姓名: {person['name']}")
    person['age'] = 31
    print(f"更新年龄后: {person}")
    
    # 添加新键值对
    person['job'] = '工程师'
    print(f"添加职业后: {person}")
    
    # 遍历字典
    for key, value in person.items():
        print(f"{key}: {value}")


def set_examples():
    """集合操作示例"""
    # 创建集合
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    
    # 集合运算
    print(f"交集: {set1 & set2}")
    print(f"并集: {set1 | set2}")
    print(f"差集: {set1 - set2}")


if __name__ == "__main__":
    print("=== 数值类型 ===")
    numeric_types()
    print("\n=== 字符串操作 ===")
    string_examples()
    print("\n=== 列表操作 ===")
    list_examples()
    print("\n=== 元组操作 ===")
    tuple_examples()
    print("\n=== 字典操作 ===")
    dict_examples()
    print("\n=== 集合操作 ===")
    set_examples()