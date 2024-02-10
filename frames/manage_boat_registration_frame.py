import customtkinter as ctk
from utils.manage_boat_label_entry import LabelEntryManageBoat
from database import database_manager
from utils import custom_messagebox

class ManageBoatRegistrationFrame(ctk.CTkFrame):
    def __init__(self, parent, treeview):
        super().__init__(parent)

        # self.pack(fill="both", expand=True)
        self.place(x=0,y=0,relwidth=0.3,relheight=1)
        self.create_widgets()
        self.treeview = treeview
        self.treeview.my_tree.bind('<ButtonRelease>', self.display_data)

        self.entry_one = self.label_entry_manager.entry_widget[0]
        self.entry_two = self.label_entry_manager.entry_widget[1]
        self.entry_three = self.label_entry_manager.entry_widget[2]
        self.entry_four = self.label_entry_manager.entry_widget[3]
        self.entry_five = self.label_entry_manager.entry_widget[4]

    def create_widgets(self):
        self.label_entry_manager = LabelEntryManageBoat(self)

        labels_and_entries = [
            ("Boat Name: ", 0, 0, 0, 1),
            ("Boat Owner: ", 1, 0, 1, 1),
            ("Boat Captain: ", 2, 0, 2, 1),
            ("Boat Capacity: ", 3, 0, 3, 1),
            ("Boat Crew: ", 4, 0, 4, 1)
        ]

        button_info = [
            ("ADD","SEARCH",42,5,0,5,1,self.add_or_insert,lambda:self.search_by_name()),
            ("UPDATE","DELETE",42,6,0,6,1,self.update,self.delete)
            # ("SELECT","RESET",42,7,0,7,1,self.add_or_insert,self.add_or_insert)
        ]
        
        
        self.label_entry_manager.label_entry_manage_boat(labels_and_entries)
        self.label_entry_manager.manage_button(button_info)

        self.label_entry_manager.place(x=0,y=0,relwidth=1,relheight=1)

    def add_or_insert(self):
        entry_values = self.label_entry_manager.get_entry_values()
        if not all(entry_values):
            custom_messagebox.show_error("Error", "Please fill in all entry fields!")
        elif database_manager.name_exists(entry_values[0]):
            custom_messagebox.show_error("Error", "Boat already exists!")
        else:
            database_manager.insert_boat(*entry_values)
            self.treeview.add_to_treeview()
            self.clear()
            custom_messagebox.show_check("Data inserted!")

    def clear(self, *clicked):
        if clicked:
            self.treeview.my_tree.selection_remove(self.treeview.my_tree.selection())
        self.label_entry_manager.clear_entry_values()
    
    def display_data(self,event):
        selected_item = self.treeview.my_tree.focus()
        if selected_item:
            row = self.treeview.my_tree.item(selected_item)['values']
            self.clear()
            self.label_entry_manager.set_entry_values(row)
        else:
            pass
        
    def delete(self):
        selected_item = self.treeview.my_tree.focus()
        if not selected_item:
            custom_messagebox.show_error("Error", "Choose boat to delete.")
        else:
            boat_name = self.treeview.my_tree.item(selected_item)['values'][0]
            database_manager.delete_boat(boat_name)
            self.treeview.add_to_treeview()
            self.clear()
            custom_messagebox.show_check("Data hass been deleted!")

    def update(self):
        selected_item = self.treeview.my_tree.focus()
        if not selected_item:
            custom_messagebox.show_error("Error", "Choose boat to update.")
        else:

            boat_info = self.treeview.my_tree.item(selected_item)['values']
            if boat_info:
                boat_name = boat_info[0]
                new_owner=self.entry_two.get()
                new_captain=self.entry_three.get()
                new_capacity=self.entry_four.get()
                new_crew=self.entry_five.get()
                database_manager.update_boat(
                    new_owner,
                    new_captain,
                    new_capacity,
                    new_crew,
                    boat_name
                )
                self.treeview.add_to_treeview()
                self.clear()
                custom_messagebox.show_check("Data has been updated!")
        
    def search_by_name(self):
        boat_name = self.entry_one.get()
        if boat_name:
            boats = database_manager.search(boat_name)
            if boats:
                boat = boats[0]
                self.label_entry_manager.set_entry_values(boat)

                # Clear the selection in the treeview
                self.treeview.my_tree.selection_remove(self.treeview.my_tree.selection())

                # Iterate through items in the treeview and select the one with the matching boat name
                for item in self.treeview.my_tree.get_children():
                    if self.treeview.my_tree.item(item, 'values')[0] == boat_name:
                        self.treeview.my_tree.selection_add(item)
                        self.treeview.my_tree.focus(item)
                        self.treeview.my_tree.see(item)
                        break
            else:
                custom_messagebox.show_error("Information", "Boat not found.")
        else:
            custom_messagebox.show_error("Information", "Please enter a boat name to search.")


    # def search_by_name(self):
        
    #     boat_name = self.entry_one.get()
    #     if boat_name:
    #         boats = database_manager.search(boat_name)
    #         if boats:
    #             boat = boats[0]
    #             self.label_entry_manager.set_entry_values(boat)
    #         else:
    #             custom_messagebox.show_error("Information", "Boat not found.")
    #     else:
    #         custom_messagebox.show_error("Information", "Please enter a boat name to search.")