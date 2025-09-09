class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __str__(self):
        return self.get_info()


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def get_info(self):
        return f"{super().get_info()}, {self.num_doors} doors"

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def get_info(self):
        return f"{super().get_info()}, {self.engine_capacity} engine"


if __name__ == '__main__':
    car = Car("Toyota", "Camry", 2022, 4)
    bike = Bike("Honda", "CBR600RR", 2021, 599)

    print(car.get_info())
    print(bike.get_info())

    print(car)
    print(bike)