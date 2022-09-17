import json
import re


def load_file_logins() -> list:
    """
    Получаем данные из файла logins.json
    :return: list
    """
    with open("logins.json", "r", encoding="utf-8") as file_login:
        return json.load(file_login)


def get_valid_login(user_login: str) -> bool:
    """
    Проверяет, соответствует ли строка требованиям
    :param user_login: str
    :return: bool
    """
    str_reg = r"^([a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*_]).{4,}([a-zA-Z\d])$"
    regexp = re.compile(str_reg)
    m = regexp.match(user_login)
    return m is not None


def main() -> None:
    u_dict: list = load_file_logins()  # получим данные из файла json
    for each in u_dict:
        u_login = each["login"]
        valid_login: bool = get_valid_login(u_login)  # проверим каждый логин на корректность
        if valid_login:
            print(u_login, "==> корректный логин")
        else:
            print(u_login, "--> не корректный логин")


if __name__ == '__main__':
    main()
