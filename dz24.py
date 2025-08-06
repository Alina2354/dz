class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Название: {self.title}, Описание: {self.description}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)


    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return

    def show_tasks(self):
        if self.tasks:
            print("Список задач:")
            for task in self.tasks:
                print(task)
        else:
            print("Список задач пуст.")


if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task(Task("Полить цветы", "До 18:00"))
    manager.add_task(Task("Купить продукты", "Молоко, хлеб"))
    manager.complete_task("Полить цветы")
    manager.show_tasks()
