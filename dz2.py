import math

def group_students(students):
    grouped_students = {}
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average_grade = math.floor(sum(grades) / len(grades))
        if average_grade in grouped_students:
            grouped_students[average_grade].append(name)
        else:
            grouped_students[average_grade] = [name]
    return grouped_students


def max_group(grouped_students):
    max_group_size = 0
    maxx_group = None
    for grade, names in grouped_students.items():
        if len(names) > max_group_size:
            max_group_size = len(names)
            maxx_group = grade

    print(maxx_group)


if __name__ == '__main__':
    students = [
        {"name": "Алексей", "grades": [4, 5, 3, 4]},
        {"name": "Мария", "grades": [5, 5, 5, 5]},
        {"name": "Иван", "grades": [3, 4, 3, 4]},
        {"name": "Ольга", "grades": [4, 4, 4, 4]},
        {"name": "Дмитрий", "grades": [2, 3, 2, 3]}
    ]
    grouped_students_result = group_students(students)
    print(grouped_students_result)
    print(max_group(grouped_students_result))
