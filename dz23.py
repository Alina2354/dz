class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percent):
        if 0 <= discount_percent <= 100:
            discounted_price = self.price * (1 - discount_percent / 100)
            return discounted_price
        else:
            print("Ошибка: Процент скидки должен быть в диапазоне от 0 до 100.")
            return self.price

class Cart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product_name):
        for product, quantity in list(self.products.items()):
            if product.name == product_name:
                del self.products[product]
                return

    def total_cost(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total


if __name__ == '__main__':
    iphone = Product("iPhone 15", 999)
    macbook = Product("MacBook Pro", 1999)

    cart = Cart()
    cart.add_product(iphone, 2)
    cart.add_product(macbook)

    print(cart.total_cost())
    cart.remove_product("iPhone 15")
    print(cart.total_cost())

