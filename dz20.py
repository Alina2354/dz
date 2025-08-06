class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Номер студенческого билета: {self.student_id}")


if __name__ == '__main__':
    student1 = Student("Алексей", 20, "12345")
    student1.display_info()

    student2 = Student("Мария", 22, "67890")
    student2.display_info()
