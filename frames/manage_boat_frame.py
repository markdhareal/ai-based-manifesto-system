import customtkinter as ctk
from frames.manage_boat_registration_frame import ManageBoatRegistrationFrame


class ManageBoatFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.place(x=0,y=0,relwidth=0.3,relheight=1)

        self.frame = ManageBoatRegistrationFrame(self)

        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Owner: ",0,0,0,1)
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",1,0,1,1)
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Captain: ",2,0,2,1)
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Capacity: ",3,0,3,1)
        # LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Crew: ",4,0,4,1)

        # ManageBoatTextBox.text_box_manage_boat(self, "Boat Crews: ")