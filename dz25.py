class Car:
    def __init__(self, model_name, year_of_manufacture, manufacturer,
                 engine_capacity, color, price):

        self.model_name = model_name
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def enter_data(self):
        self.model_name = input("Enter the model name: ")
        self.year_of_manufacture = int(input("Enter the year of manufacture: "))
        self.manufacturer = input("Enter the manufacturer: ")
        self.engine_capacity = float(input("Enter the engine capacity: "))
        self.color = input("Enter the color: ")
        self.price = float(input("Enter the price: "))

    def display_data(self):
        print("Car Information:")
        print(f"  Model Name: {self.model_name}")
        print(f"  Year of Manufacture: {self.year_of_manufacture}")
        print(f"  Manufacturer: {self.manufacturer}")
        print(f"  Engine Capacity: {self.engine_capacity}")
        print(f"  Color: {self.color}")
        print(f"  Price: {self.price}")

    def get_model_name(self):
        return self.model_name

    def set_model_name(self, model):
        self.model_name = model

    def get_year_of_manufacture(self):
        return self.year_of_manufacture

    def set_year_of_manufacture(self, year):
        self.year_of_manufacture = year

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def set_engine_capacity(self, capacity):
        self.engine_capacity = capacity

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


if __name__ == '__main__':
    car  = Car('model_name', 'year_of_manufacture', 'manufacturer',
                 'engine_capacity', 'color', 'price')
    car.enter_data()
    car.display_data()


    print(f"Model Name: {car.get_model_name()}")
    car.set_model_name("New Model Name")
    print(f"New Model Name: {car.get_model_name()}")
