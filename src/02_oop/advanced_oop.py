"""
高级面向对象编程
包括特殊方法、多重继承、抽象类等高级概念
"""
from abc import ABC, abstractmethod


class Vector:
    """向量类 - 演示特殊方法"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """对象表示"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """加法运算"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __eq__(self, other):
        """相等比较"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """长度"""
        return 2
    
    def __getitem__(self, index):
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")


class Animal(ABC):
    """动物抽象基类"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """抽象方法 - 子类必须实现"""
        pass
    
    def sleep(self):
        """具体方法"""
        print(f"{self.name} 正在睡觉")


class Dog(Animal):
    """狗类"""
    
    def make_sound(self):
        return "汪汪"


class Cat(Animal):
    """猫类"""
    
    def make_sound(self):
        return "喵喵"


class Flyable:
    """飞行能力混入类"""
    
    def fly(self):
        print(f"{self.name} 正在飞翔")


class FlyingDog(Dog, Flyable):
    """会飞的狗 - 演示多重继承"""
    pass


def special_methods_examples():
    """特殊方法示例"""
    print("=== 特殊方法 ===")
    v1 = Vector(2, 3)
    v2 = Vector(1, 4)
    
    print(f"v1: {v1}")
    print(f"repr(v1): {repr(v1)}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"len(v1): {len(v1)}")
    print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")


def abstract_class_examples():
    """抽象类示例"""
    print("\n=== 抽象类 ===")
    dog = Dog("旺财")
    cat = Cat("咪咪")
    
    animals = [dog, cat]
    for animal in animals:
        print(f"{animal.name} 说: {animal.make_sound()}")
        animal.sleep()


def multiple_inheritance_examples():
    """多重继承示例"""
    print("\n=== 多重继承 ===")
    flying_dog = FlyingDog("飞狗")
    print(f"{flying_dog.name} 说: {flying_dog.make_sound()}")
    flying_dog.fly()


if __name__ == "__main__":
    special_methods_examples()
    abstract_class_examples()
    multiple_inheritance_examples()