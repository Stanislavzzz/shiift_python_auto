import json


employees = {
    "department": "IT",
    "employeesCount": 3,
    "isRemoteTeam": True,
    "members": [
        {"name": "Alice", "age": 32},
        {"name": "Bob", "age": 37},
        {"name": "Mary", "age": 25},
    ]
}

print(employees)
print(type(employees))


with open('employees1.json', 'w', encoding="utf-8") as f:
    # json.dump(employees, f)
    json.dump(employees, f, indent=4, ensure_ascii=False)

