class LetterIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        else:
            letter = self.string[self.index].upper()
            self.index += 1
            return letter

if __name__ == '__main__':
    letters = LetterIterator("Python")
    iterator = iter(letters)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator)) 


