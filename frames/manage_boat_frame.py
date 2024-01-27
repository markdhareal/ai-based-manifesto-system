import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat
from utils.manage_boat_textbox import ManageBoatTextBox


class ManageBoatFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent
        self.place(x=0,y=0,relwidth=0.3,relheight=1)

        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",0,0,0,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Captain Name: ",1,0,1,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Capacity Name: ",2,0,2,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",3,0,3,1)

        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ")
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Captain Name: ")
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Capacity Name: ")
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ")

        # ManageBoatTextBox.text_box_manage_boat(self, "Boat Crews: ")