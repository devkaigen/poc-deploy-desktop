import tkinter as tk
from tkinter import ttk
from calc import Calc


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Initialize the calculator
        self.calc = Calc()

        # Create the input field
        self.input_field = ttk.Entry(master, width=40, font=('Arial', 16))
        self.input_field.grid(row=0, column=0, columnspan=4, pady=10)

        # Create the buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('C', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)

    def create_button(self, text, row, column):
        button = ttk.Button(self.master, text=text, width=10,
                            command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.input_field.delete(0, tk.END)
        elif text == '=':
            result = self.calc.calculate(self.input_field.get())
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, result)
        else:
            self.input_field.insert(tk.END, text)


if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
