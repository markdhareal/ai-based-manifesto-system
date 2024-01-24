# FUNCTIONAL-BASED WIDGETS
import customtkinter as ctk

class FunctionalWidgets(ctk.CTk):

    def create_button(window, text, **kwargs):
        button = ctk.CTkButton(window, text=text, **kwargs)
        return button