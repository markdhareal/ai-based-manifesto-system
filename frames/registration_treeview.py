import customtkinter as ctk
from utils.tree_view import MyTreeView

class RegistrationTreeview(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.create_widgets_registration_treeview()

        self.pack(side="top",fill="both")

    def create_widgets_registration_treeview(self):
        self.tree = MyTreeView(self)

        info = [
            ("Name"),
            ("Age"),
            ("Weight"),
            ("Sex"),
            ("Address"),
            ("Contact Number")
        ]

        self.tree.create_tree_view(info)
        self.tree.pack(fill="both", expand=True)

        item_values = ("Tristan Stephen Nido", "11-15", "49", "Male", "Bangad", "00000000000")
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)