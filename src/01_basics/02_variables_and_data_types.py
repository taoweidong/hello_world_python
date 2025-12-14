"""
Python 变量与数据类型学习模块
包括变量声明、基本数据类型及其使用方法
"""


def variable_declaration():
    """变量声明示例"""
    # Python是动态类型语言，不需要显式声明类型
    name = "张三"           # 字符串
    age = 25               # 整数
    height = 1.75          # 浮点数
    is_student = True      # 布尔值
    
    print(f"姓名: {name}, 类型: {type(name)}")
    print(f"年龄: {age}, 类型: {type(age)}")
    print(f"身高: {height}, 类型: {type(height)}")
    print(f"是否为学生: {is_student}, 类型: {type(is_student)}")


def numeric_types():
    """数值类型示例"""
    # 整数类型
    integer_example = 42
    binary_number = 0b1010    # 二进制
    octal_number = 0o12       # 八进制
    hex_number = 0xA          # 十六进制
    
    print("整数类型:")
    print(f"  十进制: {integer_example}")
    print(f"  二进制: {binary_number} (0b1010)")
    print(f"  八进制: {octal_number} (0o12)")
    print(f"  十六进制: {hex_number} (0xA)")
    
    # 浮点数类型
    float_example = 3.14159
    scientific_notation = 1.5e2  # 科学计数法 1.5 × 10²
    
    print("\n浮点数类型:")
    print(f"  普通浮点数: {float_example}")
    print(f"  科学计数法: {scientific_notation}")
    
    # 复数类型
    complex_example = 3 + 4j
    print(f"\n复数: {complex_example}, 实部: {complex_example.real}, 虚部: {complex_example.imag}")


def string_examples():
    """字符串类型示例"""
    # 字符串定义方式
    s1 = '单引号字符串'
    s2 = "双引号字符串"
    s3 = '''三引号字符串
可以跨多行'''
    s4 = """另一种三引号字符串
也可以跨多行"""
    
    print("字符串类型:")
    print(f"  单引号: {s1}")
    print(f"  双引号: {s2}")
    print(f"  三引号1: {s3}")
    print(f"  三引号2: {s4}")


def boolean_examples():
    """布尔类型示例"""
    # 布尔值
    is_true = True
    is_false = False
    
    print("布尔类型:")
    print(f"  True: {is_true}")
    print(f"  False: {is_false}")
    
    # 布尔运算
    a = True
    b = False
    print(f"\n布尔运算:")
    print(f"  {a} and {b} = {a and b}")
    print(f"  {a} or {b} = {a or b}")
    print(f"  not {a} = {not a}")
    
    # 真值测试
    print(f"\n真值测试:")
    print(f"  bool(0) = {bool(0)}")
    print(f"  bool(1) = {bool(1)}")
    print(f"  bool('') = {bool('')}")
    print(f"  bool('hello') = {bool('hello')}")
    print(f"  bool([]) = {bool([])}")
    print(f"  bool([1, 2]) = {bool([1, 2])}")


def none_type_example():
    """None类型示例"""
    # None表示空值或无值
    empty_value = None
    print(f"None类型: {empty_value}, 类型: {type(empty_value)}")
    
    # None的比较
    print(f"None == None: {None == None}")
    print(f"None is None: {None is None}")


def type_conversion():
    """类型转换示例"""
    # 显式类型转换
    str_num = "123"
    int_num = int(str_num)
    float_num = float(str_num)
    
    print("类型转换:")
    print(f"  字符串 '{str_num}' 转整数: {int_num}")
    print(f"  字符串 '{str_num}' 转浮点数: {float_num}")
    
    # 数字转字符串
    num = 456
    str_from_num = str(num)
    print(f"  数字 {num} 转字符串: '{str_from_num}'")
    
    # 布尔转换
    print(f"  int to bool: bool(0)={bool(0)}, bool(1)={bool(1)}")
    print(f"  str to bool: bool('')={bool('')}, bool('a')={bool('a')}")


if __name__ == "__main__":
    print("=== 变量声明 ===")
    variable_declaration()
    print("\n=== 数值类型 ===")
    numeric_types()
    print("\n=== 字符串类型 ===")
    string_examples()
    print("\n=== 布尔类型 ===")
    boolean_examples()
    print("\n=== None类型 ===")
    none_type_example()
    print("\n=== 类型转换 ===")
    type_conversion()