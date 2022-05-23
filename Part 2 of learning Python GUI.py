
from ast import Pass
import cmd
from distutils.command.clean import clean
import tkinter as tk
from tkinter import Menu, messagebox

class MyGUI:

    def clear(self):
        self.textbox.delete("1.0", tk.END)




    def show_message(self):
      if self.check_state.get() == 0:
          print(self.textbox.get("1.0", tk.END))
      else:
          messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
        
       
    def shortcut(self, event):
      if event.state == 12 and event.keysym == "Return":
          self.show_message()
          print("Hello YALL!!")

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)

        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close Without Question", command=exit)
        
        

        self.action_menu = tk.Menu(self.menubar, tearoff=0)
        self.action_menu.add_command(label ="Show Message", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.action_menu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="show Message Box", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        
        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 16), command=self.clear )
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

   
MyGUI()