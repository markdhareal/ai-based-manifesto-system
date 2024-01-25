import customtkinter as ctk

class ManageBoat(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        self.title(title)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        self.geometry(f'{self.width}x{self.height}')
        self.minsize(self.width, self.height)

        self.mainloop()