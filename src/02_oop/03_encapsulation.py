"""
Python 面向对象编程 - 封装
将数据和操作数据的方法绑定在一起，隐藏内部实现细节
"""

class BankAccount:
    """银行账户类 - 演示封装概念"""
    
    def __init__(self, account_holder, initial_balance=0):
        """
        初始化银行账户
        :param account_holder: 账户持有人
        :param initial_balance: 初始余额
        """
        # 使用双下划线前缀表示私有属性
        self.__account_holder = account_holder  # 私有属性
        self.__balance = initial_balance        # 私有属性
        self.__transaction_history = []         # 私有属性
        self._account_number = self._generate_account_number()  # 受保护属性
    
    def _generate_account_number(self):
        """生成账户号码 - 受保护方法"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def deposit(self, amount):
        """存款方法 - 公共接口"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +{amount}")
            print(f"成功存入 {amount} 元，当前余额: {self.__balance} 元")
        else:
            print("存款金额必须大于0")
    
    def withdraw(self, amount):
        """取款方法 - 公共接口"""
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"取款: -{amount}")
            print(f"成功取出 {amount} 元，当前余额: {self.__balance} 元")
            return True
        else:
            print("余额不足")
            return False
    
    def get_balance(self):
        """查询余额 - 公共接口"""
        return self.__balance
    
    def get_account_info(self):
        """获取账户信息 - 公共接口"""
        return {
            "account_holder": self.__account_holder,
            "account_number": self._account_number,
            "balance": self.__balance
        }
    
    def __validate_transaction(self, amount):
        """验证交易 - 私有方法"""
        # 私有方法只能在类内部使用
        return amount > 0 and amount <= self.__balance
    
    def transfer(self, target_account, amount):
        """转账方法"""
        if self.__validate_transaction(amount):
            if self.withdraw(amount):
                target_account.deposit(amount)
                print(f"成功转账 {amount} 元到账户 {target_account._account_number}")
        else:
            print("转账失败，余额不足或金额无效")


class EnhancedBankAccount(BankAccount):
    """增强版银行账户 - 演示受保护属性和方法的访问"""
    
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.__interest_rate = 0.02  # 私有属性
    
    def add_interest(self):
        """添加利息"""
        # 可以访问父类的受保护属性
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"添加利息 {interest:.2f} 元")


def encapsulation_demo():
    """封装演示"""
    print("=== 封装 ===")
    print("封装将数据和操作数据的方法绑定在一起，隐藏内部实现细节")
    
    # 创建银行账户
    account1 = BankAccount("张三", 1000)
    account2 = BankAccount("李四", 500)
    
    # 通过公共接口操作对象
    print(f"\n{account1.get_account_info()['account_holder']} 的账户信息:")
    print(f"账户号码: {account1.get_account_info()['account_number']}")
    print(f"账户余额: {account1.get_balance()} 元")
    
    # 存款和取款操作
    account1.deposit(500)
    account1.withdraw(200)
    
    # 尝试直接访问私有属性（这会导致错误）
    try:
        print(account1.__balance)  # 这会引发AttributeError
    except AttributeError as e:
        print(f"无法直接访问私有属性: {e}")
    
    # 通过公共接口转账
    account1.transfer(account2, 300)
    
    # 显示最终状态
    print(f"\n转账后 {account1.get_account_info()['account_holder']} 余额: {account1.get_balance()} 元")
    print(f"转账后 {account2.get_account_info()['account_holder']} 余额: {account2.get_balance()} 元")
    
    # 演示增强版账户
    print("\n--- 增强版账户演示 ---")
    enhanced_account = EnhancedBankAccount("王五", 2000)
    enhanced_account.add_interest()


if __name__ == "__main__":
    encapsulation_demo()