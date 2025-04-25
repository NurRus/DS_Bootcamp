def dictionary_sorter():
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
    multidict = dict(list_of_tuples)
    multidict = {country: int(number) for country, number in multidict.items()}

    # Сортируем словарь по значениям в порядке убывания, затем по ключам в алфавитном порядке
    sorted_countries = sorted(multidict.keys(), key=lambda x: (-multidict[x], x))

    # Вывод данных в нужном формате
    for country in sorted_countries:
        print(country)

if __name__ == '__main__':
    dictionary_sorter()
