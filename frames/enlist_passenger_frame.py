import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat
from utils.functional_widgets import FunctionalWidgets

class EnlistPassengerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.pack(side="top", fill="both", expand=True)
        # self.label = ctk.CTkLabel(self, fg_color="red").pack(fill="both", expand=True)
        self.create_widgets_enlist_passenger()

    def create_widgets_enlist_passenger(self):

        frame_one = FunctionalWidgets.create_frame(self)
        frame_two_camera = FunctionalWidgets.create_frame(self)
        frame_three_parent = FunctionalWidgets.create_frame(self)

        frame_one.pack(side="left", fill="both", expand=True)
        frame_two_camera.pack(side="left", fill="both", expand=True)
        frame_three_parent.pack(side="left", fill="both",expand=True)

        self.label_one = ctk.CTkLabel(frame_one, text="0/40",font=("Arial", 40),anchor=ctk.CENTER).pack(fill="both", expand=True)
        self.label_two = ctk.CTkLabel(frame_two_camera, fg_color="red").pack(fill="both", expand=True)
        # self.label_three = ctk.CTkLabel(frame_three_parent, fg_color="gray14").pack(fill="both", expand=True)
        


        self.manage_enlist_passenger = LabelEntryManageBoat(frame_three_parent)

        combo_value_boat = ["MB ELEVEN", "MB SEVEN", "MB SUPER8"]

        info_enlist_passenger = [
            ("Boat",0,0,0,1,combo_value_boat)
        ]

        button_info_enlist_passenger = [
            ("ENLIST","GENERATE REPORT",42,1,0,1,1,self.command_one,self.command_one),
            ("REMOVE","CLEAR",42,2,0,2,1,self.command_one,self.command_one)
        ]

        self.manage_enlist_passenger.label_combo_box(info_enlist_passenger)
        self.manage_enlist_passenger.manage_button(button_info_enlist_passenger)
        self.manage_enlist_passenger.place(x=0,y=0,relwidth=1,relheight=1)

    def command_one(self):
        print("hello")