import customtkinter as ctk

class ManageBoatFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent
        self.place(x=0,y=0,relwidth=0.3,relheight=1)