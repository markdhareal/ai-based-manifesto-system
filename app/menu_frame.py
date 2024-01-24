# MENU FOR MAIN FRAME
import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.2, relheight = 1)

        self.create_widgets()

    def create_widgets(self):

        # CREATE WIDGETS
        manage_boat_button = FunctionalWidgets.create_button(self, "Manage Boat", height=42)
        manage_passengers_button = FunctionalWidgets.create_button(self, "Manage Passengers", height=45)
        enlist_button = FunctionalWidgets.create_button(self, "Enlist Passenger", height=45)

        #CREATE LAYOUT
        manage_boat_button.pack(side="top", expand=True)
        manage_passengers_button.pack(side="top", expand=True)
        enlist_button.pack(side="top", expand=True)