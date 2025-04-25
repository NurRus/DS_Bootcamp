class Research:
    def __init__(self):
        self.filename = 'data.csv'

    def file_reader(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            return content

if __name__ == "__main__":
    research = Research()
    content = research.file_reader()
    print(content)
