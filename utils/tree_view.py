from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

class MyTreeView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        self.create_tree_view()

    
    def create_tree_view(self):
        my_tree = ttk.Treeview(self)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=("Arial Bold", 15))

        my_tree['columns'] = ("Boat Owner", "Boat Name", "Boat Captain")

        my_tree.column('#0', width=0, stretch=tk.NO)
        my_tree.column('Boat Owner', anchor=tk.CENTER, width=120)
        my_tree.column('Boat Name', anchor=tk.CENTER, width=120)
        my_tree.column('Boat Captain', anchor=tk.CENTER, width=120)

        my_tree.heading('Boat Owner', text='Boat Owner')
        my_tree.heading('Boat Name', text='Boat Name')
        my_tree.heading('Boat Captain', text='Boat Captain')

        my_tree.pack(fill="both", expand=True)