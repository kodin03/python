

# Вычислить число c заданной точностью d

"""print("Задача про точность числа: ")
d = float(input("Задайте точность: "))
pi = 3.141592653589793238462643

def accurary(d):
    num = 0
    if d < 0:
        print("Введена отрицательная точность. Задайте положительную")
    else:
        while d < 1:
            d *= 10
            num += 1
        print(format(pi, "." + str(num) + "f"))

accurary(d)"""




employees = [
    {"id": 1, "fio": "ivan petrov", "salary": 40},
    {"id": 2, "fio": "bob ivanov", "salary": 50},
    {"id": 3, "fio": "john don", "salary": 100}
]

departments = [
    {"id": 10, "name": "accounting", "employees": [2, 1]},
    {"id": 11, "name": "marketing", "employees": [3]}

]

id = int(input())

"""def move_employee(id):
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


move_employee(id)"""
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



dissmiss_employee(id)
