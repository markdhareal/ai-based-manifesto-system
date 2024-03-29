import customtkinter as ctk
from utils.tree_view import MyTreeView

class ManageBoatMainFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        # ctk.CTkLabel(self,fg_color="red", height=20).pack(8)
        self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight=1)
        self.tree = MyTreeView(self)
        self.create_tree()


    def create_tree(self):
        
        info = [
            ("Boat Name"),
            ("Boat Owner"),
            ("Boat Captain"),
            ("Boat Capacity"),
            ("Boat Crew")
        ]
        
        self.tree.create_tree_view(info)
        self.tree.add_to_treeview()

        self.tree.pack(fill="both", expand=True)

        # item_values = ("John Doe", "Speedy Boat", "Captain Doe", "10", "5")
        # self.tree.add_item(item_values)
        # self.tree.add_item(item_values)
        # self.tree.add_item(item_values)
        # self.tree.add_item(item_values)
        # self.tree.add_item(item_values)
        # self.tree.add_item(item_values)
