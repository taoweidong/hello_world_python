"""
Python 面向对象编程 - 类的定义
类是对象的蓝图或模板，定义了对象的属性和方法
"""

class Car:
    """汽车类 - 演示类的基本定义"""
    
    # 类属性 - 所有实例共享
    wheels = 4
    engine_type = "内燃机"
    
    def __init__(self, brand, model, color):
        """
        构造方法 - 初始化对象属性
        :param brand: 品牌
        :param model: 型号
        :param color: 颜色
        """
        # 实例属性 - 每个实例独有
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False
        self.speed = 0
    
    def start_engine(self):
        """启动引擎方法"""
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} 引擎已启动")
        else:
            print(f"{self.brand} {self.model} 引擎已在运行中")
    
    def stop_engine(self):
        """停止引擎方法"""
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print(f"{self.brand} {self.model} 引擎已停止")
        else:
            print(f"{self.brand} {self.model} 引擎已处于停止状态")
    
    def accelerate(self, speed_increase):
        """加速方法"""
        if self.is_running:
            self.speed += speed_increase
            print(f"{self.brand} {self.model} 当前速度: {self.speed} km/h")
        else:
            print("请先启动引擎")
    
    def get_info(self):
        """获取汽车信息"""
        return f"品牌: {self.brand}, 型号: {self.model}, 颜色: {self.color}"


def class_demo():
    """类定义演示"""
    print("=== 类的定义 ===")
    print("类是创建对象的模板，定义了对象的属性和方法")
    
    # 创建Car类的实例
    car1 = Car("丰田", "卡罗拉", "白色")
    car2 = Car("本田", "雅阁", "黑色")
    
    print(f"汽车1: {car1.get_info()}")
    print(f"汽车2: {car2.get_info()}")
    
    # 访问类属性
    print(f"车轮数量: {Car.wheels}")
    print(f"引擎类型: {Car.engine_type}")
    
    # 调用方法
    car1.start_engine()
    car1.accelerate(50)
    car1.accelerate(30)
    car1.stop_engine()


if __name__ == "__main__":
    class_demo()