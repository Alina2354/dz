class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"


if __name__ == '__main__':
    book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    print(book1.get_info())

    book2 = Book("1984", "Джордж Оруэлл", 1949)
    print(book2.get_info())
