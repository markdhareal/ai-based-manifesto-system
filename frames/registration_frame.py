import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat

class RegistrationFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        
        self.manage_registration = LabelEntryManageBoat(self)
        combo_value_age = ["Male", "Female"]
        combo_value_sex = ["9-10", "11-15"]

        info_labels_entries = [
            ("Name:", 0,0,0,1),
            ("Weight:", 3,0,3,1),
            ("Address:", 4,0,4,1),
            ("Contact:",5,0,5,1)
        ]

        info_labels_combo_box = [
            # Gonna put the combo box value here
            ("Age:",1,0,1,1, combo_value_age),
            ("Sex", 2,0,2,1, combo_value_sex)
        ]

        button_info_registration = [
            ("GENERATE","ADD",42,6,0,6,1,self.command_one,self.command_one),
            ("UPDATE","DELETE",42,7,0,7,1,self.command_one,self.command_one)
        ]

        self.manage_registration.label_entry_manage_boat(info_labels_entries)
        self.manage_registration.label_combo_box(info_labels_combo_box)
        self.manage_registration.manage_button(button_info_registration)

        self.manage_registration.place(x=0,y=0, relwidth=1, relheight=1)

    def command_one(self):
        print(self.manage_registration.get_combo_box_values())