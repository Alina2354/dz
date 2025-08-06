class Car:
    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year}), Пробег: {self.mileage} км"


if __name__ == '__main__':
    car = Car("Toyota", "Camry", 2020)
    car.drive(150)
    print(car.display_info())

    car2 = Car("BMW", "X5", 2022, 10000)
    car2.drive(500)
    print(car2.display_info())
