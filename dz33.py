class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

if __name__ == '__main__':
    book = Book("Зерцалия", "Евгений Гаглоев", 2014, 445)