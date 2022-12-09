from models import *
import ui.ui_controller

def show_departments():
    for department in departments:
        print(department)


def show_employees():
    for employee in employees:
        print(employee)

def show_employees_in_department():
    department_id = int(input("Введите id отдела: "))
    if id == 0:
        print("Введен некорректный id")
    else:
        department = [d for d in departments if d["id"] == department_id][0]
        print("empolyees ids: ", department["employees"])


def menu():
    for key, item in ui.ui_controller.MENU_ACTIONS.items():  # [(1, "..."), (2, "....")... ]
        print(key, item[0])

    return int(input("Выберите пункт меню: "))


def input_department():
    return input("Введите название отдела: ")

def input_employee():
    return input("Введите ФИО сотрудника: ")

def input_move_employee():
    return int(input("Введите номер сотрудника для перемещения: "))

def input_dismiss_employee():
    return int(input("Введите номер сотрудника для увольнения: "))