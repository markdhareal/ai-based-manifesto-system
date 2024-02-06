from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

class MyTreeView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.tree_scroll = ctk.CTkScrollbar(self)
        self.tree_scroll.pack(side="right", fill="y")

        self.my_tree = ttk.Treeview(self, yscrollcommand=self.tree_scroll.set)
        
        self.tree_scroll.configure(command=self.my_tree.yview)

        self.set_up_style()
        self.create_tree_view([])

    def set_up_style(self):
        style = ttk.Style(self)
        style.theme_use('alt')
        style.configure('Treeview', font=("Arial Bold", 15),background="gray14", foreground="#fff", fieldbackground="gray14", rowheight=50)
        style.configure('Treeview.Heading', font=("Arial Bold", 15))
        style.map('Treeview', background=[('selected', '#3B8ED0')])

    def create_tree_view(self, tree_info):

        self.my_tree['columns'] = tuple(tree_info)

        self.my_tree.column('#0', width=0, stretch=tk.NO)

        for i, info_heading_and_column in enumerate(tree_info):

            column = tree_info[i]

            self.my_tree.column(column, anchor=tk.CENTER, width=120)

            self.my_tree.heading(column, text=info_heading_and_column)

        self.my_tree.pack(fill="both", expand=True)

    def add_item(self, values):
        self.my_tree.insert("", "end", values=values)