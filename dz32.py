class Bookshelf:

    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = list(books)

    def __getitem__(self, key):
        if isinstance(key, int):
            try:
                return self.books[key]
            except IndexError:
                raise IndexError("число должно быть не больше количества")
        elif isinstance(key, slice):
            return Bookshelf(self.books[key])
        else:
            raise TypeError("должно быть число")

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Bookshelf with {len(self)} books"

    def add_book(self, book):
        self.books.append(book)



if __name__ == '__main__':
    book1 = "The Lord of the Rings"
    book2 = "Pride and Prejudice"
    book3 = "1984"
    book4 = "To Kill a Mockingbird"

    shelf = Bookshelf([book1, book2, book3, book4])

    print(f"Количество книг на полке: {len(shelf)}")
    print(f"Книга по индексу 1: {shelf[1]}")


