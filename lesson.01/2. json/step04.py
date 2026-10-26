import json


with open('employees.json', 'r', encoding="utf-8") as f:
    data = json.load(f)


print(data)
print(type(data))

print(data.get("members")[-1])


# employees = {
#     "department": "IT",
#     "employeesCount": 3,
#     "isRemoteTeam": True,
#     "members": [
#         {"name": "Alice", "age": 32},
#         {"name": "Bob", "age": 37},
#         {"name": "Mary", "age": 25},
#     ]
# }

