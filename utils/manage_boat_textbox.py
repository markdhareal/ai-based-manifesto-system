import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class ManageBoatTextBox(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

    def text_box_manage_boat(self, text):

        manage_boat_label_text_box = FunctionalWidgets.create_label(self,text)
        manage_boat_text_box = FunctionalWidgets.create_text_box(self)

        manage_boat_label_text_box.pack(pady=5)
        manage_boat_text_box.pack(pady=5)