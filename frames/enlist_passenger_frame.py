import customtkinter as ctk

class EnlistPassengerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.4, relheight=1)