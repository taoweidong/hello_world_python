"""
正则表达式学习模块
包括模式匹配、文本处理等
"""
import re


def basic_regex():
    """基本正则表达式"""
    text = "我的电话号码是 138-1234-5678，邮箱是 example@email.com"
    
    # 查找电话号码
    phone_pattern = r'\d{3}-\d{4}-\d{4}'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"找到电话号码: {phone_match.group()}")
    
    # 查找邮箱
    email_pattern = r'\w+@\w+\.\w+'
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"找到邮箱: {email_match.group()}")
    
    # 查找所有数字
    digits = re.findall(r'\d+', text)
    print(f"所有数字: {digits}")


def regex_groups():
    """正则表达式分组"""
    text = "张三: 25岁, 北京; 李四: 30岁, 上海; 王五: 28岁, 广州"
    
    # 使用分组提取信息
    pattern = r'(\w+):\s*(\d+)岁,\s*(\w+)'
    matches = re.findall(pattern, text)
    
    print("人员信息:")
    for name, age, city in matches:
        print(f"  姓名: {name}, 年龄: {age}, 城市: {city}")
    
    # 命名分组
    named_pattern = r'(?P<name>\w+):\s*(?P<age>\d+)岁,\s*(?P<city>\w+)'
    for match in re.finditer(named_pattern, text):
        print(f"  姓名: {match.group('name')}, "
              f"年龄: {match.group('age')}, "
              f"城市: {match.group('city')}")


def regex_substitution():
    """正则表达式替换"""
    text = "今天是2023年12月15日，明天是2023年12月16日"
    
    # 替换日期格式
    # 将 YYYY年MM月DD日 替换为 YYYY-MM-DD
    date_pattern = r'(\d{4})年(\d{1,2})月(\d{1,2})日'
    formatted_text = re.sub(date_pattern, r'\1-\2-\3', text)
    print(f"原文字: {text}")
    print(f"格式化后: {formatted_text}")
    
    # 隐藏手机号中间四位
    phone_text = "联系方式: 13812345678, 15987654321"
    hidden_phone = re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', phone_text)
    print(f"隐藏手机号: {hidden_phone}")


def regex_compilation():
    """编译正则表达式"""
    # 对于重复使用的正则表达式，预先编译可以提高性能
    email_regex = re.compile(r'\w+@\w+\.\w+')
    phone_regex = re.compile(r'\d{3}-\d{4}-\d{4}')
    
    text = "联系邮箱: test@example.com, 电话: 138-1234-5678"
    
    emails = email_regex.findall(text)
    phones = phone_regex.findall(text)
    
    print(f"找到的邮箱: {emails}")
    print(f"找到的电话: {phones}")


if __name__ == "__main__":
    print("=== 基本正则表达式 ===")
    basic_regex()
    
    print("\n=== 正则表达式分组 ===")
    regex_groups()
    
    print("\n=== 正则表达式替换 ===")
    regex_substitution()
    
    print("\n=== 编译正则表达式 ===")
    regex_compilation()