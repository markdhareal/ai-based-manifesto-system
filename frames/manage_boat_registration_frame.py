import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat
from database import database_manager
from utils import custom_messagebox

class ManageBoatRegistrationFrame(ctk.CTkFrame):
    def __init__(self, parent, treeview):
        super().__init__(parent)

        # self.pack(fill="both", expand=True)
        self.place(x=0,y=0,relwidth=0.3,relheight=1)
        self.create_widgets()
        self.treeview = treeview

    def create_widgets(self):
        self.label_entry_manager = LabelEntryManageBoat(self)

        labels_and_entries = [
            ("Boat Name: ", 0, 0, 0, 1),
            ("Boat Owner: ", 1, 0, 1, 1),
            ("Boat Captain: ", 2, 0, 2, 1),
            ("Boat Capacity: ", 3, 0, 3, 1),
            ("Boat Crew: ", 4, 0, 4, 1)
        ]

        button_info = [
            ("ADD","SEARCH",42,5,0,5,1,self.add_or_insert,self.add_or_insert),
            ("UPDATE","DELETE",42,6,0,6,1,self.add_or_insert,self.add_or_insert),
            ("SELECT","RESET",42,7,0,7,1,self.add_or_insert,self.add_or_insert)
        ]
        
        
        self.label_entry_manager.label_entry_manage_boat(labels_and_entries)
        self.label_entry_manager.manage_button(button_info)

        self.label_entry_manager.place(x=0,y=0,relwidth=1,relheight=1)


    def add_or_insert(self):
        # print(self.label_entry_manager.get_entry_values())
        entry_one, entry_two, entry_three, entry_four, entry_five = self.label_entry_manager.get_entry_values()
        if not (entry_one and entry_two and entry_three and entry_four and entry_five):
            custom_messagebox.show_error("Error", "Please fill in all entry fields!")
        elif database_manager.name_exists(entry_one):
            custom_messagebox.show_error("Error", "Boat already exists!")
        else:
            database_manager.insert_boat(entry_one,entry_two,entry_three,entry_four,entry_five)
            self.treeview.add_to_treeview()
            custom_messagebox.show_check("Data inserted!")