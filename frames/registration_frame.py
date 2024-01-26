import customtkinter as ctk

class RegistrationFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True, padx=50, pady=50)