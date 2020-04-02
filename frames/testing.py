from tkinter import Frame, Label, Button, Entry, IntVar, StringVar, END, N, S, W, E, OptionMenu, messagebox
from classes.inputs import IntEntry

from .execute import Test

class Testing(Frame):

    title = "Testing"

    def __init__(self, parent, controller, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.winfo_toplevel().title(self.title)

        self.pack(anchor="center", expand=True)
        self.show()

    def inputs(self):
        #TODO GET COM LATER
        coms = ['COM1', 'COM2', 'COM3']

        return {
            'port' : {
                'label' : Label(self, text="Select Port : "),
                'input' : Entry(self, textvariable=StringVar(self, value='COM3'), justify="center"),
            },
            'interval' : {
                'label' : Label(self, text="Test Interval(sec) :"),
                'input' : IntEntry(self, textvariable=IntVar(self, value='1'),justify="right"),
            },
            'test_count' : {
                'label' : Label(self, text="Test Count :"),
                'input' : IntEntry(self, textvariable=IntVar(self, value='5'), justify="right"),
            },
            'log_filename' : {
                'label' : Label(self, text="Log Filename :"),
                'input' : Entry(self, textvariable=StringVar(self, value='logfile.txt'), justify="center"),
            }
        }
    def show(self):

        i = 0
        self.inputs = self.inputs()

        for k, v in self.inputs.items():
            v['label'].grid(row=i, column=0, sticky=E, pady=(0, 10))
            v['input'].grid(row=i, column=1, sticky=(N, S, E, W), pady=(0, 10))
            i =  i + 1

        Button(self, text="Start", command=lambda: self.start()).grid(row=i+1, columnspan=2, sticky=(N, S, E, W))

    def start(self):
        parameters = {}
        errors = []
        for k, v in self.inputs.items():
            if not v['input'].get():
                errors.append(k) 
            
            parameters[k] = v['input'].get()

        if len(errors) > 0:
            messagebox.showerror("Alert", "Please specify empty field!")
            return False

        
        v = self.controller.show_frame(Test)
        v.setParams(parameters)
        v.show()