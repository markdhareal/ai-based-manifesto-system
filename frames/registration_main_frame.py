import customtkinter as ctk

class RegistrationMainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        ctk.CTkLabel(self, fg_color="blue").pack(fill="both", expand=True)