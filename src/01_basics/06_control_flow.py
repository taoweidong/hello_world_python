"""
Python 控制流程学习模块
包括条件语句、循环语句等控制结构
"""


def conditionals():
    """条件语句示例"""
    age = 20
    
    # if-elif-else 结构
    print("条件语句:")
    if age < 13:
        print("  儿童")
    elif age < 20:
        print("  青少年")
    elif age < 60:
        print("  成年人")
    else:
        print("  老年人")
    
    # 三元运算符
    result = "成年" if age >= 18 else "未成年"
    print(f"  年龄状态: {result}")
    
    # 多条件判断
    score = 85
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    print(f"  分数: {score}, 等级: {grade}")


def loops():
    """循环语句示例"""
    # for 循环
    print("\n循环语句:")
    print("  使用 for 循环:")
    for i in range(5):
        print(f"    第 {i+1} 次循环")
    
    # 遍历列表
    fruits = ["苹果", "香蕉", "橙子"]
    print("  遍历水果列表:")
    for fruit in fruits:
        print(f"    {fruit}")
    
    # 使用 enumerate 获取索引和值
    print("  使用 enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"    索引 {index}: {fruit}")
    
    # while 循环
    print("  使用 while 循环:")
    count = 0
    while count < 3:
        print(f"    计数: {count}")
        count += 1
    
    # 循环控制语句
    print("  循环中的 break 和 continue:")
    for i in range(10):
        if i == 3:
            continue  # 跳过本次循环
        if i == 7:
            break     # 退出循环
        print(f"    数字: {i}")


def comprehensions():
    """推导式示例"""
    # 列表推导式
    squares = [x**2 for x in range(10)]
    print("\n推导式:")
    print(f"  平方数列表: {squares}")
    
    # 条件推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"  偶数的平方: {even_squares}")
    
    # 字典推导式
    square_dict = {x: x**2 for x in range(5)}
    print(f"  平方数字典: {square_dict}")
    
    # 集合推导式
    odd_set = {x for x in range(10) if x % 2 == 1}
    print(f"  奇数集合: {odd_set}")


def nested_loops():
    """嵌套循环示例"""
    print("\n嵌套循环:")
    # 打印乘法表
    print("  九九乘法表:")
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"    {j}×{i}={i*j}", end="  ")
        print()  # 换行


def loop_else_clause():
    """循环的else子句"""
    print("\n循环的else子句:")
    
    # for循环的else
    print("  for循环的else:")
    for i in range(3):
        print(f"    循环中: {i}")
        if i == 5:  # 这个条件永远不会满足
            break
    else:
        print("    for循环正常结束")
    
    # while循环的else
    print("  while循环的else:")
    count = 0
    while count < 3:
        print(f"    计数中: {count}")
        count += 1
        if count == 10:  # 这个条件永远不会满足
            break
    else:
        print("    while循环正常结束")


def match_statement():
    """模式匹配语句 (Python 3.10+)"""
    try:
        # Python 3.10+ 的 match-case 语句
        def handle_data(data):
            match data:
                case int() if data > 0:
                    return f"正整数: {data}"
                case int() if data < 0:
                    return f"负整数: {data}"
                case int():
                    return "零"
                case str() if len(data) > 10:
                    return "长字符串"
                case str():
                    return "短字符串"
                case list() if len(data) == 0:
                    return "空列表"
                case list():
                    return f"列表包含 {len(data)} 个元素"
                case _:
                    return "未知类型"
        
        print("\n模式匹配:")
        test_values = [42, -5, 0, "hello", "这是一个长字符串", [], [1, 2, 3]]
        for value in test_values:
            result = handle_data(value)
            print(f"  {value} -> {result}")
            
    except SyntaxError:
        print("\n模式匹配:")
        print("  当前Python版本不支持 match-case 语句 (需要Python 3.10+)")


if __name__ == "__main__":
    print("=== 条件语句 ===")
    conditionals()
    
    print("\n=== 循环语句 ===")
    loops()
    
    print("\n=== 推导式 ===")
    comprehensions()
    
    print("\n=== 嵌套循环 ===")
    nested_loops()
    
    print("\n=== 循环的else子句 ===")
    loop_else_clause()
    
    print("\n=== 模式匹配 ===")
    match_statement()