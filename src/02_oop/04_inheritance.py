"""
Python 面向对象编程 - 继承
子类复用父类的属性和方法，并可以扩展或重写
"""

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self, food):
        """进食方法"""
        print(f"{self.name} 正在吃 {food}")
        self.energy += 10
    
    def sleep(self):
        """睡觉方法"""
        print(f"{self.name} 正在睡觉")
        self.energy += 20
    
    def make_sound(self):
        """发出声音 - 将被子类重写"""
        pass
    
    def get_info(self):
        """获取基本信息"""
        return f"名字: {self.name}, 种类: {self.species}, 精力: {self.energy}"


class Dog(Animal):
    """狗类 - 继承自动物类"""
    
    def __init__(self, name, breed):
        # 调用父类构造方法
        super().__init__(name, "犬科")
        self.breed = breed  # 子类特有属性
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 汪汪叫")
    
    def fetch(self):
        """子类特有方法"""
        print(f"{self.name} 捡回了球")
        self.energy -= 10
    
    def get_info(self):
        """重写父类方法并扩展"""
        base_info = super().get_info()
        return f"{base_info}, 品种: {self.breed}"


class Cat(Animal):
    """猫类 - 继承自动物类"""
    
    def __init__(self, name, color):
        super().__init__(name, "猫科")
        self.color = color
        self.lives = 9  # 猫有九条命（传说）
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 喵喵叫")
    
    def climb_tree(self):
        """子类特有方法"""
        print(f"{self.name} 爬上了树")
        self.energy -= 5
    
    def get_info(self):
        """重写父类方法并扩展"""
        base_info = super().get_info()
        return f"{base_info}, 颜色: {self.color}, 剩余生命: {self.lives}"


class Bird(Animal):
    """鸟类 - 继承自动物类"""
    
    def __init__(self, name, wingspan):
        super().__init__(name, "鸟类")
        self.wingspan = wingspan  # 翼展
    
    def make_sound(self):
        """重写父类方法"""
        print(f"{self.name} 啾啾叫")
    
    def fly(self):
        """子类特有方法"""
        if self.energy >= 20:
            print(f"{self.name} 在空中飞翔，翼展 {self.wingspan} 厘米")
            self.energy -= 20
        else:
            print(f"{self.name} 太累了，无法飞翔")
    
    def get_info(self):
        """重写父类方法并扩展"""
        base_info = super().get_info()
        return f"{base_info}, 翼展: {self.wingspan}cm"


class PetDog(Dog):
    """宠物狗类 - 多层继承"""
    
    def __init__(self, name, breed, owner):
        super().__init__(name, breed)
        self.owner = owner  # 主人
    
    def play_with_owner(self):
        """与主人玩耍"""
        print(f"{self.name} 和主人 {self.owner} 一起玩耍")
        self.energy -= 15
    
    def get_info(self):
        """重写父类方法并扩展"""
        base_info = super().get_info()
        return f"{base_info}, 主人: {self.owner}"


def inheritance_demo():
    """继承演示"""
    print("=== 继承 ===")
    print("子类复用父类的属性和方法，并可以扩展或重写")
    
    # 创建不同类型的动物对象
    dog = Dog("旺财", "金毛")
    cat = Cat("咪咪", "橘色")
    bird = Bird("小鸟", 30)
    pet_dog = PetDog("豆豆", "泰迪", "小明")
    
    # 使用继承的方法
    print("\n--- 动物基本信息 ---")
    animals = [dog, cat, bird, pet_dog]
    for animal in animals:
        print(animal.get_info())
    
    # 使用各自的声音方法（多态体现）
    print("\n--- 动物叫声 ---")
    for animal in animals:
        animal.make_sound()
    
    # 使用各自的特有方法
    print("\n--- 各自特有行为 ---")
    dog.fetch()
    cat.climb_tree()
    bird.fly()
    pet_dog.play_with_owner()
    
    # 使用继承的通用方法
    print("\n--- 通用行为 ---")
    dog.eat("骨头")
    cat.sleep()
    bird.eat("虫子")
    pet_dog.sleep()
    
    # 再次显示信息
    print("\n--- 活动后状态 ---")
    for animal in animals:
        print(animal.get_info())


if __name__ == "__main__":
    inheritance_demo()