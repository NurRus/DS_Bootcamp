### Exercise 02 : Search by key

Разрешенные функции: import sys

* Необходимо скопировать в одну из своих функций следующие словари:

        COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

        STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

* Напишите программу, которая принимает название компании (например, Apple) в качестве аргумента и выводит цену акций (например, 287.73) на стандартный вывод. Если вы дадите программе компанию, которая не из словаря, в качестве аргумента, ваш
скрипт должен вывести Unknown company. Если аргументов нет или их слишком много, ваша программа не должна ничего делать и завершить работу.

        $> python3 stock_prices.py tesla
        724.88
        $> python3 stock_prices.py Facebook
        Unknown company
        $> python3 stock_prices.py Tesla Apple