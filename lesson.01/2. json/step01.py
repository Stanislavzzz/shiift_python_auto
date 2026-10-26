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

json_str = json.dumps(employees)
print(json_str)
print(type(json_str))