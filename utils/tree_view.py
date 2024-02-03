from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

class MyTreeView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.my_tree = ttk.Treeview(self)

    def create_tree_view(self, tree_info):
    
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=("Arial Bold", 15))

        self.my_tree['columns'] = tuple(tree_info)

        self.my_tree.column('#0', width=0, stretch=tk.NO)

        for i, info_heading_and_column in enumerate(tree_info):

            column = tree_info[i]

            self.my_tree.column(column, anchor=tk.CENTER, width=120)

            self.my_tree.heading(column, text=info_heading_and_column)

        self.my_tree.pack(fill="both", expand=True)



    #     self.pack(fill="both", expand=True)

    #     self.create_tree_view()

    
    # def create_tree_view(self):
    #     my_tree = ttk.Treeview(self)

    #     style = ttk.Style()
    #     style.theme_use('clam')
    #     style.configure("Treeview", font=("Arial Bold", 15))

    #     my_tree['columns'] = ("Boat Owner", "Boat Name", "Boat Captain")

    #     my_tree.column('#0', width=0, stretch=tk.NO)
    #     my_tree.column('Boat Owner', anchor=tk.CENTER, width=120)
    #     my_tree.column('Boat Name', anchor=tk.CENTER, width=120)
    #     my_tree.column('Boat Captain', anchor=tk.CENTER, width=120)

    #     my_tree.heading('Boat Owner', text='Boat Owner')
    #     my_tree.heading('Boat Name', text='Boat Name')
    #     my_tree.heading('Boat Captain', text='Boat Captain')

    #     my_tree.pack(fill="both", expand=True)