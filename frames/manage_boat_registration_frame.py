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

        manage_boat_label = FunctionalWidgets.create_label(self,"Manage Boat")
        manage_boat_label.grid(row=0,column=1)

        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Owner: ",0,0,0,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",1,0,1,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Captain: ",2,0,2,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Capacity: ",3,0,3,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Crew: ",4,0,4,1)

        LabelEntryManageBoat.button_manage_boat(self,"Click",5,0,5,1)
        LabelEntryManageBoat.button_manage_boat(self,"Click",6,0,6,1)
        LabelEntryManageBoat.button_manage_boat(self,"Click",7,0,7,1)

