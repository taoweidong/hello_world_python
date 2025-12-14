"""
Python 容器类型学习模块
包括列表、元组、字典、集合等容器类型的使用方法
"""


def list_examples():
    """列表示例"""
    # 创建列表
    empty_list = []
    fruits = ["苹果", "香蕉", "橙子"]
    mixed_list = [1, "hello", 3.14, True]
    
    print("列表:")
    print(f"  空列表: {empty_list}")
    print(f"  水果列表: {fruits}")
    print(f"  混合列表: {mixed_list}")
    
    # 访问列表元素
    print(f"  第一个水果: {fruits[0]}")
    print(f"  最后一个水果: {fruits[-1]}")
    
    # 修改列表
    fruits[1] = "葡萄"
    print(f"  修改后的水果列表: {fruits}")
    
    # 列表方法
    fruits.append("草莓")
    print(f"  添加草莓后: {fruits}")
    
    fruits.insert(1, "樱桃")
    print(f"  在位置1插入樱桃: {fruits}")
    
    fruits.remove("橙子")
    print(f"  移除橙子: {fruits}")
    
    popped_item = fruits.pop()
    print(f"  弹出最后一个元素: {popped_item}, 列表: {fruits}")
    
    # 列表切片
    print(f"  前两个元素: {fruits[:2]}")
    print(f"  从第二个开始的所有元素: {fruits[1:]}")
    
    # 列表长度
    print(f"  列表长度: {len(fruits)}")


def tuple_examples():
    """元组示例"""
    # 创建元组
    empty_tuple = ()
    coordinates = (10, 20)
    person = ("张三", 25, "北京")
    single_element = (42,)  # 注意逗号，否则不是元组
    
    print("\n元组:")
    print(f"  空元组: {empty_tuple}")
    print(f"  坐标: {coordinates}")
    print(f"  个人信息: {person}")
    print(f"  单元素元组: {single_element}")
    
    # 访问元组元素
    print(f"  X坐标: {coordinates[0]}")
    print(f"  Y坐标: {coordinates[1]}")
    
    # 元组解包
    x, y = coordinates
    print(f"  解包后的坐标: x={x}, y={y}")
    
    name, age, city = person
    print(f"  解包后的信息: 姓名={name}, 年龄={age}, 城市={city}")
    
    # 元组方法
    numbers = (1, 2, 3, 2, 4, 2)
    print(f"  数字元组: {numbers}")
    print(f"  2出现的次数: {numbers.count(2)}")
    print(f"  3第一次出现的位置: {numbers.index(3)}")


def dict_examples():
    """字典示例"""
    # 创建字典
    empty_dict = {}
    person = {
        "name": "李四",
        "age": 30,
        "city": "上海"
    }
    # 使用dict()构造函数
    scores = dict(math=95, english=87, science=92)
    
    print("\n字典:")
    print(f"  空字典: {empty_dict}")
    print(f"  个人信息: {person}")
    print(f"  成绩: {scores}")
    
    # 访问字典元素
    print(f"  姓名: {person['name']}")
    print(f"  数学成绩: {scores['math']}")
    
    # 安全访问（避免KeyError）
    print(f"  英语成绩: {scores.get('english')}")
    print(f"  物理成绩: {scores.get('physics', '未录入')}")
    
    # 修改字典
    person["age"] = 31
    print(f"  更新年龄后: {person}")
    
    # 添加新键值对
    person["job"] = "工程师"
    scores["physics"] = 88
    print(f"  添加职业后: {person}")
    print(f"  添加物理成绩后: {scores}")
    
    # 删除键值对
    del person["city"]
    removed_score = scores.pop("science")
    print(f"  删除城市后: {person}")
    print(f"  删除科学成绩: {removed_score}, 剩余: {scores}")
    
    # 字典方法
    print(f"  所有键: {list(scores.keys())}")
    print(f"  所有值: {list(scores.values())}")
    print(f"  所有键值对: {list(scores.items())}")


def set_examples():
    """集合示例"""
    # 创建集合
    empty_set = set()  # 注意：{} 创建的是空字典，不是空集合
    numbers = {1, 2, 3, 4, 5}
    duplicate_numbers = {1, 2, 2, 3, 3, 3}  # 重复元素会被自动去重
    
    print("\n集合:")
    print(f"  空集合: {empty_set}")
    print(f"  数字集合: {numbers}")
    print(f"  带重复元素的集合: {duplicate_numbers}")
    
    # 集合操作
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"  集合1: {set1}")
    print(f"  集合2: {set2}")
    
    # 交集
    print(f"  交集: {set1 & set2}")
    print(f"  交集(方法): {set1.intersection(set2)}")
    
    # 并集
    print(f"  并集: {set1 | set2}")
    print(f"  并集(方法): {set1.union(set2)}")
    
    # 差集
    print(f"  差集(set1-set2): {set1 - set2}")
    print(f"  差集(set2-set1): {set2 - set1}")
    print(f"  差集(方法): {set1.difference(set2)}")
    
    # 对称差集
    print(f"  对称差集: {set1 ^ set2}")
    print(f"  对称差集(方法): {set1.symmetric_difference(set2)}")
    
    # 添加和删除元素
    set1.add(7)
    print(f"  添加7后: {set1}")
    
    set1.remove(1)
    print(f"  移除1后: {set1}")
    
    # 安全删除（避免KeyError）
    set1.discard(10)  # 删除不存在的元素不会报错
    print(f"  尝试移除10后: {set1}")


def container_comparison():
    """容器类型比较"""
    print("\n容器类型比较:")
    print("  可变性:")
    print("    列表(List): 可变")
    print("    元组(Tuple): 不可变")
    print("    字典(Dictionary): 可变")
    print("    集合(Set): 可变")
    
    print("\n  有序性:")
    print("    列表(List): 有序")
    print("    元组(Tuple): 有序")
    print("    字典(Dictionary): 有序(Python 3.7+)")
    print("    集合(Set): 无序")
    
    print("\n  重复元素:")
    print("    列表(List): 允许")
    print("    元组(Tuple): 允许")
    print("    字典(Dictionary): 键不允许重复")
    print("    集合(Set): 不允许")
    
    print("\n  访问方式:")
    print("    列表(List): 索引")
    print("    元组(Tuple): 索引")
    print("    字典(Dictionary): 键")
    print("    集合(Set): 只能遍历")


if __name__ == "__main__":
    print("=== 列表示例 ===")
    list_examples()
    
    print("\n=== 元组示例 ===")
    tuple_examples()
    
    print("\n=== 字典示例 ===")
    dict_examples()
    
    print("\n=== 集合示例 ===")
    set_examples()
    
    print("\n=== 容器类型比较 ===")
    container_comparison()