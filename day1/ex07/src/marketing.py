import sys

# Списки учетных записей электронной почты
clients = [
    'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com'
]
participants = [
    'walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
]
recipients = [
    'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
]

def call_center():
    client_set = set(clients)
    recipients_set = set(recipients)
    return(client_set - recipients_set)

def potential_clients():
    clients_set = set(clients)
    participants_set = set(participants)
    return(participants_set - clients_set)

def loyalty_program():
    client_set = set(clients)
    participants_set = set(participants)
    return(client_set - participants_set.intersection(clients))

def main():
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")

    task = sys.argv[1]

    if task == "call_center":
        result = call_center()
    elif task == "potential_clients":
        result = potential_clients()
    elif task == "loyalty_program":
        result = loyalty_program()
    else:
        raise Exception("Invalid task name")

    for email in result:
        print(email)

if __name__ == '__main__':
    main()