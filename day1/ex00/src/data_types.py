def data_types():
    # Объявление переменных различных типов
    int_var: int = 10
    str_var: str = "Hello"
    float_var: float = 3.14
    bool_var: bool = True
    list_var: list = [1, 2, 3]
    dict_var: dict = {"key": "value"}
    tuple_var: tuple = (1, 2, 3)
    set_var: set = {1, 2, 3}

    # Список переменных
    variables = [int_var, str_var, float_var, bool_var, list_var, dict_var, tuple_var, set_var]

    # Получение типов переменных
    types = [type(var).__name__ for var in variables]

    # Вывод типов на стандартный вывод
    print(types)

if __name__ == '__main__':
    data_types()
