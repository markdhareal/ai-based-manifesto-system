import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets
from utils.manage_boat_label_entry import LabelEntryManageBoat

class ManageBoatRegistrationFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)
        # self.label = FunctionalWidgets.create_label(self,"Gumana ka", fg_color="red").grid(row=0,column=1)
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
            ("ADD",5,0,5,1,self.command_one,self.command_one),
            ("UPDATE",6,0,6,1,self.command_one,self.command_one)
        ]
        
        
        self.label_entry_manager.label_entry_manage_boat(labels_and_entries)
        self.label_entry_manager.manage_button(button_info)

        self.label_entry_manager.place(x=0,y=0,relwidth=1,relheight=1)

        # button_one = FunctionalWidgets.create_button(self, "ADD", height=42, command=self.command_one)
        # button_two = FunctionalWidgets.create_button(self,"ADD", height=42, command=self.command_one)
        # button_three = FunctionalWidgets.create_button(self,"ADD", height=42, command=self.command_one)
        # button_four = FunctionalWidgets.create_button(self,"ADD", height=42, command=self.command_one)
        # button_five = FunctionalWidgets.create_button(self,"ADD", height=42, command=self.command_one)
        # button_six = FunctionalWidgets.create_button(self,"ADD", height=42, command=self.command_one)
        # # Add other buttons as needed
        # button_one.grid(row=5,column=0, padx=20, pady=25)
        # button_two.grid(row=5,column=1,padx=20,pady=25)
        # button_three.grid(row=6,column=0, padx=20, pady=25)
        # button_four.grid(row=6,column=1, padx=20, pady=25)
        # button_five.grid(row=7,column=0, padx=20, pady=25)
        # button_six.grid(row=7,column=1, padx=20, pady=25)
        # Grid other buttons as needed
    def command_one(self):
        print(self.label_entry_manager.get_entry_values())
