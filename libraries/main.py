from currency_converter import CurrencyConverter

c = CurrencyConverter()

amount = float(input("Enter the amount in USD: "))

new_amount = c.convert(amount, 'USD', 'INR')

print(f"The amount you entered is: {new_amount}")
