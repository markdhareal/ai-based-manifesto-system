import customtkinter as ctk

class RegistrationFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        ctk.CTkLabel(self, fg_color="red").pack(fill="both", expand=True)