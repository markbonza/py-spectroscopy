import time
import threading
from tkinter import Frame, Label, Button, Entry, IntVar, StringVar, END, N, S, W, E, OptionMenu, messagebox, LEFT, BOTH, RIGHT

from lib.plot import Plot, Demo
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib
matplotlib.use('TkAgg')

class Test(Frame):
    title = "Execute Test"

    parameters = {}

    def __init__(self, parent, controller, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.winfo_toplevel().title(self.title)

        self.pack(side="top", fill="both", expand=True)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

    def setParams(self, params):
        self.parameters = params

    def show(self):
        self.plotframe = Frame(self) #, borderwidth=2, relief="solid")
        self.plotframe.grid(row=0, column=0, sticky=(N, S, E, W))
        info = Frame(self) #, borderwidth=2, relief="solid")
        info.grid(row=0, column=1, sticky=(N, S, E, W))

        Label(info, text="TEST CONFIG", font=self.controller.title_font).pack(anchor=N)
        for k, v in self.parameters.items():
            f = Frame(info)
            f.pack(anchor=E, fill=BOTH)
            Label(f, text="{} : {}".format(k.upper(), v.upper())).pack(anchor=E)

        #t1 = threading.Thread(target=self.start)  
        #t1.start()
        self.start()

    def start(self):
        port = self.parameters.get('port')
        self.test_count = int(self.parameters.get('test_count'))
        test_interval = int(self.parameters.get('interval')) * 1000
        log_filename = self.parameters.get('log_filename')

        fig = Figure()
        self.ax1 = fig.add_subplot(1,1,1)

        scatter3 = FigureCanvasTkAgg(fig, self.plotframe)
        scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

        self.ani=animation.FuncAnimation(fig, self.animate, interval=test_interval)
        #plt.show()

    def animate(self, i):
        
        counter = i + 1;
        if counter > self.test_count:
            self.ani.event_source.stop()
            self.controller.setStatus("Ready")
            return False

        percent = int((counter / self.test_count) * 100)

        self.controller.setStatus("Working : {} / {}".format(counter, self.test_count), percent)

        p = Demo()
        res = p.test()

        self.ax1.scatter(res.x, res.y, color=res.colors,s=1)
        self.ax1.set_xticks(res.wl)