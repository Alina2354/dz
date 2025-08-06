class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity

    def display_data(self):
        print("Stadium Information:")
        print(f"  Name: {self.name}")
        print(f"  Opening Date: {self.opening_date}")
        print(f"  Country: {self.country}")
        print(f"  City: {self.city}")
        print(f"  Capacity: {self.capacity}")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    @property
    def opening_date(self):
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        self._opening_date = opening_date

    @property
    def country(self):

        return self._country

    @country.setter
    def country(self, country):
        self._country = country


    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            print("Invalid capacity. Capacity must be a positive integer.")

if __name__ == '__main__':
    stadium = Stadium('name', 'opening_date', 'country', 'city', 'capacity')
    stadium.display_data()
    print("Stadium Name:", stadium.name)
    stadium.name = "New Stadium Name"
    print("New Stadium Name:", stadium.name)
    stadium.capacity = 50000
    print("Capacity:", stadium.capacity)
    stadium.capacity = "abc"
    print("Capacity:", stadium.capacity)
