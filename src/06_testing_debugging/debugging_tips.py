"""
调试技巧学习模块
"""
import logging
import pdb
import traceback


def basic_logging():
    """基本日志记录"""
    # 配置日志
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    # 不同级别的日志
    logger.debug("这是调试信息")
    logger.info("这是普通信息")
    logger.warning("这是警告信息")
    logger.error("这是错误信息")
    logger.critical("这是严重错误信息")


def exception_handling():
    """异常处理示例"""
    def divide_numbers(a, b):
        """除法运算"""
        try:
            result = a / b
            return result
        except ZeroDivisionError as e:
            print(f"除零错误: {e}")
            # 打印堆栈跟踪
            traceback.print_exc()
            return None
        except Exception as e:
            print(f"其他错误: {e}")
            return None
    
    # 测试正常情况
    print("正常除法:")
    result = divide_numbers(10, 2)
    print(f"结果: {result}")
    
    # 测试除零错误
    print("\n除零错误:")
    result = divide_numbers(10, 0)
    print(f"结果: {result}")


def debug_with_pdb():
    """使用pdb调试"""
    def calculate_average(numbers):
        """计算平均值"""
        total = 0
        count = 0
        
        for num in numbers:
            # 在这里设置断点
            # pdb.set_trace()  # 取消注释这行来进行调试
            total += num
            count += 1
        
        if count == 0:
            return 0
        
        return total / count
    
    # 测试数据
    data = [1, 2, 3, 4, 5]
    average = calculate_average(data)
    print(f"平均值: {average}")


def custom_exception():
    """自定义异常"""
    class CustomError(Exception):
        """自定义异常类"""
        def __init__(self, message, error_code=None):
            super().__init__(message)
            self.error_code = error_code
    
    def process_data(data):
        """处理数据"""
        if not data:
            raise CustomError("数据不能为空", error_code=1001)
        
        if len(data) > 100:
            raise CustomError("数据量过大", error_code=1002)
        
        return sum(data)
    
    # 测试正常情况
    try:
        result = process_data([1, 2, 3, 4, 5])
        print(f"处理结果: {result}")
    except CustomError as e:
        print(f"自定义错误: {e}, 错误代码: {e.error_code}")
    
    # 测试异常情况
    try:
        result = process_data([])
        print(f"处理结果: {result}")
    except CustomError as e:
        print(f"自定义错误: {e}, 错误代码: {e.error_code}")


if __name__ == "__main__":
    print("=== 基本日志记录 ===")
    basic_logging()
    
    print("\n=== 异常处理 ===")
    exception_handling()
    
    print("\n=== 使用pdb调试 ===")
    debug_with_pdb()
    
    print("\n=== 自定义异常 ===")
    custom_exception()