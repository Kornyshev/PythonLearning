"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from abc import abstractmethod
from abc import ABC


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        ...


class MorningDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.25


class ElderDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9


class Order:
    def __init__(self, price, strategy: DiscountStrategy):
        self.price = price
        self._discount_strategy = strategy

    @property
    def discount_strategy(self) -> DiscountStrategy:
        return self._discount_strategy

    @discount_strategy.setter
    def discount_strategy(self, strategy: DiscountStrategy) -> None:
        self._discount_strategy = strategy

    def final_price(self):
        return self.price - self._discount_strategy.apply_discount(self.price)


if __name__ == '__main__':
    order_1 = Order(100, MorningDiscount())
    assert order_1.final_price() == 75

    order_1.discount_strategy = ElderDiscount()
    assert order_1.final_price() == 10
