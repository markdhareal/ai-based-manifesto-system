import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class LabelEntryManageBoat(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)        

        # self.pack(fill="both", expand=True)
        
    def label_entry_manage_boat(self, text, row_label, cols_label,row_entry, cols_entry):
        
        # CREATE WIDGETS
        manage_boat_label = FunctionalWidgets.create_label(self, text)
        manage_boat_entry = FunctionalWidgets.create_entry(self, corner_radius=2)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        #CREATE LAYOUT
        manage_boat_label.grid(row=row_label,column=cols_label,padx=30, pady=20,sticky="w")
        manage_boat_entry.grid(row=row_entry,column=cols_entry,padx=5,pady=20,sticky="we")

    def button_manage_boat(self, text, row_btn_one, cols_button_one,row_button_two, cols_button_two):

        button_one = FunctionalWidgets.create_button(self, text, height=42)
        button_two = FunctionalWidgets.create_button(self,text, height=42)


        button_one.grid(row=row_btn_one,column=cols_button_one, padx=20, pady=25)
        button_two.grid(row=row_button_two,column=cols_button_two,pady=25)

