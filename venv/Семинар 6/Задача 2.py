departments = [
    {"id": 10, "name": "accounting", "employees": [2, 1]},
    {"id": 11, "name": "marketing", "employees": [3]}
]

def max_id_department():
    max = 0
    for i in range(len(departments)):
        if departments[i]["id"] >= max:
            max = departments[i]["id"]
    print(max)

max_id_department()