class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price

    def display_data(self):
        print("Book Information:")
        print(f"  Title: {self.title}")
        print(f"  Year of Publication: {self.year}")
        print(f"  Publisher: {self.publisher}")
        print(f"  Genre: {self.genre}")
        print(f"  Author: {self.author}")
        print(f"  Price: {self.price}")
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            print("Invalid year. Year must be a positive integer.")



    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher


    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = price
        else:
            print("Invalid price. Price must be a non-negative number.")


if __name__ == '__main__':
    book = Book('title', 'year', 'publisher', 'genre', 'author', 'price')
    book.display_data()

    print("Title:", book.title)
    book.title = "A New Title"
    print("New Title:", book.title)

    book.year = 2024
    print("Year:", book.year)

    book.year = "abc"
    print("Year:", book.year)

