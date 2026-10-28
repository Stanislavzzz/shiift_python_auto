from pathlib import Path


path_file = Path("data/temp.txt")
path_dir = Path("data")
path_file123 = Path("data/temp123.txt")


# print(path_file.name)
# print(path_file.parent)
# print(path_file.resolve())
# print(path_file.exists())
# print(path_file123.exists())
print(path_file.is_file())
print(path_file.is_dir())

print("*" * 10)
# print(path_dir.name)
# print(path_dir.parent)
# print(path_dir.resolve().parent.parent.parent)
# print(path_dir.exists())
print(path_dir.is_file())
print(path_dir.is_dir())


if path_file123.exists():
    if path_file.is_file():
        print("Это файла")
    if path_file.is_dir():
        print("Это директория")