import tkinter as tk
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry = tk.Entry(self.root, width=33, borderwidth=18,background="#FFE5B4")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create number buttons
        self.button_7 = tk.Button(self.root,background="#E78A61" , text="7", padx=22,pady=18, command=lambda: self.click_button("7"))
        self.button_7.grid(row=1, column=0,)

        self.button_8 = tk.Button(self.root,background="#E78A61", text="8", padx=22,pady=18, command=lambda : self.click_button("8"))
        self.button_8.grid(row=1, column=1,)

        self.button_9 = tk.Button(self.root,background="#E78A61" ,text="9", padx=22,pady=18, command=lambda: self.click_button("9"))
        self.button_9.grid(row=1, column=2)

        self.button_divide = tk.Button(self.root,background="#E78A61", text="/",padx=22,pady=18, command=lambda: self.click_button("/"))
        self.button_divide.grid(row=1, column=3)

        self.button_4 = tk.Button(self.root,background="#E78A61", text="4", padx=22,pady=18, command=lambda: self.click_button("4"))
        self.button_4.grid(row=2, column=0)

        self.button_5 = tk.Button(self.root,background="#E78A61", text="5", padx=22,pady=18, command=lambda: self.click_button("5"))
        self.button_5.grid(row=2, column=1)

        self.button_6 = tk.Button(self.root,background="#E78A61", text="6", padx=22,pady=18, command=lambda: self.click_button("6"))
        self.button_6.grid(row=2, column=2)

        self.button_multiply = tk.Button(self.root,background="#E78A61", text="*", padx=22,pady=18, command=lambda: self.click_button("*"))
        self.button_multiply.grid(row=2, column=3)

        self.button_1 = tk.Button(self.root, background="#E78A61",text="1", padx=22,pady=18, command=lambda: self.click_button("1"))
        self.button_1.grid(row=3, column=0)

        self.button_2 = tk.Button(self.root, background="#E78A61",text="2", padx=22,pady=18, command=lambda: self.click_button("2"))
        self.button_2.grid(row=3, column=1)

        self.button_3 = tk.Button(self.root, background="#E78A61",text="3", padx=22,pady=18, command=lambda: self.click_button("3"))
        self.button_3.grid(row=3, column=2)

        self.button_subtract = tk.Button(self.root, background="#E78A61",text="-", padx=22,pady=18, command=lambda: self.click_button("-"))
        self.button_subtract.grid(row=3, column=3)

        self.button_0 = tk.Button(self.root,background="#E78A61", text="0", padx=22,pady=18, command=lambda: self.click_button("0"))
        self.button_0.grid(row=4, column=0)

        self.button_dot = tk.Button(self.root,background="#E78A61", text=".",padx=22 ,pady=18, command=lambda: self.click_button("."))
        self.button_dot.grid(row=4, column=1)

        self.button_equal = tk.Button(self.root,background="#E78A61", text="=",padx=22 ,pady=18, command=self.calculate)
        self.button_equal.grid(row=4, column=2)

        self.button_add = tk.Button(self.root,background="#E78A61", text="+", padx=22,pady=18, command=lambda: self.click_button("+"))
        self.button_add.grid(row=4, column=3)

        self.button_clear = tk.Button(self.root,background="#E78A61", text="Clear", padx=104,pady=30, command=self.clear)
        self.button_clear.grid(row=5, column=0, columnspan=4)

    def click_button(self, button):
        self.entry.insert(tk.END, button)
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x400")
    calculator = Calculator(root)
    root.mainloop()