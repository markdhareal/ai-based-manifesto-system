import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets
from utils.manage_boat_label_entry import LabelEntryManageBoat

class ManageBoatFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent
        self.place(x=0,y=0,relwidth=0.3,relheight=1)

        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",0,0,0,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Captain Name: ",1,0,1,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Capacity Name: ",2,0,2,1)
        LabelEntryManageBoat.label_entry_manage_boat(self,"Boat Name: ",3,0,3,1)

        #self.create_widgets_manage_boat()

    # def create_widgets_manage_boat(self):

    #     self.column
        
    #     boat_name_label = FunctionalWidgets.create_label(self,"Boat Name: ").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    #     captain_name_label = FunctionalWidgets.create_label(self,"Captain: ").grid(row=4, column=0,sticky="w", padx=5, pady=5)
    #     capacity_label = FunctionalWidgets.create_label(self,"Capacity: ").grid(row=5, column=0,sticky="w", padx=5, pady=5)

    #     boat_name_entry = FunctionalWidgets.create_entry(self).grid(row=3,column=1)
    #     captain_name_entry = FunctionalWidgets.create_entry(self).grid(row=4,column=1)
    #     capacity_label = FunctionalWidgets.create_entry(self).grid(row=5, column=1)