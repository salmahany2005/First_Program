from abc import ABC, abstractmethod
class Order:
    def __init__(self, order_id, items, total_price):
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
    def get_order_details(self):
        return f"Order ID: {self.order_id}, Items: {self.items}, Total Price: {self.total_price}"
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")
def process_payment(payment_processor: PaymentProcessor, amount):
    payment_processor.process_payment(amount)
class Printable(ABC):
    @abstractmethod
    def print_details(self):
        pass

class PrintableOrder(Order, Printable):
    def print_details(self):
        print(self.get_order_details())
class OrderService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
    def complete_order(self, order: Order):
        print("Completing order...")
        self.payment_processor.process_payment(order.total_price)
        print("Order completed!")
if __name__ == "__main__":
    order = PrintableOrder(1, ["Laptop", "Mouse"], 1500)
    order.print_details()

    credit_card_payment = CreditCardPayment()
    order_service = OrderService(credit_card_payment)
    order_service.complete_order(order)

    paypal_payment = PayPalPayment()
    order_service = OrderService(paypal_payment)
    order_service.complete_order(order)


