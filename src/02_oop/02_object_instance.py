"""
Python 面向对象编程 - 对象和实例
对象是类的具体实例，拥有类定义的属性和方法
"""

class Smartphone:
    """智能手机类"""
    
    # 类属性
    operating_systems = ["Android", "iOS"]
    
    def __init__(self, brand, model, os_type):
        """初始化手机对象"""
        self.brand = brand
        self.model = model
        self.os_type = os_type
        self.is_powered_on = False
        self.apps = []
        self.battery_level = 100
    
    def power_on(self):
        """开机"""
        if not self.is_powered_on:
            self.is_powered_on = True
            print(f"{self.brand} {self.model} 开机成功")
        else:
            print(f"{self.brand} {self.model} 已经开机了")
    
    def power_off(self):
        """关机"""
        if self.is_powered_on:
            self.is_powered_on = False
            print(f"{self.brand} {self.model} 关机成功")
        else:
            print(f"{self.brand} {self.model} 已经关机了")
    
    def install_app(self, app_name):
        """安装应用"""
        if self.is_powered_on:
            if app_name not in self.apps:
                self.apps.append(app_name)
                print(f"成功安装应用: {app_name}")
            else:
                print(f"应用 {app_name} 已经安装过了")
        else:
            print("请先开机再安装应用")
    
    def show_status(self):
        """显示手机状态"""
        print(f"\n--- {self.brand} {self.model} 状态 ---")
        print(f"操作系统: {self.os_type}")
        print(f"开关机状态: {'开机' if self.is_powered_on else '关机'}")
        print(f"电池电量: {self.battery_level}%")
        print(f"已安装应用: {', '.join(self.apps) if self.apps else '无'}")


def object_demo():
    """对象实例演示"""
    print("=== 对象和实例 ===")
    print("对象是类的具体实例，每个对象都有自己的属性值")
    
    # 创建不同的手机对象
    iphone = Smartphone("Apple", "iPhone 15", "iOS")
    samsung = Smartphone("Samsung", "Galaxy S24", "Android")
    huawei = Smartphone("Huawei", "P70", "Android")
    
    # 显示初始状态
    iphone.show_status()
    samsung.show_status()
    huawei.show_status()
    
    # 操作不同的对象
    print("\n--- 操作iPhone ---")
    iphone.power_on()
    iphone.install_app("微信")
    iphone.install_app("支付宝")
    iphone.show_status()
    
    print("\n--- 操作Samsung ---")
    samsung.power_on()
    samsung.install_app("微信")
    samsung.install_app("抖音")
    samsung.show_status()
    
    print("\n--- 操作Huawei ---")
    huawei.power_on()
    huawei.install_app("华为地图")
    huawei.install_app("华为视频")
    huawei.show_status()
    
    # 验证对象的独立性
    print("\n--- 对象独立性 ---")
    print(f"iPhone品牌: {iphone.brand}")
    print(f"Samsung品牌: {samsung.brand}")
    print(f"Huawei品牌: {huawei.brand}")
    print("每个对象都有自己独立的属性值")


if __name__ == "__main__":
    object_demo()