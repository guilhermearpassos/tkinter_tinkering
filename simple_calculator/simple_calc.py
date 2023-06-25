import tkinter as tk
from tkinter import messagebox


class SimpleCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.bind('<Key>', lambda e: print(self.window, e.keysym))
        self.first = tk.Entry()
        self.other = tk.Entry()
        self.button = tk.Button(text="Evaluate", command=self.evaluate)
        self.operation = tk.StringVar(value="+")
        r1 = tk.Radiobutton(text="+", value="+", variable=self.operation)
        r2 = tk.Radiobutton(text="-", value="-", variable=self.operation)
        r3 = tk.Radiobutton(text="*", value="*", variable=self.operation)
        r4 = tk.Radiobutton(text="/", value="/", variable=self.operation)
        r1.grid(column=2, row=1)
        r2.grid(column=2, row=2)
        r3.grid(column=2, row=3)
        r4.grid(column=2, row=4)
        self.first.grid(column=1, row=3)
        self.other.grid(column=3, row=3)
        self.button.grid(row=5, column=2)
        self.result = None
        self.message = tk.Tk()
        self.message.withdraw()

    def evaluate(self):
        self.message = tk.Tk()
        self.message.withdraw()
        operation = self.operation.get()
        first = self.first.get()
        other = self.other.get()
        try:
            first = float(first)
        except ValueError:
            self.result = None
            messagebox.showerror(f"Error! {first} is not a valid number!",  master=self.message)
            return
        try:
            other = float(other)
        except ValueError:
            self.result = None
            messagebox.showerror(f"Error! {other} is not a valid number!",  master=self.message)
            return
        if operation == '+':
            self.result = first + other
        elif operation == '-':
            self.result = first - other
        elif operation == '*':
            self.result = first * other
        elif operation == '/':
            if float(other) == 0:
                self.result = None
                messagebox.showerror(f"Error! can't divide by 0!",  master=self.message)
                return
            self.result = first / other
        messagebox.showinfo('Result', f'result: {self.result}', master=self.message)

    def start(self):

        self.window.mainloop()


def main():
    sc = SimpleCalculator()
    sc.start()


if __name__ == '__main__':
    main()