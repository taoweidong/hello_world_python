"""
Python 面向对象编程 - 多态
同一接口在不同对象中有不同行为
"""

import math

class Shape:
    """形状基类 - 定义通用接口"""
    
    def area(self):
        """计算面积 - 抽象方法"""
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        """计算周长 - 抽象方法"""
        raise NotImplementedError("子类必须实现perimeter方法")
    
    def describe(self):
        """描述形状"""
        return f"这是一个{self.__class__.__name__}"


class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """计算矩形面积"""
        return self.width * self.height
    
    def perimeter(self):
        """计算矩形周长"""
        return 2 * (self.width + self.height)
    
    def describe(self):
        """描述矩形"""
        return f"这是一个矩形，宽: {self.width}, 高: {self.height}"


class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """计算圆形面积"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """计算圆形周长"""
        return 2 * math.pi * self.radius
    
    def describe(self):
        """描述圆形"""
        return f"这是一个圆形，半径: {self.radius}"


class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, a, b, c):
        # 检查是否能构成三角形
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("三边不能构成三角形")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        """使用海伦公式计算三角形面积"""
        s = (self.a + self.b + self.c) / 2  # 半周长
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        """计算三角形周长"""
        return self.a + self.b + self.c
    
    def describe(self):
        """描述三角形"""
        return f"这是一个三角形，三边长: {self.a}, {self.b}, {self.c}"


class Square(Rectangle):
    """正方形类 - 继承自矩形"""
    
    def __init__(self, side):
        super().__init__(side, side)
    
    def describe(self):
        """描述正方形"""
        return f"这是一个正方形，边长: {self.width}"


def print_shape_info(shape):
    """打印形状信息 - 演示多态"""
    print(shape.describe())
    print(f"  面积: {shape.area():.2f}")
    print(f"  周长: {shape.perimeter():.2f}")
    print()


def polymorphism_demo():
    """多态演示"""
    print("=== 多态 ===")
    print("同一接口在不同对象中有不同行为")
    
    # 创建不同类型的形状对象
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(3, 4, 5),
        Square(6)
    ]
    
    # 使用相同的接口处理不同的对象
    print("--- 形状信息 ---")
    for shape in shapes:
        print_shape_info(shape)
    
    # 计算总面积
    total_area = sum(shape.area() for shape in shapes)
    print(f"所有形状的总面积: {total_area:.2f}")
    
    # 计算总周长
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    print(f"所有形状的总周长: {total_perimeter:.2f}")


class Animal:
    """动物基类 - 演示方法多态"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """发出声音"""
        pass
    
    def move(self):
        """移动"""
        print(f"{self.name} 正在移动")


class Dog(Animal):
    """狗类"""
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 汪汪叫")


class Cat(Animal):
    """猫类"""
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 喵喵叫")


class Bird(Animal):
    """鸟类"""
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 啾啾叫")
    
    def move(self):
        """重写父类方法"""
        print(f"{self.name} 在天空中飞翔")


def animal_concert(animals):
    """动物音乐会 - 演示多态"""
    print("\n--- 动物音乐会 ---")
    for animal in animals:
        animal.make_sound()


def animal_parade(animals):
    """动物游行 - 演示多态"""
    print("\n--- 动物游行 ---")
    for animal in animals:
        animal.move()


def advanced_polymorphism_demo():
    """高级多态演示"""
    print("\n=== 高级多态演示 ===")
    
    # 创建动物对象
    animals = [
        Dog("旺财"),
        Cat("咪咪"),
        Bird("小鸟")
    ]
    
    # 同一方法在不同对象上有不同表现
    animal_concert(animals)
    animal_parade(animals)


if __name__ == "__main__":
    polymorphism_demo()
    advanced_polymorphism_demo()