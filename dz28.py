class MyString:
    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(self.string + other.string)
        elif isinstance(other, str):
            return MyString(self.string + other)
        else:
            raise TypeError("может быть только  строкой")

    def __mul__(self, other):
        if isinstance(other, int) and other > 0:
            return MyString(self.string * other)
        elif isinstance(other, int) and other <= 0:
            return MyString("")
        else:
            raise TypeError("можно только положительное число")

    def __lt__(self, other):
        if isinstance(other, MyString):
            return len(self.string) < len(other.string)
        elif isinstance(other, str):
            return len(self.string) < len(other)
        else:
            raise TypeError("может быть только  строкой")

    def __gt__(self, other):

        if isinstance(other, MyString):
            return len(self.string) > len(other.string)
        elif isinstance(other, str):
            return len(self.string) > len(other)
        else:
            raise TypeError("может быть только  строкой")

    def __getitem__(self, item):
        try:
            return self.string[item]
        except TypeError:
            raise TypeError("индекс должен быть числом")

    def __str__(self):
        return self.string


if __name__ == '__main__':
    str1 = MyString("Hello")
    str2 = MyString(" World")

    str3 = str1 + str2
    print(f"Конкатенация: {str3}")


class BankAccount:


    def __init__(self, balance=0):
        self.balance = balance

    def __add__(self, amount):
        if amount > 0:
            self.balance += amount
            return BankAccount(self.balance)
        else:
            raise ValueError("число должно быть положительным")

    def __sub__(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return BankAccount(self.balance)
            else:
                raise ValueError("недостаточно средств")
        else:
            raise ValueError("число должно быть положительным")

    def __iadd__(self, amount):
        if amount > 0:
            self.balance += amount
            return self
        else:
            raise ValueError("число должно быть положительным")

    def __isub__(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self
            else:
                raise ValueError("недостаточно средств")
        else:
            raise ValueError("число должно быть положительным")

    def __str__(self):
        return f"Balance: {self.balance}"


if __name__ == '__main__':
    account = BankAccount(100)

    account = account + 50
    print(account)

