def read_and_write():
    input_file = 'ds.csv'
    output_file = 'ds.tsv'

    # Функция для замены запятых на табуляцию вне кавычек
    def replace_commas(line):
        result = ''
        in_quotes = False
        for char in line:
            if char == '"':
                in_quotes = not in_quotes
            if char == ',' and not in_quotes:
                result += '\t'
            else:
                result += char
        return result

    # Чтение CSV файла и запись в TSV файл
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()

    with open(output_file, 'w', encoding='utf-8') as tsv_file:
        for line in lines:
            new_line = replace_commas(line.strip())
            tsv_file.write(new_line + '\n')

if __name__ == '__main__':
    read_and_write()

