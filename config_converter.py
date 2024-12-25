import json
import re
import sys

# Функция для преобразования значения в формат учебного конфигурационного языка
def convert_value(value):
    if isinstance(value, dict):
        return convert_dict(value)
    elif isinstance(value, list):
        return convert_array(value)
    elif isinstance(value, str):
        return value
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        raise ValueError("Неизвестный тип данных")

# Преобразование массива
def convert_array(array):
    return "#(" + " ".join(convert_value(item) for item in array) + " )"

# Преобразование словаря
def convert_dict(dct):
    result = "{\n"
    for key, value in dct.items():
        if not re.match(r'^[a-z]+$', key):  # Проверка на корректность имени
            raise ValueError(f"Неверное имя: {key}")
        result += f"  {key} = {convert_value(value)}\n"
    result += "}"
    return result

# Преобразование объявления константы
def convert_constant(name, value):
    if not re.match(r'^[a-z]+$', name):
        raise ValueError(f"Неверное имя для константы: {name}")
    return f"{name} := {convert_value(value)};"

# Преобразование вычисления константы
def convert_computation(name):
    if not re.match(r'^[a-z]+$', name):
        raise ValueError(f"Неверное имя для вычисления: {name}")
    return f"@[{name}]"

# Основная функция для преобразования JSON в конфигурационный язык
def json_to_config(json_data):
    try:
        parsed_json = json.loads(json_data)
        if isinstance(parsed_json, dict):
            return convert_dict(parsed_json)
        elif isinstance(parsed_json, list):
            return convert_array(parsed_json)
        else:
            return convert_value(parsed_json)
    except ValueError as e:
        return f"Ошибка: {e}"

# Тесты с примерами
def run_tests():
    test_1 = '{"name": "John", "age": 30, "city": "New York"}'
    test_2 = '[1, 2, 3, 4]'
    test_3 = '{"config": {"host": "localhost", "port": 8080}, "services": [{"name": "service1", "enabled": true}]}'

    print("Тест 1:")
    print(json_to_config(test_1))
    print("Тест 2:")
    print(json_to_config(test_2))
    print("Тест 3:")
    print(json_to_config(test_3))

if __name__ == "__main__":
    input_data = sys.stdin.read()
    print(json_to_config(input_data))
