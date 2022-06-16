import tkinter as tk
import threading
import time
import random

class Typing_Speed_Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Roshan And Yug - Typing Speed Analyzer")
        self.root.iconbitmap("logo.ico")
        self.root.config(bg="#04275c")
        self.root.geometry('595x345')
        self.root.resizable(False, False)


        self.line = open("w_file.txt", "r").read().split("\n") 

        self.frame = tk.Frame(self.root)
        
        self.title = tk.Label(self.root, text="Welcome to RAY Typing Speed Game", font=("Arial Rounded MT Black", 20, "bold underline"), fg="white", bg="#04275f")
        self.title.place(x=45, y=30)

        self.label_1 = tk.Label(self.root, text="Type this:- ", font=("Arial Rounded MT Black", 16), fg="white", bg="#04275f")
        self.label_1.place(x=15, y=100)

        self.sample_label = tk.Label(self.root, text=random.choice(self.line), font=("Arial Rounded MT Black", 16, "bold"), wraplength=525, fg="white", bg="#04275f", justify=tk.LEFT)
        self.sample_label.place(x=45, y=140)

        self.label_2 = tk.Label(self.root, text="Here:- ", font=("Arial Rounded MT Black", 16), fg="white", bg="#04275f")
        self.label_2.place(x=15, y=225)

        self.input_entry = tk.Entry(self.root, font=("Times new roman serif", 16, "bold"), fg="red", justify=tk.LEFT, width=40, relief=tk.FLAT)
        self.input_entry.place(x=80, y=225)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.root, text="Speed: 0.00 CPS\t0.00 WPM", font=("Arial Rounded MT Black", 16), fg="white", bg="#04275f")
        self.speed_label.place(x=15, y=275)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, font=("HELVETICA", 14, "bold"), height=1, width=8)
        self.reset_button.place(x=450, y=275)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()
    
    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18, 20]:
                self.running = True
                t=threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text'):
            self.input_entry.config(fg="green")
            self.running = False

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get())/self.counter
            wpm = (len(self.input_entry.get().split(" "))/self.counter)*60
            self.speed_label.config(text=f"Speed: {cps:.2f} CPS\t{wpm:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: 0.00 CPS\t0.00 WPM")
        self.sample_label.config(text=random.choice(self.line))
        self.input_entry.delete(0, tk.END)

Typing_Speed_Gui()