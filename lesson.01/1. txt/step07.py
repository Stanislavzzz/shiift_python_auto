line_to_save = [
    "1. Привет, c++!!!\n",
    "2 Привет, Java!!!!",
    "3. Привет, Pyhon!!!!",
]


info = open('info1.txt', 'w', encoding='utf-8')

info.writelines(line_to_save)

info.close()