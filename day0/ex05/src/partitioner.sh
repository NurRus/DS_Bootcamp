#!/bin/bash

input_file="../../ex03/src/hh_positions.csv"
file_names="file_names.txt"  # Имя файла для хранения имен выходных файлов
header_file="header.txt"

# Чтение заголовка
header=$(head -n 1 "$input_file")

echo "$header" > "$header_file"

# Инициализация переменных
current_date=""
output_file=""

# Функция для удаления кавычек
remove_quotes() {
    echo "$1" | tr -d '"'
}

# Чтение файла построчно, начиная со второй строки
tail -n +2 "$input_file" | while IFS=, read -r id created_at name has_test alternate_url; do
    # Извлечение даты и удаление кавычек
    date=$(remove_quotes "$created_at" | cut -d'T' -f1)

    # Если дата изменилась, создаем новый файл
    if [ "$date" != "$current_date" ]; then
        if [ -n "$output_file" ]; then
            # Закрываем текущий файл
            exec 3>&-
        fi

        # Открываем новый файл для записи
        output_file="${date}.csv"
        echo "$output_file" >> "$file_names"  # Добавляем имя файла в выходной файл
        exec 3>>"$output_file"

        # Обновляем текущую дату
        current_date="$date"
    fi

    # Записываем строку в текущий файл
    echo "$id,$created_at,$name,$has_test,$alternate_url" >&3
done

# Закрываем последний файл
exec 3>&-