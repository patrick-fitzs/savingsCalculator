import tkinter as tk

def calculate_savings():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    result = principal * (1 + rate / 100) ** time
    result_label.config(text=f"Savings: ${result:.2f}")

app = tk.Tk()
app.title("Savings Calculator")

tk.Label(app, text="Principal ($):").grid(row=0, column=0)
principal_entry = tk.Entry(app)
principal_entry.grid(row=0, column=1)

tk.Label(app, text="Rate (%):").grid(row=1, column=0)
rate_entry = tk.Entry(app)
rate_entry.grid(row=1, column=1)

tk.Label(app, text="Time (years):").grid(row=2, column=0)
time_entry = tk.Entry(app)
time_entry.grid(row=2, column=1)

tk.Button(app, text="Calculate", command=calculate_savings).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(app, text="Savings: $0.00")
result_label.grid(row=4, column=0, columnspan=2)


app.mainloop()
