import sys

def extract_names(file_path):
    
    with open(file_path, 'r') as file:
            emails = file.read().split('\n')

    employees = []
    for email in emails:
        if email:  # Проверяем, что строка не пустая
            name, surname = email.split('@')[0].split('.')
            name = name.capitalize()
            surname = surname.capitalize()
            employees.append(f"{name}\t{surname}\t{email}")

    with open('employees.tsv', 'w') as output_file:
        output_file.write("Name\tSurname\tE-mail\n")
        output_file.write('\n'.join(employees))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <path_to_file>")
    else:
        file_path = sys.argv[1]
        extract_names(file_path)
