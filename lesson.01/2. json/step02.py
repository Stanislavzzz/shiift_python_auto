import json


str_json = """{"department": "IT", "employeesCount": 3, "isRemoteTeam": true, "members": [{"name": "Alice", "age": 32}, {"name": "Bob", "age": 37}, {"name": "Mary", "age": 25}]}"""
print(str_json)
print(type(str_json))

data = json.loads(str_json)
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

