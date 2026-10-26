import pickle


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


with open("employees.pkl", "wb") as f:
    pickle.dump(employees, f)