import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat

class EnlistPassengerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets_enlist_passenger()

    def create_widgets_enlist_passenger(self):
        self.manage_enlist_passenger = LabelEntryManageBoat(self)

        combo_value_boat = ["MB ELEVEN", "MB SEVEN", "MB SUPER8"]

        info_enlist_passenger = [
            ("Boat",0,0,0,1,combo_value_boat)
        ]

        self.manage_enlist_passenger.label_combo_box(info_enlist_passenger)
        self.manage_enlist_passenger.place(x=0, y=0, relwidth=1, relheight=1)