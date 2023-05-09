import tkinter as tk

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Temperature Converter")
        self.master.geometry("300x250")
        self.master.configure(bg='Gray')
        self.celsius_entry = self.create_label_and_entry("Celsius:", 0)
        self.fahrenheit_entry = self.create_label_and_entry("Fahrenheit:", 1)
        self.kelvin_entry = self.create_label_and_entry("Kelvin:", 2)
        self.create_convert_button("Convert to Celsius", self.convert_to_celsius, 3, 0)
        self.create_convert_button("Convert to Fahrenheit", self.convert_to_fahrenheit, 3, 1)
        self.create_convert_button("Convert to Kelvin", self.convert_to_kelvin, 4, 0, 2, padx=(5, 0), pady=5)
        self.create_clear_button("Clear", self.clear_entries, 5, 0, 2, 'n')
        self.master.bind('<Return>', lambda event: self.convert_to_fahrenheit())

    def create_label_and_entry(self, label_text, row):
        label = tk.Label(self.master, text=label_text, bg='#FFFFFF')
        label.grid(row=row, column=0, padx=5, pady=5)
        entry = tk.Entry(self.master)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def create_convert_button(self, button_text, button_command, row, column, columnspan=1, padx=5, pady=5):
        button = tk.Button(self.master, text=button_text, command=button_command, bg='#6ab04c', fg='#FFFFFF', relief='flat', bd=3)
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky='we')

    def create_clear_button(self, button_text, button_command, row, column, columnspan=1, anchor=None):
        button = tk.Button(self.master, text=button_text, command=button_command, bg='#E74C3C', fg='#FFFFFF', relief='flat', bd=4)
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5, sticky='we')

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            self.celsius_entry.delete(0, tk.END)
            self.celsius_entry.insert(0, celsius)
        except ValueError:
            self.celsius_entry.delete(0, tk.END)
            self.celsius_entry.insert(0, "Invalid input")

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = celsius * 9/5 + 32
            self.fahrenheit_entry.delete(0, tk.END)
            self.fahrenheit_entry.insert(0, fahrenheit)
        except ValueError:
            self.fahrenheit_entry.delete(0, tk.END)
            self.fahrenheit_entry.insert(0, "Invalid input")

    def convert_to_kelvin(self):
        try:
            celsius = float(self.celsius_entry.get())
            kelvin = celsius + 273.15
            self.kelvin_entry.delete(0, tk.END)
            self.kelvin_entry.insert(0, kelvin)
        except ValueError:
            self.kelvin_entry.delete(0, tk.END)
            self.kelvin_entry.insert(0, "Invalid input")

    def clear_entries(self):
            self.celsius_entry.delete(0, tk.END)
            self.fahrenheit_entry.delete(0, tk.END)
            self.kelvin_entry.delete(0, tk.END)

if __name__ == "__main__":
        root = tk.Tk()
        app = TemperatureConverter(root)
        root.mainloop()
