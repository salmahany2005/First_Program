class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_details(self):
        return f"Product: {self.name}, Price: {self.price}"
class Discount:
    def apply_discount(self, price):
        raise 
NotImplementedError("Subclasses must implement apply_discount")
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage
    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)
class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount
    def apply_discount(self, price):
        return max(0, price - self.amount)
def calculate_final_price(product: Product, discount: Discount):
    return discount.apply_discount(product.price)
class Printable:
    def print_details(self):
        raise NotImplementedError("Subclasses must implement print_details")
class PrintableProduct(Product, Printable):
    def print_details(self):
        print(self.get_details())
class CheckoutService:
    def __init__(self, discount: Discount):
        self.discount = discount
    def checkout(self, product: Product):
        final_price = self.discount.apply_discount(product.price)
        print(f"Final price after discount: {final_price}")
