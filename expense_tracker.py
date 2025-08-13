# expense_tracker.py

import pandas as pd
import matplotlib.pyplot as chart

# Load expenses CSV
xp = pd.read_csv('expenses.csv')  # Columns: Date, Amount, Category, Description

# Total per category
cat_total = xp.groupby('Category')['Amount'].sum()
print("Expenses by Category:")
print(cat_total)

# Total per month
xp['Date'] = pd.to_datetime(xp['Date'])
xp['Month'] = xp['Date'].dt.to_period('M')
month_total = xp.groupby('Month')['Amount'].sum()
print("\nExpenses by Month:")
print(month_total)

# Bar chart for top 5 categories
top_categories = cat_total.sort_values(ascending=False).head(5)
top_categories.plot(kind='bar', title='Top 5 Expense Categories')
chart.xlabel('Category')
chart.ylabel('Total Amount')
chart.tight_layout()
chart.savefig('top_categories.png')
chart.show()

# Save totals to CSV
cat_total.to_csv('category_total.csv')
month_total.to_csv('monthly_total.csv')
