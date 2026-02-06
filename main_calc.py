import tkinter as tk


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("330x440")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(
            self.root,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="both", ipadx=8, ipady=15)

        self.create_buttons()

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        for button in buttons:
            btn = tk.Button(
                buttons_frame,
                text=button,
                width=5,
                height=2,
                font=("Arial", 16),
                command=lambda b=button: self.on_click(b)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_btn = tk.Button(
            self.root,
            text="C",
            font=("Arial", 16),
            command=self.clear
        )
        clear_btn.pack(fill="both")

    def on_click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
