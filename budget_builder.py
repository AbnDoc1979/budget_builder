# 📊 Budget Builder with File Saving
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 🎉 Splash Screen
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: #4CAF50;'>💰 Budget Builder</h1>
    <h3>Plan smarter. Save better. Live well.</h3>
    <p>Welcome to your personal budgeting tool. Adjust your income and expenses, visualize your spending, and download your summary — all in one place.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")



st.title("💰 Budget Builder")
st.write("Create a monthly budget, adjust expenses, and visualize your spending.")

# Income slider
income = st.slider("Monthly Income ($)", min_value=500, max_value=10000, value=3000, step=100)

# Fixed Expenses
st.subheader("Fixed Expenses")
rent = st.slider("Rent/Mortgage", 0, 3000, 1000, 50)
utilities = st.slider("Utilities", 0, 500, 150, 10)
insurance = st.slider("Insurance", 0, 500, 200, 10)
debt = st.slider("Loan/Credit Payments", 0, 1000, 250, 25)

# Flexible Expenses
st.subheader("Flexible Expenses")
groceries = st.slider("Groceries", 0, 800, 300, 10)
transportation = st.slider("Transportation", 0, 500, 150, 10)
entertainment = st.slider("Entertainment", 0, 500, 100, 10)
other = st.slider("Other", 0, 500, 100, 10)

# Savings Goal
savings_goal = st.slider("Savings Goal", 0, 2000, 500, 50)

# Calculations
categories = {
    "Rent/Mortgage": rent,
    "Utilities": utilities,
    "Insurance": insurance,
    "Debt Payments": debt,
    "Groceries": groceries,
    "Transportation": transportation,
    "Entertainment": entertainment,
    "Other": other,
    "Savings": savings_goal
}

total_expenses = sum(categories.values())
remaining = income - total_expenses
savings_percent = (savings_goal / income) * 100 if income > 0 else 0

# Budget Summary
st.subheader("📈 Budget Summary")
st.write(f"**Total Income:** ${income}")
st.write(f"**Total Expenses:** ${total_expenses}")
st.write(f"**Remaining Balance:** ${remaining}")
st.write(f"**Savings Rate:** {savings_percent:.1f}%")

if remaining < 0:
    st.warning("⚠️ You're over budget! Consider adjusting your expenses.")
elif remaining < 100:
    st.info("💡 You're close to your limit. A small buffer helps with surprise costs.")
else:
    st.success("✅ Great job! You’re living within your means and saving for the future.")

# Pie Chart
st.subheader("📊 Expense Breakdown")
fig, ax = plt.subplots()
ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# File Saving
st.subheader("📥 Download Your Budget Summary")
summary = f"""Budget Summary
-----------------------
Total Income: ${income}
Total Expenses: ${total_expenses}
Remaining Balance: ${remaining}
Savings Rate: {savings_percent:.1f}%
"""

# 📥 Download Budget as CSV
st.subheader("📥 Download Your Budget as CSV")

# Create DataFrame
df = pd.DataFrame({
    "Category": list(categories.keys()),
    "Amount": list(categories.values())
})

# Add summary row
summary_row = pd.DataFrame({
    "Category": ["Total Income", "Total Expenses", "Remaining Balance", "Savings Rate (%)"],
    "Amount": [income, total_expenses, remaining, round(savings_percent, 1)]
})

df = pd.concat([df, summary_row], ignore_index=True)

# Convert to CSV
csv = df.to_csv(index=False).encode("utf-8")

# Download button
st.download_button(
    label="Download Budget as CSV",
    data=csv,
    file_name="budget_summary.csv",
    mime="text/csv"
)

# Download button
st.download_button(
    label="Download Summary as .txt",
    data=summary.encode("utf-8"),
    file_name="budget_summary.txt",
    mime="text/plain"
)


