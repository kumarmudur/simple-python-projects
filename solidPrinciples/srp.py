# Single Responsibility Principle (SRP)
# A class should have only one reason to change.

# Bad Example,
# Problem: The Invoice class does both business logic and presentation (printing).
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount * 1.18  # tax

    def print_invoice(self):
        print(f"Invoice total: {self.calculate_total()}") # handles printing


# Good Example
class Invoice1:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount * 1.18  # tax


class InvoicePrinter:
    def print_invoice(self, invoice: Invoice):
        print(f"Invoice total: {invoice.calculate_total()}")


# Each class has one job:
# Invoice: calculates data
# InvoicePrinter: handles display

# 💼 Real-World Project Example
# InvoiceCalculator (handles tax, discounts)
# InvoicePrinter (handles output)
# InvoiceRepository (handles database storage)
