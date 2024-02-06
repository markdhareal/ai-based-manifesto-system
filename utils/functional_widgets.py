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
        entry = ctk.CTkEntry(window, border_width=1, **kwargs)
        return entry

    def create_text_box(window,**kwargs):
        text_box = ctk.CTkTextbox(window, width=300, height=200, border_width=1, **kwargs)
        return text_box

    def create_combo_box(window, value, **kwargs):
        combo_box = ctk.CTkComboBox(window, values=value, **kwargs)
        return combo_box
    
    def create_frame(window, **kwargs):
        frame = ctk.CTkFrame(window, **kwargs)
        return frame