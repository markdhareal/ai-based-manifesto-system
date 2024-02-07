import customtkinter as ctk
from utils.functional_widgets import FunctionalWidgets

class RegistrationCamera(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets_registration_camera()
        self.pack(side="top",fill="both", expand=True)

    def create_widgets_registration_camera(self):
        camera_frame = FunctionalWidgets.create_frame(self)
        loading_frame = FunctionalWidgets.create_frame(self)

        label_one = ctk.CTkLabel(camera_frame, fg_color="blue")
        label_one.pack(fill="both", expand=True)

        label_two = ctk.CTkLabel(loading_frame,text="100%", anchor=ctk.CENTER)
        label_two.pack(fill="both", expand=True)

        camera_frame.pack(side="left", fill="both", expand=True)
        loading_frame.pack(side="left", fill="both", expand=True)