import customtkinter as ctk
from frames.registration_treeview import RegistrationTreeview
from frames.registration_camera import RegistrationCamera

class RegistrationMainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # self.pack(fill="both", expand=True)
        # ctk.CTkLabel(self, fg_color="blue").pack(fill="both", expand=True)

        # self.create_frame_camera()
        # self.create_frame_tree_view()
        self.camera_view = RegistrationCamera(self)
        self.tree_view = RegistrationTreeview(self)