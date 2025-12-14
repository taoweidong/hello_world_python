"""
Python 面向对象编程 - 抽象
只暴露必要接口，隐藏复杂实现
"""

from abc import ABC, abstractmethod
import math

class Vehicle(ABC):
    """交通工具抽象基类"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._is_running = False
    
    @abstractmethod
    def start_engine(self):
        """启动引擎 - 抽象方法，子类必须实现"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """停止引擎 - 抽象方法，子类必须实现"""
        pass
    
    @abstractmethod
    def get_max_speed(self):
        """获取最大速度 - 抽象方法，子类必须实现"""
        pass
    
    def is_engine_running(self):
        """检查引擎是否运行 - 具体方法"""
        return self._is_running
    
    def get_info(self):
        """获取基本信息 - 具体方法"""
        return f"品牌: {self.brand}, 型号: {self.model}"


class Car(Vehicle):
    """汽车类 - 实现抽象基类"""
    
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.max_speed = 200
    
    def start_engine(self):
        """实现启动引擎"""
        if not self._is_running:
            self._is_running = True
            print(f"{self.brand} {self.model} 汽车引擎启动")
        else:
            print("引擎已经在运行")
    
    def stop_engine(self):
        """实现停止引擎"""
        if self._is_running:
            self._is_running = False
            print(f"{self.brand} {self.model} 汽车引擎停止")
        else:
            print("引擎已经停止")
    
    def get_max_speed(self):
        """实现获取最大速度"""
        return self.max_speed


class Motorcycle(Vehicle):
    """摩托车类 - 实现抽象基类"""
    
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size  # 发动机排量
        self.max_speed = 400
    
    def start_engine(self):
        """实现启动引擎"""
        if not self._is_running:
            self._is_running = True
            print(f"{self.brand} {self.model} 摩托车引擎启动，轰鸣声响起")
        else:
            print("引擎已经在运行")
    
    def stop_engine(self):
        """实现停止引擎"""
        if self._is_running:
            self._is_running = False
            print(f"{self.brand} {self.model} 摩托车引擎停止")
        else:
            print("引擎已经停止")
    
    def get_max_speed(self):
        """实现获取最大速度"""
        return self.max_speed


class ElectricVehicle(ABC):
    """电动车辆抽象基类 - 演示多重抽象"""
    
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity  # 电池容量(kWh)
        self.current_charge = battery_capacity    # 当前电量
    
    @abstractmethod
    def charge(self, amount):
        """充电 - 抽象方法"""
        pass
    
    @abstractmethod
    def estimate_range(self):
        """估算续航里程 - 抽象方法"""
        pass


class ElectricCar(Vehicle, ElectricVehicle):
    """电动汽车 - 多重继承"""
    
    def __init__(self, brand, model, battery_capacity, efficiency):
        # 初始化两个父类
        Vehicle.__init__(self, brand, model)
        ElectricVehicle.__init__(self, battery_capacity)
        self.efficiency = efficiency  # 能效(km/kWh)
        self.max_speed = 180
    
    def start_engine(self):
        """实现启动引擎"""
        if not self._is_running:
            if self.current_charge > 0:
                self._is_running = True
                print(f"{self.brand} {self.model} 电动汽车启动，静音运行")
            else:
                print("电池没电，无法启动")
        else:
            print("电机已经在运行")
    
    def stop_engine(self):
        """实现停止引擎"""
        if self._is_running:
            self._is_running = False
            print(f"{self.brand} {self.model} 电动汽车停止")
        else:
            print("电机已经停止")
    
    def get_max_speed(self):
        """实现获取最大速度"""
        return self.max_speed
    
    def charge(self, amount):
        """实现充电方法"""
        if amount > 0:
            self.current_charge = min(self.battery_capacity, self.current_charge + amount)
            print(f"充电 {amount} kWh，当前电量: {self.current_charge:.1f}/{self.battery_capacity} kWh")
        else:
            print("充电量必须大于0")
    
    def estimate_range(self):
        """实现估算续航里程"""
        return self.current_charge * self.efficiency


def vehicle_test(vehicle):
    """测试交通工具 - 演示抽象的使用"""
    print(f"\n--- 测试 {vehicle.__class__.__name__} ---")
    print(f"基本信息: {vehicle.get_info()}")
    
    # 使用抽象接口
    vehicle.start_engine()
    print(f"引擎状态: {'运行中' if vehicle.is_engine_running() else '已停止'}")
    print(f"最大速度: {vehicle.get_max_speed()} km/h")
    vehicle.stop_engine()


def abstraction_demo():
    """抽象演示"""
    print("=== 抽象 ===")
    print("只暴露必要接口，隐藏复杂实现")
    
    # 由于Vehicle是抽象类，不能直接实例化
    try:
        vehicle = Vehicle("通用", "型号")  # 这会引发TypeError
    except TypeError as e:
        print(f"无法实例化抽象类: {e}")
    
    # 创建具体实现类的实例
    car = Car("丰田", "凯美瑞", "汽油")
    motorcycle = Motorcycle("本田", "CBR", "1000cc")
    electric_car = ElectricCar("特斯拉", "Model 3", 75, 600/75)  # 600km续航，75kWh电池
    
    # 测试各种交通工具
    vehicle_test(car)
    vehicle_test(motorcycle)
    vehicle_test(electric_car)
    
    # 电动汽车特有的功能
    print(f"\n--- 电动汽车特有功能 ---")
    electric_car.charge(20)
    print(f"预估续航里程: {electric_car.estimate_range():.0f} km")


class DataProcessor(ABC):
    """数据处理器抽象基类"""
    
    @abstractmethod
    def process(self, data):
        """处理数据 - 抽象方法"""
        pass
    
    def process_batch(self, data_list):
        """批处理数据 - 具体方法"""
        results = []
        for data in data_list:
            result = self.process(data)
            results.append(result)
        return results


class NumberProcessor(DataProcessor):
    """数字处理器"""
    
    def process(self, data):
        """实现数字处理"""
        if isinstance(data, (int, float)):
            return data ** 2
        return 0


class StringProcessor(DataProcessor):
    """字符串处理器"""
    
    def process(self, data):
        """实现字符串处理"""
        if isinstance(data, str):
            return data.upper()
        return ""


def processor_demo():
    """处理器演示"""
    print("\n=== 数据处理器演示 ===")
    
    # 创建不同的处理器
    num_processor = NumberProcessor()
    str_processor = StringProcessor()
    
    # 处理单个数据
    print(f"数字处理: {num_processor.process(5)}")
    print(f"字符串处理: {str_processor.process('hello')}")
    
    # 批处理数据
    numbers = [1, 2, 3, 4, 5]
    strings = ["apple", "banana", "cherry"]
    
    print(f"数字批处理: {num_processor.process_batch(numbers)}")
    print(f"字符串批处理: {str_processor.process_batch(strings)}")


if __name__ == "__main__":
    abstraction_demo()
    processor_demo()