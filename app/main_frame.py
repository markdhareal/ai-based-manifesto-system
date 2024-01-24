import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, name, title):
        super().__init__()
        self.name = name
        self.title(title)
        self.state('zoomed')
        self.mainloop()

    def print_this(self):
        print(self.name)
        print(self.title)
