class Must_read:
    def __init__(self):
        self.filename = 'data.csv'

    def read_file(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            print(content)

if __name__ == "__main__":
    reader = Must_read()
    reader.read_file()
