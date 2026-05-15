from abc import ABC , abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay (self,amount):
        raise Exception("pay() is not implemented")
    

class CardPayment(Payment):
    def pay(self,amount):
        return f"Paid {self.amount} with card"
    
class CashPayment(Payment):
    def pay(self,amount):
        return f"Paid {self.amount} with cash"
    
card=CardPayment()
cash=CashPayment()

print(card.pay(50))
print(cash.pay(30))
