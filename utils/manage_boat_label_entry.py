import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class LabelEntryManageBoat(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)        

        self.pack(fill="both", expand=True)
        
    def label_entry_manage_boat(self, text, row_label, cols_label,row_entry, cols_entry):

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        # CREATE WIDGETS
        manage_boat_label = FunctionalWidgets.create_label(self, text)
        manage_boat_entry = FunctionalWidgets.create_entry(self, corner_radius=2)

        #CREATE LAYOUT
        manage_boat_label.grid(row=row_label,column=cols_label,padx=5, pady=20,sticky="w")
        manage_boat_entry.grid(row=row_entry,column=cols_entry,padx=5,pady=20,sticky="we")