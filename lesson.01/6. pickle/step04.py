import pickle


with open("employees_set.pkl", "rb") as f:
    load_data = pickle.load(f)

print(load_data)
print(type(load_data))