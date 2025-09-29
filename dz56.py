def count_by_department(employees, department):
    count = 0
    for employee in employees:
        if employee['department'] == department:
            count += 1
    return count