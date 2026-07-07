
from abc import ABC,abstractmethod
class abstract_demo(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def display2(self):
        pass
class demo(abstract_demo):
    def display(self):
        print(f"implementation done 1")
    def display2(self):
        print(f"implementation 2 done")
    def display3(self):
        print(f"add on")
obj = demo()
obj.display()
obj.display2()

from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class gpay(payment):
    def pay(self):
        print(f"payment has received 1")

class cred(payment):
    def pay(self):
        print(f"payment has received 2")

class supermoney(payment):
    def pay(self):
        print(f"payment has received 3")


obj = gpay()
obj.pay()

obj2= cred()
obj2.pay()

obj3 = supermoney()
obj3.pay()
