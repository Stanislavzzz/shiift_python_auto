import pickle


class Employee:
    def __init__(self, name, prof):
        self.name = name
        self.prof = prof

    def print_employee(self):
        print(self.name)
        print(self.prof)


employees = Employee('Bob', "IT")

print(employees)
print(type(employees))
employees.print_employee()


with open("employees_class.pkl", "wb") as f:
    pickle.dump(employees, f)