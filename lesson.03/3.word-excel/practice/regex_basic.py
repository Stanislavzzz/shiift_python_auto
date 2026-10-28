import re


text = "Сотрудники: EMP-0001, EMP-0011 и EMP-0018."

pattern = r"EMP-[0-9]{4}"

# print(f"Текст: {text}")
# print(f"Шаблона {pattern}")
# print("*" * 10)
#
# fist_match = re.search(pattern, text)
#
# if fist_match:
#     print(f"Первый найденный код:  {fist_match.group()}")
# else:
#     print("Код не найден")
#
#
# all_codes = re.findall(pattern, text)
# print(f"Все коды:  {all_codes}")
#
#
# correct_code = "EMP-0001"
# wrong_code = "Код: EMP-0001"
#
# result_ok = re.fullmatch(pattern, correct_code) is not None
# result_wrong = re.fullmatch(pattern, wrong_code) is not None
# print(result_ok)
# print(result_wrong)


# raw_department = "Отдел           разработки     ПО\n"
# # \s+
#
#
# clean_department = re.sub(r"\s+", " ", raw_department)
# print(raw_department)
# print(clean_department)


phone_pattern = r"\+7 \(9[0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2}"

phone_ok = "+7 (901) 201-01-07"
phone_wrong = "8 (901) 201-01-07"

print(re.fullmatch(phone_pattern, phone_ok) is not None)
print(re.fullmatch(phone_pattern, phone_wrong) is not None)