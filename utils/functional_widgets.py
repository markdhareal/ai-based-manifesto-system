# FUNCTIONAL-BASED WIDGETS
import customtkinter as ctk

class FunctionalWidgets(ctk.CTk):

    def create_button(window, text, **kwargs):
        button = ctk.CTkButton(window, text=text, **kwargs)
        return button
    
    def create_label(window, text, **kwargs):
        label = ctk.CTkLabel(window,text=text,**kwargs)
        return label
    
    def create_entry(window, **kwargs):
        entry = ctk.CTkEntry(window, **kwargs)
        return entry