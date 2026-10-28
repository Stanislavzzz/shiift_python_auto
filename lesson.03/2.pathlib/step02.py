from pathlib import Path


path_file = Path(__file__).parent
print(path_file)

new_path = path_file / "new_data" / "new_data1" / "new_data2" / "new_data3"
print(new_path)

# new_path.mkdir(parents=True, exist_ok=True)
# new_path.mkdir(parents=True, exist_ok=True, mode=)

new_path.chmod(0o644)