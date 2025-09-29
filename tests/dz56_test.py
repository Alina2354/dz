import pytest
from dz56 import count_by_department

@pytest.fixture(params=[
    (
        [
            {"name": "Иван", "department": "HR"},
            {"name": "Мария", "department": "IT"},
            {"name": "Петр", "department": "IT"},
        ],
        "IT",
        2,
    ),
    (
        [
            {"name": "Иван", "department": "HR"},
            {"name": "Мария", "department": "IT"},
            {"name": "Петр", "department": "IT"},
        ],
        "HR",
        1,
    ),
    (
        [
            {"name": "Иван", "department": "HR"},
            {"name": "Мария", "department": "IT"},
            {"name": "Петр", "department": "IT"},
        ],
        "Sales",
        0,
    ),
    ([], "IT", 0),
])
def employee_data(request):
    return request.param

def test_count_by_department(employee_data):
    employees, department, expected_count = employee_data
    actual_count = count_by_department(employees, department)
    assert actual_count == expected_count