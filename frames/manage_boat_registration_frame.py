import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat

class ManageBoatRegistrationFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # self.pack(fill="both", expand=True)
        self.place(x=0,y=0,relwidth=0.3,relheight=1)
        self.create_widgets()

    def create_widgets(self):
        self.label_entry_manager = LabelEntryManageBoat(self)

        labels_and_entries = [
            ("Boat Owner: ", 0, 0, 0, 1),
            ("Boat Name: ", 1, 0, 1, 1),
            ("Boat Captain: ", 2, 0, 2, 1),
            ("Boat Capacity: ", 3, 0, 3, 1),
            ("Boat Crew: ", 4, 0, 4, 1)
        ]

        button_info = [
            ("ADD","SEARCH",42,5,0,5,1,self.command_one,self.command_one),
            ("UPDATE","DELETE",42,6,0,6,1,self.command_one,self.command_one),
            ("SELECT","RESET",42,7,0,7,1,self.command_one,self.command_one)
        ]
        
        
        self.label_entry_manager.label_entry_manage_boat(labels_and_entries)
        self.label_entry_manager.manage_button(button_info)

        self.label_entry_manager.place(x=0,y=0,relwidth=1,relheight=1)

    def command_one(self):
        # print(self.label_entry_manager.get_entry_values())
        entry_one, entry_two, entry_three, entry_four, entry_five = self.label_entry_manager.get_entry_values()
        print(entry_one)
        print(entry_two)
        print(entry_three)
        print(entry_four)
        print(entry_five)
