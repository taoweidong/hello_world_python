"""
Python 字符串操作学习模块
包括字符串的各种操作方法和技巧
"""


def string_creation():
    """字符串创建"""
    # 多种方式创建字符串
    s1 = '单引号字符串'
    s2 = "双引号字符串"
    s3 = '''三引号字符串
可以跨多行'''
    s4 = """另一种三引号字符串
也可以跨多行"""
    
    # 使用str()函数创建
    s5 = str(123)
    s6 = str(3.14)
    
    print("字符串创建:")
    print(f"  单引号: {s1}")
    print(f"  双引号: {s2}")
    print(f"  三引号1: {s3}")
    print(f"  三引号2: {s4}")
    print(f"  str(123): {s5}")
    print(f"  str(3.14): {s6}")


def string_indexing_slicing():
    """字符串索引和切片"""
    text = "Python编程"
    
    print("字符串索引和切片:")
    print(f"  原字符串: {text}")
    print(f"  第1个字符: {text[0]}")
    print(f"  第2个字符: {text[1]}")
    print(f"  最后一个字符: {text[-1]}")
    print(f"  倒数第二个字符: {text[-2]}")
    
    # 切片操作 [start:end:step]
    print(f"  前4个字符: {text[:4]}")
    print(f"  从第5个字符开始: {text[4:]}")
    print(f"  第2到第5个字符: {text[1:5]}")
    print(f"  逆序字符串: {text[::-1]}")


def string_methods():
    """字符串常用方法"""
    text = "  Hello, Python World!  "
    
    print("字符串常用方法:")
    print(f"  原字符串: '{text}'")
    print(f"  去除两端空格: '{text.strip()}'")
    print(f"  转大写: '{text.upper()}'")
    print(f"  转小写: '{text.lower()}'")
    print(f"  首字母大写: '{text.capitalize()}'")
    print(f"  每个单词首字母大写: '{text.title()}'")
    
    # 查找和替换
    find_text = "Python"
    print(f"  查找'{find_text}': 位置 {text.find(find_text)}")
    print(f"  替换'Python'为'Java': '{text.replace('Python', 'Java')}'")
    
    # 分割和连接
    words = "apple,banana,orange"
    word_list = words.split(',')
    print(f"  分割'{words}': {word_list}")
    print(f"  连接列表: {'-'.join(word_list)}")


def string_formatting():
    """字符串格式化"""
    name = "张三"
    age = 25
    score = 95.5
    
    print("字符串格式化:")
    
    # 百分号格式化 (旧式)
    old_style = "姓名: %s, 年龄: %d, 分数: %.1f" % (name, age, score)
    print(f"  %格式化: {old_style}")
    
    # format方法 (新式)
    new_style = "姓名: {}, 年龄: {}, 分数: {:.1f}".format(name, age, score)
    print(f"  format方法: {new_style}")
    
    # f-string (推荐，Python 3.6+)
    f_string = f"姓名: {name}, 年龄: {age}, 分数: {score:.1f}"
    print(f"  f-string: {f_string}")
    
    # 带索引的format
    indexed_format = "分数: {2:.1f}, 姓名: {0}, 年龄: {1}".format(name, age, score)
    print(f"  索引format: {indexed_format}")
    
    # 带名称的format
    named_format = "姓名: {name}, 年龄: {age}, 分数: {score:.1f}".format(
        name=name, age=age, score=score)
    print(f"  命名format: {named_format}")


def string_validation():
    """字符串验证方法"""
    text1 = "Hello123"
    text2 = "123456"
    text3 = "Hello"
    text4 = "   "
    
    print("字符串验证方法:")
    print(f"  '{text1}' 是否为字母数字: {text1.isalnum()}")
    print(f"  '{text2}' 是否为数字: {text2.isdigit()}")
    print(f"  '{text3}' 是否为字母: {text3.isalpha()}")
    print(f"  '{text4}' 是否为空白: {text4.isspace()}")
    print(f"  '{text3}' 是否为大写: {text3.isupper()}")
    print(f"  '{text3}' 是否为小写: {text3.islower()}")
    print(f"  '{text3}' 是否以'H'开头: {text3.startswith('H')}")
    print(f"  '{text3}' 是否以'o'结尾: {text3.endswith('o')}")


def string_encoding():
    """字符串编码"""
    text = "你好，Python"
    
    print("字符串编码:")
    print(f"  原字符串: {text}")
    print(f"  UTF-8编码: {text.encode('utf-8')}")
    print(f"  GBK编码: {text.encode('gbk')}")
    
    # 解码
    utf8_bytes = text.encode('utf-8')
    decoded_text = utf8_bytes.decode('utf-8')
    print(f"  解码后: {decoded_text}")


def multiline_strings():
    """多行字符串"""
    # 使用三引号创建多行字符串
    multiline1 = """这是第一行
这是第二行
这是第三行"""
    
    # 使用转义字符
    multiline2 = "这是第一行\n这是第二行\n这是第三行"
    
    # 隐式连接
    multiline3 = ("这是第一行 "
                  "这是同一行的延续 "
                  "还是同一行")
    
    print("多行字符串:")
    print("  三引号方式:")
    print(multiline1)
    print("  转义字符方式:")
    print(multiline2)
    print(f"  隐式连接: {multiline3}")


def string_constants():
    """字符串常量"""
    import string
    
    print("字符串常量:")
    print(f"  ascii_letters: {string.ascii_letters}")
    print(f"  ascii_lowercase: {string.ascii_lowercase}")
    print(f"  ascii_uppercase: {string.ascii_uppercase}")
    print(f"  digits: {string.digits}")
    print(f"  punctuation: {string.punctuation}")


if __name__ == "__main__":
    print("=== 字符串创建 ===")
    string_creation()
    
    print("\n=== 字符串索引和切片 ===")
    string_indexing_slicing()
    
    print("\n=== 字符串常用方法 ===")
    string_methods()
    
    print("\n=== 字符串格式化 ===")
    string_formatting()
    
    print("\n=== 字符串验证方法 ===")
    string_validation()
    
    print("\n=== 字符串编码 ===")
    string_encoding()
    
    print("\n=== 多行字符串 ===")
    multiline_strings()
    
    print("\n=== 字符串常量 ===")
    string_constants()