import customtkinter as ctk
from utils.tree_view import MyTreeView

class RegistrationMainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # self.pack(fill="both", expand=True)
        # ctk.CTkLabel(self, fg_color="blue").pack(fill="both", expand=True)

        self.create_frame_camera()
        self.create_frame_tree_view()

    def create_frame_camera(self):
        
        frame = ctk.CTkFrame(self, fg_color="blue")
        # frame.pack(side="top",fill="both", expand=True)
        self.tree = MyTreeView(self)

        info = [
            ("Name"),
            ("Weight"),
            ("Age"),
            ("Address"),
            ("Contact Number")
        ]

        self.tree.create_tree_view(info)
        self.tree.pack(fill="both", expand=True)

        item_values = ("John Doe", "Speedy Boat", "Captain Doe", "10", "5")
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)

    def create_frame_tree_view(self):
        frame_2 = ctk.CTkFrame(self,)
        # frame_2.pack(fill="both", expand=True)

        self.tree = MyTreeView(self)

        info = [
            ("Name"),
            ("Weight"),
            ("Age"),
            ("Address"),
            ("Contact Number")
        ]

        self.tree.create_tree_view(info)
        self.tree.pack(fill="both", expand=True)

        item_values = ("John Doe", "Speedy Boat", "Captain Doe", "10", "5")
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)
        self.tree.add_item(item_values)