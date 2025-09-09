class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __str__(self):
        return self.get_info()