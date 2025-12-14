"""
类和对象学习模块
包括类的定义、实例化、属性和方法等基本概念
"""


class Person:
    """人类 - 基本类示例"""
    
    # 类属性
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """构造方法"""
        self.name = name  # 实例属性
        self.age = age    # 实例属性
    
    def introduce(self):
        """实例方法"""
        print(f"你好, 我是 {self.name}, 今年 {self.age} 岁")
    
    @classmethod
    def get_species(cls):
        """类方法"""
        return cls.species
    
    @staticmethod
    def info():
        """静态方法"""
        print("这是一个人类的类")


class Student(Person):
    """学生类 - 继承自Person"""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll_course(self, course):
        """选课方法"""
        self.courses.append(course)
        print(f"{self.name} 选修了 {course}")
    
    def introduce(self):
        """重写父类方法"""
        super().introduce()
        print(f"学号是 {self.student_id}")
        if self.courses:
            print(f"选修课程: {', '.join(self.courses)}")


class Rectangle:
    """矩形类 - 演示属性装饰器"""
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        """计算面积 - 属性方式访问"""
        return self._width * self._height
    
    @property
    def width(self):
        """宽度获取"""
        return self._width
    
    @width.setter
    def width(self, value):
        """宽度设置"""
        if value <= 0:
            raise ValueError("宽度必须大于0")
        self._width = value
    
    @property
    def height(self):
        """高度获取"""
        return self._height
    
    @height.setter
    def height(self, value):
        """高度设置"""
        if value <= 0:
            raise ValueError("高度必须大于0")
        self._height = value


def class_examples():
    """类和对象示例"""
    print("=== 创建和使用对象 ===")
    # 创建Person对象
    person = Person("张三", 25)
    person.introduce()
    print(f"物种: {Person.get_species()}")
    Person.info()
    
    print("\n=== 继承和多态 ===")
    # 创建Student对象
    student = Student("李四", 20, "2023001")
    student.introduce()
    student.enroll_course("Python编程")
    student.enroll_course("数据结构")
    student.introduce()
    
    print("\n=== 属性装饰器 ===")
    # 使用属性装饰器
    rect = Rectangle(5, 3)
    print(f"宽度: {rect.width}, 高度: {rect.height}")
    print(f"面积: {rect.area}")
    
    # 修改属性
    rect.width = 10
    print(f"新宽度: {rect.width}")
    print(f"新面积: {rect.area}")


if __name__ == "__main__":
    class_examples()