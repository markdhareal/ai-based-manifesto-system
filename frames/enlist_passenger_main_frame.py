import customtkinter as ctk
from utils.tree_view import MyTreeView

class EnlistPassengerMainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        self.create_treeview_enlist_passenger_main()
        # self.label = ctk.CTkLabel(self, fg_color="red").pack(fill="both", expand=True)

    def create_treeview_enlist_passenger_main(self):
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