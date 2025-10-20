from abc import ABC, abstractmethod


# Open/Closed Principle (OCP)

# Classes should be open for extension, but closed for modification.

# 💼 Real-World Project Example

# E-commerce platform:
# Add new discount types or coupon rules without changing core billing logic — just add new DiscountStrategy subclasses.


# ❌ Bad Example
# 🧨 You must edit this class every time a new discount type appears.
class Discount:
    def __init__(self, customer_type):
        self.customer_type = customer_type

    def get_discount(self, price):
        if self.customer_type == "Regular":
            return price * 0.1
        elif self.customer_type == "VIP":
            return price * 0.2


# ✅ Good Example (using polymorphism)

class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self, price):
        pass


class RegularDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.1


class VIPDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.2


# Extending behavior without modifying existing code
class SuperVIPDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.3

