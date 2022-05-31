import tkinter as tk


root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=("Arial", 25)).pack()

play_area = tk.Frame(root, width=300, height=300, bg="white")
XO_points = []
class XOPoint:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)


    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg="snow", fg="black")
            self.value = current_chr
            if current_chr == "X":
                current_chr = "O"
            elif current_chr == "O":
                current_chr = "X"



    def reset(self):
        self.button.configure(text="", bg="white")
        self.value = None
for x in range(1, 4): 
    for y in range(1,4):
        XOPoint(x, y)

play_area.pack(pady=10, padx=10)

root.mainloop()



