import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")
        
        # Create display
        self.display = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        # Create and place buttons
        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, width=5, height=2,
                             command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2)
        
        # Initialize calculation variables
        self.current_expression = ""
        self.new_number = True

    def button_click(self, value):
        if value == 'C':
            self.clear_display()
        elif value == '=':
            self.calculate_result()
        else:
            if self.new_number:
                self.display.delete(0, tk.END)
                self.new_number = False
            self.display.insert(tk.END, value)
            self.current_expression += value

    def clear_display(self):
        self.display.delete(0, tk.END)
        self.current_expression = ""
        self.new_number = True

    def calculate_result(self):
        try:
            result = str(eval(self.current_expression))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.current_expression = result
            self.new_number = True
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.current_expression = ""
            self.new_number = True

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()