import sys

def generate_letter(email):
    with open('employees.tsv', 'r') as file:
        lines = file.readlines()
    
    for line in lines[1:]:
        parts = line.strip().split('\t')
        if len(parts) == 3:
            name, surname, email_person = parts
            if email_person == email:
                return f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you.That’s a precondition for the professionals that our company hires."
    
    return "Email address not found."

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: python letter_starter.py <email_address>")
    else:
        email = sys.argv[1]
        letter = generate_letter(email)
        print(letter)