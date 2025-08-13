# Expense Tracker

A Python script that reads a CSV of expenses, summarizes totals by category and month, and generates visualizations.

## Features
- Summarizes expenses by category and month
- Saves top categories chart as `top_categories.png`
- Exports summary CSV files: `category_total.csv` and `monthly_total.csv`

## Requirements
- Python 3.11+
- pandas
- matplotlib

## Usage
1. Place your CSV `expenses.csv` in the project folder (columns: Date, Amount, Category, Description)
2. Run the script:
   ```bash
   python expense_tracker.py
