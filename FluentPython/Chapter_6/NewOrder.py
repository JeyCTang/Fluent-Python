from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # contents
    def __init__(self, customer, cart, demo, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.demo = demo

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return '<Order total: {:05.2f} due: {:05.2f}>'.format(self.total(), self.due())

    def test(self):
        print(type(self.customer))
        print(self.customer)
        print(type(self.demo))
        print(self.demo)


def fidelity_promo(order):
    """provide 5% discount for customer who has 1000 or above fidelity"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """provide 10% discount for customer who purchase 20 or above single items"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """provide 7% discount for customer who purchase 10 or above various items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .7
    return 0


def best_promo(order):
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart_1 = [
        LineItem("banana", 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)
    ]
    print(Order(joe, cart_1, fidelity_promo))
    print(Order(ann, cart_1, fidelity_promo))

    banana_cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5),
    ]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart_1, large_order_promo))

    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart_1, best_promo))
