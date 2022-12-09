

employees = [
    {"id": 1, "fio": "ivan petrov", "salary": 40},
    {"id": 2, "fio": "bob ivanov", "salary": 50},
    {"id": 3, "fio": "john don", "salary": 100}
]

departments = [
    {"id": 10, "name": "accounting", "employees": [2, 1]},
    {"id": 11, "name": "marketing", "employees": [3]}
]

def max_id_department():
    max = 0
    for i in range(len(departments)):
        if departments[i]["id"] >= max:
            max = departments[i]["id"]
    return max

def max_id_employees():
    max = 0
    for i in range(len(employees)):
        if employees[i]["id"] >= max:
            max = employees[i]["id"]
    return max

def add_department(name):
    departments.append({
        "id": max_id_department() + 1,
        "name": name,
        "employees": []
    })

def add_employee(fio):
    employees.append({
        "id": max_id_employees() + 1,
        "fio": fio,
        "salary": 0
    })

def move_employee(id):
    for i in range(len(departments)):
        list = departments[i]["employees"]
        for j in range(len(list)):

            if (list[j] == id) and (i + 1 < len(departments)):
                departments[i + 1]["employees"].append(id)
                list.pop(j)
                break
            elif (list[j] == id) and (i - 1 >= 0):
                departments[i - 1]["employees"].append(id)

                list.pop(j)
                break
            elif (len(departments) == 1): print("Всего один отдел. Добавьте еще один для перемещения")


def dissmiss_employee(id):
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            del employees[i]
            break
    for i in range(len(departments)):
        list = departments[i]["employees"]
        for j in range(len(list)):
            if list[j] == id:
                list.pop(j)
                break
