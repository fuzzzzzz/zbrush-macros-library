
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Send to ZBrush !")
        self.button = tk.Button(self, text="Quit", command=self.quit)
        self.label.pack()
        self.button.pack()


if __name__ == "__main__":
    app = Application()
    app.title("Python App using TKinter :-)")
    app.mainloop()