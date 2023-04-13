import tkinter as tk
def full_name():
    full_name = f"{first_name.get()} {middle_name.get()} {last_name.get()}"

    output.delete(0, tk.END)
    output.insert(0, full_name)
def clear_all():
    output.delete(0, tk.END)
    first_name.delete(0,'end')
    middle_name.delete(0,'end')
    last_name.delete(0,'end')
window = tk.Tk()
window.title("Midterm Exam Problem 2")

tk.Label(window, text="My Full Name", font=("Verdana,16"), fg="red" ).grid(row=0, column=3, padx=5, pady=5)

tk.Label(window, text="Enter Given Name:",fg="red").grid(row=1, column=2, padx=5, pady=5)
first_name = tk.Entry(window)
first_name.grid(row=1, column=4, padx=10, pady=10)

tk.Label(window, text="Enter Middle Name:",fg="red").grid(row=2, column=2, padx=5, pady=5)
middle_name = tk.Entry(window)
middle_name.grid(row=2, column=4, padx=10, pady=10)

tk.Label(window, text="Enter Last Name:",fg="red").grid(row=3, column=2, padx=5, pady=5)
last_name = tk.Entry(window)
last_name.grid(row=3, column=4, padx=10, pady=10)

tk.Label(window, text="My Full Name is:",fg="red").grid(row=4, column=2, padx=5, pady=5)
output = tk.Entry(window,fg="red")
output.grid(row=4, column=4, padx=10, pady=10)

tk.Button(window, text="Show Full Name", command=full_name,width=15).grid(row=5, column=3, padx=10, pady=10)
tk.Button(window, text="Clear All", command=clear_all, width=15).grid(row=6, column=3, padx=10, pady=5)



window.mainloop()