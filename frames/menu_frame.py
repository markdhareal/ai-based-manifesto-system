# MENU FOR MAIN FRAME
import customtkinter as ctk
from PIL import Image, ImageTk
from utils.functional_widgets import FunctionalWidgets
from app.manage_boat_app import ManageBoat

class MenuFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.2, relheight = 1)

        self.create_widgets()

    def create_widgets(self):

        # IMAGES FOR BUTTONS
        boat_image = ctk.CTkImage(Image.open("images/boat.png"))
        passenger_image = ctk.CTkImage(Image.open("images/registration.png"))
        face_recognition_image = ctk.CTkImage(Image.open("images/face-recognition.png"))

        # CREATE WIDGETS
        manage_boat_button = FunctionalWidgets.create_button(self, "Manage Boat", height=42,image=boat_image, compound="left", anchor="w", command=self.go_to_manage_boat_app)
        manage_passengers_button = FunctionalWidgets.create_button(self, "Registration", height=45, image=passenger_image, compound="left", anchor="w")
        enlist_button = FunctionalWidgets.create_button(self, "Enlist Passenger", height=45, image=face_recognition_image, compound="left", anchor="w")

        #CREATE LAYOUT
        manage_boat_button.pack(side="top", expand=True)
        manage_passengers_button.pack(side="top", expand=True)
        enlist_button.pack(side="top", expand=True)

    def go_to_manage_boat_app(self):
        self.manage_boat = ManageBoat("Manage Boat")