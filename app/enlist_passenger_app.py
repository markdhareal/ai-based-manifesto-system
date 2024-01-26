import customtkinter as ctk
from frames.enlist_passenger_frame import EnlistPassengerFrame

class EnlistPassengerApp(ctk.CTk):
    def __init__(self,title):
        super().__init__()

        self.title(title)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()

        self.geometry("%dx%d+0+0" % (self.width, self.height))
        self.minsize(self.width, self.height)

        self.enlist_passenger_frame = EnlistPassengerFrame(self)
        self.after(0, lambda:self.state("zoomed"))

        self.mainloop()