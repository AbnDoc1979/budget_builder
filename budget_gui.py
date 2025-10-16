import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def calculate_budget():
    try:
        income = float(entry_income.get())
        expenses = {
            "Rent": float(entry_rent.get()),
            "Utilities": float(entry_utilities.get()),
            "Insurance": float(entry_insurance.get()),
            "Debt": float(entry_debt.get()),
            "Groceries": float(entry_groceries.get()),
            "Transport": float(entry_transport.get()),
            "Entertainment": float(entry_entertainment.get()),
            "Other": float(entry_other.get()),
            "Savings": float(entry_savings.get())
        }

        total_expenses = sum(expenses.values())
        remaining = income - total_expenses
        savings_percent = (expenses["Savings"] / income) * 100 if income > 0 else 0

        result_text.set(f"Total Expenses: ${total_expenses:.2f}\n"
                        f"Remaining Balance: ${remaining:.2f}\n"
                        f"Savings Rate: {savings_percent:.1f}%")

        if remaining < 0:
            messagebox.showwarning("Over Budget", "⚠️ You're over budget!")
        elif remaining < 100:
            messagebox.showinfo("Tight Budget", "💡 You're close to your limit.")
        else:
            messagebox.showinfo("Good Job", "✅ You're living within your means!")

        # Pie chart
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().grid(row=12, column=0, columnspan=2)
        canvas.draw()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI setup
window = tk.Tk()
window.title("💰 Budget Builder")
window.geometry("500x700")

# Input fields
fields = [
    ("Monthly Income", "income"),
    ("Rent/Mortgage", "rent"),
    ("Utilities", "utilities"),
    ("Insurance", "insurance"),
    ("Debt Payments", "debt"),
    ("Groceries", "groceries"),
    ("Transportation", "transport"),
    ("Entertainment", "entertainment"),
    ("Other", "other"),
    ("Savings Goal", "savings")
]

entries = {}
for i, (label_text, key) in enumerate(fields):
    tk.Label(window, text=label_text).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10)
    entries[key] = entry

entry_income = entries["income"]
entry_rent = entries["rent"]
entry_utilities = entries["utilities"]
entry_insurance = entries["insurance"]
entry_debt = entries["debt"]
entry_groceries = entries["groceries"]
entry_transport = entries["transport"]
entry_entertainment = entries["entertainment"]
entry_other = entries["other"]
entry_savings = entries["savings"]

# Calculate button
tk.Button(window, text="Calculate Budget", command=calculate_budget, bg="#4CAF50", fg="white").grid(row=10, column=0, columnspan=2, pady=10)

# Result display
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text, justify="left", font=("Arial", 10)).grid(row=11, column=0, columnspan=2, pady=10)

window.mainloop()

