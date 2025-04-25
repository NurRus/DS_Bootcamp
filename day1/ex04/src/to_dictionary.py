def dictionary_conversion():
    list_of_tuples = [
  ('Russia', '25'),
  ('France', '132'),
  ('Germany', '132'),
  ('Spain', '178'),
  ('Italy', '162'),
  ('Portugal', '17'),
  ('Finland', '3'),
  ('Hungary', '2'),
  ('The Netherlands', '28'),
  ('The USA', '610'),
  ('The United Kingdom', '95'),
  ('China', '83'),
  ('Iran', '76'),
  ('Turkey', '65'),
  ('Belgium', '34'),
  ('Canada', '28'),
  ('Switzerland', '26'),
  ('Brazil', '25'),
  ('Austria', '14'),
  ('Israel', '12')
  ]
    # Создаем пустой словарь
    multidict = {}

    # Заполняем multidict
    for country, number in list_of_tuples:
        number = int(number)  # Преобразуем строку в целое число
        if number in multidict:
            multidict[number].append(country)  # Добавляем страну в список, если ключ уже существует
        else:
            multidict[number] = [country]  # Создаем новый список, если ключ не существует

    # Вывод данных в нужном формате
    for number, countries in multidict.items():
        for country in countries:
            print(f"'{number}' : '{country}'")

if __name__ == '__main__':
    dictionary_conversion()