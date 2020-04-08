import tkinter as tk
from tkinter.ttk import Progressbar, Style
from tkinter import font as tkfont, Menu
from classes.utils import *

from frames.main import Main
from frames.setup import Setup

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.winfo_toplevel().title("Welcome")

        self.geometry("900x600")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        bottom = tk.Frame(self, bd=1, relief=tk.SUNKEN, height=20)
        bottom.pack(side="bottom", fill="x")

        self.status_lbl = tk.Label(bottom, text="Ready")
        self.status_lbl.pack(side=tk.LEFT)
        
        self.progressbar = Progressbar(bottom, orient = tk.HORIZONTAL, length = 100, mode = 'determinate')
        self.progressbar.pack(side=tk.RIGHT)
        self.progressbar["value"] = 0
        self.progressbar.update()

        self.container = container

        self._frame = None
        
        self.start()

    def setStatus(self, text, percent = 0):
        self.status_lbl['text'] = text
        self.progressbar["value"] = percent
        self.progressbar.update()

    def start(self):
        menubar = Menu(self)
        menubar.add_command(label="Main", command=lambda: self.show_frame(Main))
        menubar.add_command(label="Testing", command=lambda: self.show_frame(Setup))
        menubar.add_command(label="Training")
        menubar.add_command(label="Quit", command=self.quit)
        self.config(menu=menubar)

        self.show_frame(Main)

    def show_frame(self, frame_class):
        new_frame = frame_class(self.container, self)

        if self._frame is not None:
            self._frame.destroy()
            
        self._frame = new_frame
        self._frame.tkraise()
        return new_frame

if __name__ == "__main__":
    root = App()
    center(root)
    root.mainloop()