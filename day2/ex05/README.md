### Exercise 05 : Config and the main program

Разрешенные функции: import sys, from random import randint

Теперь нужно сделать наш код еще понятнее. Нужно перенести всю логику скрипта в другой файл. И второе, переместить все
параметры в файл конфигурации. Bмпортируем файл конфигурации и файл модуля в основной скрипт программы.

То же самое в деталях:
* создайте файл с именем config.py, где будут храниться все внешние параметры, такие как num_of_steps для predict_random()
* удалите логику после блока if __name__ == ’__main__’ из скрипта из предыдущего упражнения, переименуйте этот скрипт в analytics.py
* добавьте в класс Analytics метод, который сохраняет любой заданный результат в файл с заданным расширением, например save_file(data, name of file, ‘txt’)
* создайте новый файл с именем make_report.py, где будет записана вся логика вашей программы, результат, сохраненный в файле, должен выглядеть следующим образом (могут потребоваться дополнительные методы для добавления в analytics.py):

We have made 12 observations from tossing a coin: 5 of them were tails and 7 of
them were heads. The probabilities are 41.67\% and 58.33\%, respectively. Our
forecast is that in the next 3 observations we will have: 1 tail and 2 heads.

Шаблон текста должен быть сохранен в config.py.

В этом упражнении config.py может иметь код в глобальной области видимости (для переменных).
В этом упражнении config.py и analytics.py не обязательно должны содержать блок if __name__
== ’__main__’.
