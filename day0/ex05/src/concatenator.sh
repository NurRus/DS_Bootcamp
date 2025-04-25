#!/bin/bash

file_names="file_names.txt"
header="header.txt"
input_file="../../ex03/src/hh_positions.csv"

# Объединение файлов в один
output_combined="combined.csv"

cat "$header" > "$output_combined"

while IFS= read -r file; do    
    cat "$file" >> "$output_combined"
done < "$file_names"

echo "Файлы объединены в $output_combined"

# Сравнение исходного файла и склеенного файла
diff "$input_file" "$output_combined" > diff_output.txt

if [ -s diff_output.txt ]; then
    echo "Файлы различаются. Различия сохранены в diff_output.txt"
else
    echo "Файлы идентичны"
    rm diff_output.txt  # Удаляем файл с различиями, если файлы идентичны
fi
