"""
文件操作学习模块
包括文件读写、路径操作等
"""
import json
import os
import csv
from pathlib import Path


def basic_file_operations():
    """基本文件操作"""
    # 写入文件
    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write("Hello, Python!\n")
        f.write("这是第二行\n")
        f.write("这是第三行")
    
    # 读取整个文件
    with open('example.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("文件内容:")
        print(content)
    
    # 按行读取
    with open('example.txt', 'r', encoding='utf-8') as f:
        print("逐行读取:")
        for line_num, line in enumerate(f, 1):
            print(f"第{line_num}行: {line.strip()}")
    
    # 删除示例文件
    if os.path.exists('example.txt'):
        os.remove('example.txt')


def path_operations():
    """路径操作"""
    # 使用 os.path
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', 'example.txt')
    print(f"文件路径: {file_path}")
    print(f"目录名: {os.path.dirname(file_path)}")
    print(f"文件名: {os.path.basename(file_path)}")
    print(f"是否存在: {os.path.exists(file_path)}")
    
    # 使用 pathlib (推荐)
    p = Path('data') / 'example.txt'
    print(f"\nPath对象: {p}")
    print(f"父目录: {p.parent}")
    print(f"文件名: {p.name}")
    print(f"后缀: {p.suffix}")


def json_operations():
    """JSON操作"""
    # 数据
    data = {
        'name': '张三',
        'age': 30,
        'skills': ['Python', 'Java', 'JavaScript'],
        'address': {
            'city': '北京',
            'district': '朝阳区'
        }
    }
    
    # 序列化为JSON字符串
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print("JSON字符串:")
    print(json_str)
    
    # 写入JSON文件
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 从JSON文件读取
    with open('data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print("\n从文件加载的数据:")
        print(loaded_data)
    
    # 清理文件
    if os.path.exists('data.json'):
        os.remove('data.json')


def csv_operations():
    """CSV操作"""
    # 示例数据
    data = [
        ['姓名', '年龄', '城市'],
        ['张三', '25', '北京'],
        ['李四', '30', '上海'],
        ['王五', '28', '广州']
    ]
    
    # 写入CSV文件
    with open('people.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    # 读取CSV文件
    with open('people.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("CSV文件内容:")
        for row in reader:
            print(row)
    
    # 使用DictReader和DictWriter
    with open('people_dict.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['姓名', '年龄', '城市']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        writer.writerow({'姓名': '赵六', '年龄': '35', '城市': '深圳'})
        writer.writerow({'姓名': '孙七', '年龄': '22', '城市': '杭州'})
    
    with open('people_dict.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\n使用DictReader:")
        for row in reader:
            print(f"{row['姓名']} - {row['年龄']}岁 - {row['城市']}")
    
    # 清理文件
    for file in ['people.csv', 'people_dict.csv']:
        if os.path.exists(file):
            os.remove(file)


if __name__ == "__main__":
    print("=== 基本文件操作 ===")
    basic_file_operations()
    
    print("\n=== 路径操作 ===")
    path_operations()
    
    print("\n=== JSON操作 ===")
    json_operations()
    
    print("\n=== CSV操作 ===")
    csv_operations()