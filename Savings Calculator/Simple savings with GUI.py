import tkinter as tk

def savings_calculator():
    initial_sum = float(initial_sum_entry.get())
    interest_rate = float(initial_rate_entry.get())
    time = float(time_entry.get())
    result = initial_sum * (1+interest_rate/100) ** time
    result_label.config(text=f"You would have: £{result:.2f} in savings after {time} years")


app = tk.Tk()
app.title("Simple Savings Calculator")

tk.Label(app, text="Initial sum (£): ").grid(row=0, column=0)
initial_sum_entry = tk.Entry(app)
initial_sum_entry.grid(row=0, column=1)

tk.Label(app, text="Initial rate (%): ").grid(row=1, column=0)
initial_rate_entry = tk.Entry(app)
initial_rate_entry.grid(row=1, column=1)

tk.Label(app, text="Time (years): ").grid(row=2, column=0)
time_entry = tk.Entry(app)
time_entry.grid(row=2, column=1)

tk.Button(app, text="Calculate", command= savings_calculator).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(app, text="Savings balance: £0.00p")
result_label.grid(row=4, column=0)

app.mainloop()


