import json


class Asserts:
    """Методы для проверки ответов отправленных запросов"""

    @staticmethod
    def assert_status_code(result, code):
        """Метод для проверки статус-кода"""
        assert result.status_code == code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def assert_json_fields(result, value):
        """Метод, проверяющий наличие обязательных полей запроса"""
        json_fields = json.loads(result.text)  # Возвращает структуру данных Python: объект JSON превращается в словарь,
        # массив — в список, строки/числа — в соответствующие типы данных.
        assert list(json_fields) == value, f"ОШИБКА, поле {list(json_fields)} отсутствует в ответе"
        print(f"Все поля  {list(json_fields)} присутствует в ответе")

    @staticmethod
    def assert_field_value(result, field, exp_value):
        """Метод, проверяющий значение указанного поля из ответа"""
        result_field = result.json().get(field)
        assert result_field == exp_value, (f"ОШИБКА, значение поля {result.json().get(field)} не соответствует ожидаемому"
                                           f" результату {exp_value}")
        print(f"Значение поля {field} = {result_field} корректно")
