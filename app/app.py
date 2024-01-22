
class App:
    def __init__(self, name, title):
        super().__init__()
        self.name = name
        self.title = title

    def print_this(self):
        print(self.name)
        print(self.title)