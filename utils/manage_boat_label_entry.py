import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class LabelEntryManageBoat(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.entry_widget = []    
        self.combo_box_widget = []

        # self.pack(fill="both", expand=True)
        
    def label_entry_manage_boat(self, labels_and_entries):
        for index, (label_text, row_label, cols_label, row_entry, cols_entry) in enumerate(labels_and_entries):
            # CREATE WIDGETS
            manage_boat_label = FunctionalWidgets.create_label(self, label_text)
            manage_boat_entry = FunctionalWidgets.create_entry(self, corner_radius=2)

            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=3)

            # CREATE LAYOUT
            manage_boat_label.grid(row=row_label, column=cols_label, padx=30, pady=20, sticky="w")
            manage_boat_entry.grid(row=row_entry, column=cols_entry, padx=5, pady=20, sticky="we")

            self.entry_widget.append(manage_boat_entry)

    def label_combo_box(self, labels_and_combo_box):
        
        for index, (label_text_combo, row_label, cols_label, row_combo, cols_combo, combo_values) in enumerate(labels_and_combo_box):

            label_combo = FunctionalWidgets.create_label(self, label_text_combo)
            combo_box = FunctionalWidgets.create_combo_box(self,combo_values)

            self.columnconfigure(0, weight=1)
            self.columnconfigure(1, weight=3)

            label_combo.grid(row=row_label, column=cols_label, padx=30, pady=20, sticky="w")
            combo_box.grid(row=row_combo, column=cols_combo,padx=5, pady=20, sticky="we")

            self.combo_box_widget.append(combo_box)

    def manage_button(self, button_info):
        for i, (text_one, text_two, button_size, row_btn_one, cols_button_one,row_button_two, cols_button_two,command_one_1, command_two_2) in enumerate(button_info):
            # CREATE WIDGETS
            button_one = FunctionalWidgets.create_button(self, text_one,height=button_size, command=command_one_1)
            button_two = FunctionalWidgets.create_button(self, text_two,height=button_size, command=command_two_2)

            self.columnconfigure((0,1), weight=1)

            # CREATE LAYOUT
            button_one.grid(row=row_btn_one,column=cols_button_one,padx=20,pady=25)
            button_two.grid(row=row_button_two,column=cols_button_two,padx=20,pady=25)

    def get_entry_values(self):
        return [entry.get() for entry in self.entry_widget]
    
    def get_combo_box_values(self):
        return[combo.get() for combo in self.combo_box_widget]