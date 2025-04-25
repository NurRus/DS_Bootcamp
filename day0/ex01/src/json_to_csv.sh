#!/bin/bash

# Получаем имя файла JSON из аргумента
JSON_FILE=$1

# Проверяем, существует ли файл JSON
if [ ! -f "$JSON_FILE" ]; then
    echo "Файл $JSON_FILE не найден."
    exit 1
fi

# Имя выходного файла CSV
CSV_FILE="hh.csv"

# Заголовки для CSV-файла
echo "id,created_at,name,has_test,alternate_url" > "$CSV_FILE"

# Используем jq для фильтрации данных и сохраняем результат в CSV-файл
jq -r -f filter.jq "$JSON_FILE" >> "$CSV_FILE"

# -r: Эта опция указывает jq выводить результат в виде строк (raw output).

# -f filter.jq: Эта опция указывает jq использовать фильтр из файла filter.jq. 
# filter.jq: < .items[] | [.id, .created_at, .name, .has_test, .alternate_url] @csv >
# .items[]: Перебирает все элементы массива items в JSON.
# [.id, .created_at, .name, .has_test, .alternate_url]: Создает массив из значений полей:
# id, created_at, name, has_test и alternate_url для каждого элемента массива items.
# @csv - это опция автоматически добавит кавычки вокруг значений и разделит их запятыми.

# >> "$CSV_FILE": Оператор перенаправления добавляет результат в конец файла CSV_FILE. 
# Это позволяет добавлять новые строки в файл hh.csv без перезаписи его содержимого.