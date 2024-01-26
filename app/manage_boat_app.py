import customtkinter as ctk
from frames.manage_boat_frame import ManageBoatFrame

class ManageBoat(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        self.title(title)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        self.geometry("%dx%d+0+0" % (self.width, self.height))
        self.minsize(self.width, self.height)

        self.manage_boat_frame = ManageBoatFrame(self)
        self.after(0, lambda:self.state("zoomed"))

        self.mainloop()