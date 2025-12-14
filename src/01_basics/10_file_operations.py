"""
Python 文件操作学习模块
包括文件的读写、路径操作等
"""
import os
import json
import csv
from pathlib import Path


def basic_file_operations():
    """基本文件操作"""
    filename = "example.txt"
    
    # 写入文件
    print("基本文件操作:")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Hello, Python!\n")
        f.write("这是第二行\n")
        f.write("这是第三行")
    
    # 读取整个文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"  文件内容:\n{content}")
    
    # 按行读取
    with open(filename, 'r', encoding='utf-8') as f:
        print("  逐行读取:")
        for line_num, line in enumerate(f, 1):
            print(f"    第{line_num}行: {line.strip()}")
    
    # 删除示例文件
    if os.path.exists(filename):
        os.remove(filename)


def file_modes():
    """文件模式"""
    print("\n文件模式:")
    print("  r: 只读模式（默认）")
    print("  w: 写入模式，会覆盖原有内容")
    print("  a: 追加模式，在文件末尾添加内容")
    print("  x: 独占创建模式，如果文件已存在会失败")
    print("  b: 二进制模式")
    print("  t: 文本模式（默认）")
    print("  +: 读写模式")


def file_methods():
    """文件方法"""
    filename = "methods_example.txt"
    
    # 写入示例数据
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("第一行\n第二行\n第三行\n第四行")
    
    print("\n文件方法:")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"  文件指针位置: {f.tell()}")
        first_line = f.readline()
        print(f"  读取第一行: {first_line.strip()}")
        print(f"  文件指针位置: {f.tell()}")
        
        # 移动文件指针
        f.seek(0)
        print(f"  重置指针后位置: {f.tell()}")
        all_lines = f.readlines()
        print(f"  读取所有行: {[line.strip() for line in all_lines]}")
    
    # 追加内容
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\n追加的新行")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"  追加后的内容:\n{content}")
    
    # 清理文件
    if os.path.exists(filename):
        os.remove(filename)


def path_operations():
    """路径操作"""
    print("\n路径操作:")
    
    # 使用 os.path
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', 'example.txt')
    print(f"  文件路径: {file_path}")
    print(f"  目录名: {os.path.dirname(file_path)}")
    print(f"  文件名: {os.path.basename(file_path)}")
    print(f"  是否存在: {os.path.exists(file_path)}")
    
    # 使用 pathlib (推荐)
    p = Path('data') / 'example.txt'
    print(f"\n  Path对象: {p}")
    print(f"  父目录: {p.parent}")
    print(f"  文件名: {p.name}")
    print(f"  后缀: {p.suffix}")


def json_operations():
    """JSON操作"""
    print("\nJSON操作:")
    
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
    print("  JSON字符串:")
    print(json_str)
    
    # 写入JSON文件
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # 从JSON文件读取
    with open('data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print(f"\n  从文件加载的数据: {loaded_data}")
    
    # 清理文件
    if os.path.exists('data.json'):
        os.remove('data.json')


def csv_operations():
    """CSV操作"""
    print("\nCSV操作:")
    
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
        print("  CSV文件内容:")
        for row in reader:
            print(f"    {row}")
    
    # 使用DictReader和DictWriter
    with open('people_dict.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['姓名', '年龄', '城市']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        writer.writerow({'姓名': '赵六', '年龄': '35', '城市': '深圳'})
        writer.writerow({'姓名': '孙七', '年龄': '22', '城市': '杭州'})
    
    with open('people_dict.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("\n  使用DictReader:")
        for row in reader:
            print(f"    {row['姓名']} - {row['年龄']}岁 - {row['城市']}")
    
    # 清理文件
    for file in ['people.csv', 'people_dict.csv']:
        if os.path.exists(file):
            os.remove(file)


def binary_files():
    """二进制文件操作"""
    print("\n二进制文件操作:")
    
    # 创建二进制数据
    binary_data = bytes([0, 1, 2, 3, 4, 5])
    
    # 写入二进制文件
    with open('binary_example.bin', 'wb') as f:
        f.write(binary_data)
    
    # 读取二进制文件
    with open('binary_example.bin', 'rb') as f:
        read_data = f.read()
        print(f"  读取的二进制数据: {list(read_data)}")
    
    # 清理文件
    if os.path.exists('binary_example.bin'):
        os.remove('binary_example.bin')


def file_context_manager():
    """文件上下文管理器"""
    print("\n文件上下文管理器:")
    print("  使用 with 语句自动管理文件的打开和关闭")
    print("  即使发生异常也会确保文件被正确关闭")
    
    try:
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write("测试内容")
            raise Exception("模拟异常")
    except Exception as e:
        print(f"  发生异常: {e}")
    finally:
        # 文件已经被自动关闭
        if os.path.exists('test.txt'):
            os.remove('test.txt')
            print("  文件已被清理")


def directory_operations():
    """目录操作"""
    print("\n目录操作:")
    
    # 创建目录
    if not os.path.exists('test_dir'):
        os.makedirs('test_dir')
        print("  创建目录: test_dir")
    
    # 列出目录内容
    print(f"  当前目录内容: {os.listdir('.')}")
    
    # 检查路径类型
    test_path = 'test_dir'
    print(f"  {test_path} 是目录: {os.path.isdir(test_path)}")
    print(f"  {test_path} 是文件: {os.path.isfile(test_path)}")
    
    # 删除目录
    if os.path.exists('test_dir'):
        os.rmdir('test_dir')
        print("  删除目录: test_dir")


if __name__ == "__main__":
    print("=== Python 文件操作 ===")
    basic_file_operations()
    file_modes()
    file_methods()
    path_operations()
    json_operations()
    csv_operations()
    binary_files()
    file_context_manager()
    directory_operations()