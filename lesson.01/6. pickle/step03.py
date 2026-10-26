import pickle


employees = {"department", "employeesCount", "isRemoteTeam", "members"}

print(employees)
print(type(employees))

with open("employees_set.pkl", "wb") as f:
    pickle.dump(employees, f)