import os

try:
    import tkinter as Tk  # noqa: N812
    import tkinter.ttk as Ttk  # noqa: N812
except ImportError:
    import Tkinter as Tk
    import Tkinter.ttk as Ttk
from PIL import Image, ImageTk


class GuiStatusUI(Tk.Frame):
    def __init__(self, master=None, width=900, height=300):
        super().__init__(master, width=width, height=height)
        self.pb = None
        self.master.title("GuiStatusApplication")
        self.pack(fill=Tk.BOTH, expand=1)
        self.init_ui()
        self.bring_to_front()

    def bring_to_front(self):
        self.master.lift()
        self.master.attributes('-topmost', True)
        self.master.after_idle(self.master.attributes, '-topmost', False)

    def clear_text(self):
        if self.pb is not None:
            self.pb.grid_forget()
        for t in [self.suite_text, self.status_text]:
            t.set("")

    def init_ui(self):
        logo_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logo.jpg")
        image_data = Image.open(logo_file)
        render = ImageTk.PhotoImage(image_data)
        image_label = Tk.Label(self, image=render)
        image_label.image = render
        image_label.grid(row=0, column=0, rowspan=6)

        for idx, txt_label in enumerate(["Suite", "Status", "Overall", "Steps"]):
            text_label = Tk.Label(self, text=txt_label, justify=Tk.RIGHT, anchor=Tk.E)
            text_label.grid(row=idx, column=1)

        self.suite_text = Tk.StringVar()
        self.status_text = Tk.StringVar()

        pblen = 200
        for idx, t in enumerate([self.suite_text, self.status_text]):
            text_label = Tk.Label(self, textvariable=t, justify=Tk.LEFT, anchor=Tk.W, relief=Tk.RIDGE, width=50)
            text_label.grid(row=idx, column=2, columnspan=2)
            pblen = text_label.winfo_width()

        self.sb = Ttk.Progressbar(self, orient='horizontal', mode='indeterminate', maximum=100)
        self.sb.pack(expand=True, fill=Tk.BOTH, side=Tk.TOP)
        self.sb.grid(row=2, column=2, columnspan=2, sticky='EW')
        self.clear_text()

    def add_progressbar(self, steps):
        if self.pb is not None:
            self.pb.grid_forget()

        self.pb = Ttk.Progressbar(self, orient='horizontal', mode='determinate', maximum=steps)
        self.pb.pack(expand=True, fill=Tk.BOTH, side=Tk.TOP)
        self.pb.grid(row=3, column=2, columnspan=2, sticky='EW')
