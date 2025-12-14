"""
多线程编程学习模块
"""
import threading
import time
import queue


def basic_threading():
    """基本多线程示例"""
    def worker(name, duration):
        """工作函数"""
        print(f"线程 {name} 开始工作")
        time.sleep(duration)
        print(f"线程 {name} 工作完成")
    
    # 创建线程
    thread1 = threading.Thread(target=worker, args=("Worker-1", 2))
    thread2 = threading.Thread(target=worker, args=("Worker-2", 3))
    
    # 启动线程
    thread1.start()
    thread2.start()
    
    # 等待线程完成
    thread1.join()
    thread2.join()
    
    print("所有线程完成")


def thread_synchronization():
    """线程同步示例"""
    # 共享资源
    counter = 0
    counter_lock = threading.Lock()
    
    def increment_counter(name, iterations):
        """增加计数器"""
        global counter
        for i in range(iterations):
            with counter_lock:  # 使用锁保护共享资源
                temp = counter
                time.sleep(0.0001)  # 模拟一些处理时间
                counter = temp + 1
                print(f"{name}: {counter}")
    
    # 创建多个线程同时修改计数器
    threads = []
    for i in range(3):
        t = threading.Thread(target=increment_counter, args=(f"Thread-{i}", 5))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    print(f"最终计数: {counter}")


def producer_consumer():
    """生产者-消费者模式"""
    # 创建队列
    q = queue.Queue(maxsize=10)
    
    def producer(name, count):
        """生产者"""
        for i in range(count):
            item = f"{name}-item-{i}"
            q.put(item)
            print(f"生产者 {name} 生产了 {item}")
            time.sleep(0.5)
        
        # 发送结束信号
        q.put(None)
        print(f"生产者 {name} 完成")
    
    def consumer(name):
        """消费者"""
        while True:
            item = q.get()
            if item is None:
                # 收到结束信号，重新放入队列供其他消费者使用
                q.put(None)
                break
            
            print(f"消费者 {name} 消费了 {item}")
            time.sleep(1)
        
        print(f"消费者 {name} 完成")
    
    # 创建生产者和消费者线程
    producer_thread = threading.Thread(target=producer, args=("Producer-1", 5))
    consumer_threads = []
    for i in range(2):
        t = threading.Thread(target=consumer, args=(f"Consumer-{i}",))
        consumer_threads.append(t)
    
    # 启动所有线程
    producer_thread.start()
    for t in consumer_threads:
        t.start()
    
    # 等待所有线程完成
    producer_thread.join()
    for t in consumer_threads:
        t.join()


class Counter:
    """线程安全的计数器"""
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        """增加计数"""
        with self._lock:
            self._value += 1
            return self._value
    
    @property
    def value(self):
        """获取当前值"""
        return self._value


def thread_safe_counter():
    """线程安全计数器示例"""
    counter = Counter()
    
    def worker(name, increments):
        """工作线程"""
        for i in range(increments):
            new_value = counter.increment()
            print(f"{name} 增加计数至 {new_value}")
            time.sleep(0.01)
    
    # 创建多个线程
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"Thread-{i}", 10))
        threads.append(t)
        t.start()
    
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    print(f"最终计数值: {counter.value}")


if __name__ == "__main__":
    print("=== 基本多线程 ===")
    basic_threading()
    
    print("\n=== 线程同步 ===")
    thread_synchronization()
    
    print("\n=== 生产者-消费者模式 ===")
    producer_consumer()
    
    print("\n=== 线程安全计数器 ===")
    thread_safe_counter()