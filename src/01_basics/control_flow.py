"""
控制流程学习模块
包括条件语句、循环语句等控制结构
"""


def conditionals():
    """条件语句示例"""
    age = 20
    
    # if-elif-else 结构
    if age < 13:
        print("儿童")
    elif age < 20:
        print("青少年")
    elif age < 60:
        print("成年人")
    else:
        print("老年人")
    
    # 三元运算符
    result = "成年" if age >= 18 else "未成年"
    print(f"年龄状态: {result}")


def loops():
    """循环语句示例"""
    # for 循环
    print("使用 for 循环:")
    for i in range(5):
        print(f"  第 {i+1} 次循环")
    
    # 遍历列表
    fruits = ["苹果", "香蕉", "橙子"]
    print("遍历水果列表:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # 使用 enumerate 获取索引和值
    print("使用 enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"  索引 {index}: {fruit}")
    
    # while 循环
    print("使用 while 循环:")
    count = 0
    while count < 3:
        print(f"  计数: {count}")
        count += 1
    
    # 循环控制语句
    print("循环中的 break 和 continue:")
    for i in range(10):
        if i == 3:
            continue  # 跳过本次循环
        if i == 7:
            break     # 退出循环
        print(f"  数字: {i}")


def comprehensions():
    """推导式示例"""
    # 列表推导式
    squares = [x**2 for x in range(10)]
    print(f"平方数列表: {squares}")
    
    # 条件推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"偶数的平方: {even_squares}")
    
    # 字典推导式
    square_dict = {x: x**2 for x in range(5)}
    print(f"平方数字典: {square_dict}")
    
    # 集合推导式
    odd_set = {x for x in range(10) if x % 2 == 1}
    print(f"奇数集合: {odd_set}")


if __name__ == "__main__":
    print("=== 条件语句 ===")
    conditionals()
    print("\n=== 循环语句 ===")
    loops()
    print("\n=== 推导式 ===")
    comprehensions()