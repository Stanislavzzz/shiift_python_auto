import re


EMAIL_PATTERN = r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_PATTERN = r"\+7 \(9[0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2}"
EMPLYEE_CODE_PATTERN = r"EMP-[0-9]{4}"


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    return re.fullmatch(EMAIL_PATTERN, email) is not None


def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    return re.fullmatch(PHONE_PATTERN, phone) is not None


def is_valid_employee_code(code):
    if not isinstance(code, str):
        return False
    return re.fullmatch(EMPLYEE_CODE_PATTERN, code) is not None


if __name__ == '__main__':
    print(is_valid_email("bob.ivanov.001@gmail.com"))
    print(is_valid_email("bob@ivanov.001@gmail.com"))
    print(is_valid_employee_code("EMP-11"))
    print(is_valid_employee_code("EMP-1234"))
    print(is_valid_phone("+7 (901) 201-01-07"))
    print(is_valid_phone("+7 901) 201-01-07"))

