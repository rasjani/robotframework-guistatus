#!/usr/bin/env python
import os
try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import Tkinter.ttk as ttk
from PIL import Image, ImageTk


class GuiStatusUI(tk.Frame):
    def __init__(self, master=None, width=900, height=300):
        super().__init__(master, width=width, height=height)
        self.master.title("GuiStatusApplication")
        self.pack(fill=tk.BOTH, expand=1)
        #self.pack()
        self.init_ui()
        self.bring_to_front()

    def bring_to_front(self):
        self.master.lift()
        self.master.attributes('-topmost', True)
        self.master.after_idle(self.master.attributes, '-topmost', False)

    def clear_text(self):
        for t in [self.suite_text, self.task_text, self.keyword_text, self.log_text, self.status_text]:
            t.set("")

    def init_ui(self):
        logo_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logo.jpg")
        image_data = Image.open(logo_file)
        render = ImageTk.PhotoImage(image_data)
        image_label = tk.Label(self, image=render)
        image_label.image = render
        image_label.grid(row=0, column=0, rowspan=6,)

        for idx, txt_label in enumerate(["Suite", "Task", "Keyword", "Log", "Status"]):
            text_label = tk.Label(self, text=txt_label, justify=tk.RIGHT, anchor=tk.E)
            text_label.grid(row=idx, column=1)

        self.suite_text = tk.StringVar()
        self.task_text = tk.StringVar()
        self.keyword_text = tk.StringVar()
        self.log_text = tk.StringVar()
        self.status_text = tk.StringVar()

        pblen = 200
        for idx, t in enumerate([self.suite_text, self.task_text, self.keyword_text, self.log_text, self.status_text]):
            text_label = tk.Label(self, textvariable=t, justify=tk.LEFT, anchor=tk.W, relief=tk.RIDGE, width=50)
            text_label.grid(row=idx, column=2, columnspan=2)
            pblen = text_label.winfo_width()

        self.pb = ttk.Progressbar(self, orient='horizontal', mode='determinate', maximum=100)
        self.pb.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        self.pb.grid(row=5, column=2, columnspan=2, sticky='EW')

        self.clear_text()
