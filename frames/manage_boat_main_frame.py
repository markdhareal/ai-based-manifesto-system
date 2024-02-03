import customtkinter as ctk
from utils.tree_view import MyTreeView

class ManageBoatMainFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        # ctk.CTkLabel(self,fg_color="red").pack(fill="both", expand=True)
        self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight=1)

        self.tree = MyTreeView(self)