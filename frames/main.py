from tkinter import Frame, Label, Button, Entry, W, E, CENTER, TOP

class Main(Frame):

    title = "Main"

    def __init__(self, parent, controller, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.winfo_toplevel().title(self.title)
        
        self.pack(side="top", fill="both", expand=True)
        
        self.show()

    def show(self):
        Label(self, text="Welcome to {APP}", font=self.controller.title_font).pack(pady=(250, 0))
        Label(self, text="There are plenty of things to note in this example").pack()