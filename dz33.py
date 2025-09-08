class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def get_description(self):
        return f"{self.title} by {self.author} ({self.year}), {self.pages} pages"
    def __str__(self):
        return self.get_description()


if __name__ == '__main__':
    book = Book("Зерцалия", "Евгений Гаглоев", 2014, 445)
    description = book.get_description()
    print(description)