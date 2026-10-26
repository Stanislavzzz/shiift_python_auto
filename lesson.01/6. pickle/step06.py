import pickle


class Employee:
    def __init__(self, name, prof):
        self.name = name
        self.prof = prof

    def print_employee(self):
        print(self.name)
        print(self.prof)


with open("employees_class.pkl", "rb") as f:
    load_data = pickle.load(f)

print(load_data)
print(type(load_data))
load_data.print_employee()