"""
Python 运算符学习模块
包括各种运算符的使用方法和优先级
"""


def arithmetic_operators():
    """算术运算符"""
    a = 10
    b = 3
    
    print("算术运算符:")
    print(f"  {a} + {b} = {a + b}")    # 加法
    print(f"  {a} - {b} = {a - b}")    # 减法
    print(f"  {a} * {b} = {a * b}")    # 乘法
    print(f"  {a} / {b} = {a / b}")    # 除法
    print(f"  {a} // {b} = {a // b}")  # 整除
    print(f"  {a} % {b} = {a % b}")    # 取模
    print(f"  {a} ** {b} = {a ** b}")  # 幂运算


def comparison_operators():
    """比较运算符"""
    x = 5
    y = 10
    
    print("\n比较运算符:")
    print(f"  {x} == {y}: {x == y}")   # 等于
    print(f"  {x} != {y}: {x != y}")   # 不等于
    print(f"  {x} < {y}: {x < y}")     # 小于
    print(f"  {x} > {y}: {x > y}")     # 大于
    print(f"  {x} <= {y}: {x <= y}")   # 小于等于
    print(f"  {x} >= {y}: {x >= y}")   # 大于等于


def logical_operators():
    """逻辑运算符"""
    a = True
    b = False
    
    print("\n逻辑运算符:")
    print(f"  {a} and {b}: {a and b}")  # 逻辑与
    print(f"  {a} or {b}: {a or b}")    # 逻辑或
    print(f"  not {a}: {not a}")         # 逻辑非


def bitwise_operators():
    """位运算符"""
    x = 5   # 二进制: 101
    y = 3   # 二进制: 011
    
    print("\n位运算符:")
    print(f"  {x} & {y}: {x & y}")     # 按位与
    print(f"  {x} | {y}: {x | y}")     # 按位或
    print(f"  {x} ^ {y}: {x ^ y}")     # 按位异或
    print(f"  ~{x}: {~x}")             # 按位取反
    print(f"  {x} << 1: {x << 1}")     # 左移
    print(f"  {x} >> 1: {x >> 1}")     # 右移


def assignment_operators():
    """赋值运算符"""
    a = 10
    print("\n赋值运算符:")
    print(f"  初始值 a = {a}")
    
    a += 5
    print(f"  a += 5 之后: {a}")
    
    a -= 3
    print(f"  a -= 3 之后: {a}")
    
    a *= 2
    print(f"  a *= 2 之后: {a}")
    
    a /= 4
    print(f"  a /= 4 之后: {a}")
    
    a //= 2
    print(f"  a //= 2 之后: {a}")
    
    a %= 3
    print(f"  a %= 3 之后: {a}")
    
    a **= 2
    print(f"  a **= 2 之后: {a}")


def membership_operators():
    """成员运算符"""
    fruits = ["苹果", "香蕉", "橙子"]
    item = "苹果"
    
    print("\n成员运算符:")
    print(f"  '{item}' in {fruits}: {item in fruits}")
    print(f"  '{item}' not in {fruits}: {item not in fruits}")
    
    # 字符串中的成员运算
    text = "Hello, Python!"
    char = "Python"
    print(f"  '{char}' in '{text}': {char in text}")


def identity_operators():
    """身份运算符"""
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print("\n身份运算符:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  c = a")
    print(f"  a is b: {a is b}")           # 比较对象身份
    print(f"  a is c: {a is c}")           # 比较对象身份
    print(f"  a is not b: {a is not b}")   # 比较对象身份
    print(f"  a == b: {a == b}")           # 比较对象值


def operator_precedence():
    """运算符优先级"""
    # 括号具有最高优先级
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    
    print("\n运算符优先级:")
    print(f"  2 + 3 * 4 = {result1}")      # 乘法优先于加法
    print(f"  (2 + 3) * 4 = {result2}")    # 括号改变优先级
    
    # 复杂表达式
    expr = 2 ** 3 * 4 / 2 + 5 - 1
    print(f"  2 ** 3 * 4 / 2 + 5 - 1 = {expr}")
    print("  计算顺序: 指数 -> 乘法 -> 除法 -> 加法 -> 减法")


def ternary_operator():
    """三元运算符"""
    age = 20
    
    # 三元运算符语法: value_if_true if condition else value_if_false
    status = "成年人" if age >= 18 else "未成年人"
    print(f"\n三元运算符:")
    print(f"  年龄: {age}")
    print(f"  状态: {status}")
    
    # 更复杂的三元运算符示例
    score = 85
    grade = "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"
    print(f"  分数: {score}")
    print(f"  等级: {grade}")


if __name__ == "__main__":
    print("=== 算术运算符 ===")
    arithmetic_operators()
    
    print("\n=== 比较运算符 ===")
    comparison_operators()
    
    print("\n=== 逻辑运算符 ===")
    logical_operators()
    
    print("\n=== 位运算符 ===")
    bitwise_operators()
    
    print("\n=== 赋值运算符 ===")
    assignment_operators()
    
    print("\n=== 成员运算符 ===")
    membership_operators()
    
    print("\n=== 身份运算符 ===")
    identity_operators()
    
    print("\n=== 运算符优先级 ===")
    operator_precedence()
    
    print("\n=== 三元运算符 ===")
    ternary_operator()