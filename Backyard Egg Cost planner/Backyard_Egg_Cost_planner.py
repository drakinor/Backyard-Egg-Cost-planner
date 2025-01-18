import tkinter as tk
from tkinter import messagebox

def calculate_costs():
    try:
        # --- Fixed Costs ---
        housing_cost = float(entry_housing.get())
        fencing_cost = float(entry_fencing.get())
        equipment_cost = float(entry_equipment.get())
        total_fixed_costs = housing_cost + fencing_cost + equipment_cost
        
        # --- Recurring Monthly Costs ---
        feed_cost = float(entry_feed.get())
        bedding_cost = float(entry_bedding.get())
        water_cost = float(entry_water.get())
        medication_cost = float(entry_medication.get())
        other_cost = float(entry_other.get())
        total_monthly_recurring_cost = feed_cost + bedding_cost + water_cost + medication_cost + other_cost
        
        # --- Production (Daily) ---
        num_chickens = int(entry_num_chickens.get())
        eggs_per_chicken_per_day = float(entry_eggs_per_chicken_per_day.get())
        
        # Calculate monthly egg production (approx 30-day month)
        eggs_per_month = eggs_per_chicken_per_day * num_chickens * 30
        
        if eggs_per_month <= 0:
            raise ValueError("Eggs per month is zero or less. Check your chicken/egg inputs.")
        
        # --- Store and Selling Prices (Per Dozen) ---
        store_egg_price_per_dozen = float(entry_store_egg_price.get())
        selling_price_per_dozen = float(entry_selling_price.get())
        
        # Convert these to "per egg"
        store_egg_price_per_egg = store_egg_price_per_dozen / 12
        selling_price_per_egg = selling_price_per_dozen / 12
        
        # --- Cost Per Egg ---
        cost_per_egg = total_monthly_recurring_cost / eggs_per_month
        cost_per_dozen = cost_per_egg * 12
        
        # --- Savings if you're just eating the eggs ---
        savings_per_egg = store_egg_price_per_egg - cost_per_egg
        monthly_savings = savings_per_egg * eggs_per_month
        
        if monthly_savings > 0:
            break_even_eating_months = total_fixed_costs / monthly_savings
        else:
            break_even_eating_months = float('inf')
        
        # --- Profit if you're selling the eggs ---
        profit_per_egg = selling_price_per_egg - cost_per_egg
        monthly_profit = profit_per_egg * eggs_per_month
        
        if monthly_profit > 0:
            break_even_selling_months = total_fixed_costs / monthly_profit
        else:
            break_even_selling_months = float('inf')
        
        # --- Update Result Labels ---
        label_cost_per_egg_val.config(text=f"${cost_per_egg:.2f}")
        label_cost_per_dozen_val.config(text=f"${cost_per_dozen:.2f}")
        
        if break_even_eating_months == float('inf'):
            label_break_even_eating_val.config(text="N/A")
        else:
            label_break_even_eating_val.config(text=f"{break_even_eating_months:.1f} mo")
        
        if break_even_selling_months == float('inf'):
            label_break_even_selling_val.config(text="N/A")
        else:
            label_break_even_selling_val.config(text=f"{break_even_selling_months:.1f} mo")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input data: {e}")

def clear_fields():
    # Clear all fields
    entry_housing.delete(0, tk.END)
    entry_fencing.delete(0, tk.END)
    entry_equipment.delete(0, tk.END)
    entry_feed.delete(0, tk.END)
    entry_bedding.delete(0, tk.END)
    entry_water.delete(0, tk.END)
    entry_medication.delete(0, tk.END)
    entry_other.delete(0, tk.END)
    
    entry_num_chickens.delete(0, tk.END)
    entry_eggs_per_chicken_per_day.delete(0, tk.END)
    
    entry_store_egg_price.delete(0, tk.END)
    entry_selling_price.delete(0, tk.END)
    
    label_cost_per_egg_val.config(text="$0.00")
    label_cost_per_dozen_val.config(text="$0.00")
    label_break_even_eating_val.config(text="0 mo")
    label_break_even_selling_val.config(text="0 mo")

root = tk.Tk()
root.title("Backyard Egg Cost Calculator")

# Fixed Costs
tk.Label(root, text="Housing Cost:").grid(row=0, column=0, sticky="e")
entry_housing = tk.Entry(root)
entry_housing.grid(row=0, column=1)

tk.Label(root, text="Fencing Cost:").grid(row=1, column=0, sticky="e")
entry_fencing = tk.Entry(root)
entry_fencing.grid(row=1, column=1)

tk.Label(root, text="Equipment Cost:").grid(row=2, column=0, sticky="e")
entry_equipment = tk.Entry(root)
entry_equipment.grid(row=2, column=1)

# Recurring Costs
tk.Label(root, text="Feed Cost/Month:").grid(row=3, column=0, sticky="e")
entry_feed = tk.Entry(root)
entry_feed.grid(row=3, column=1)

tk.Label(root, text="Bedding Cost/Month:").grid(row=4, column=0, sticky="e")
entry_bedding = tk.Entry(root)
entry_bedding.grid(row=4, column=1)

tk.Label(root, text="Water Cost/Month:").grid(row=5, column=0, sticky="e")
entry_water = tk.Entry(root)
entry_water.grid(row=5, column=1)

tk.Label(root, text="Medication Cost/Month:").grid(row=6, column=0, sticky="e")
entry_medication = tk.Entry(root)
entry_medication.grid(row=6, column=1)

tk.Label(root, text="Other Cost/Month:").grid(row=7, column=0, sticky="e")
entry_other = tk.Entry(root)
entry_other.grid(row=7, column=1)

# Production
tk.Label(root, text="Number of Chickens:").grid(row=8, column=0, sticky="e")
entry_num_chickens = tk.Entry(root)
entry_num_chickens.grid(row=8, column=1)

tk.Label(root, text="Eggs/Chicken/Day:").grid(row=9, column=0, sticky="e")
entry_eggs_per_chicken_per_day = tk.Entry(root)
entry_eggs_per_chicken_per_day.grid(row=9, column=1)

# Market Data (Per Dozen)
tk.Label(root, text="Store Egg Price (per dozen):").grid(row=10, column=0, sticky="e")
entry_store_egg_price = tk.Entry(root)
entry_store_egg_price.grid(row=10, column=1)

tk.Label(root, text="Selling Price (per dozen):").grid(row=11, column=0, sticky="e")
entry_selling_price = tk.Entry(root)
entry_selling_price.grid(row=11, column=1)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_costs)
btn_calculate.grid(row=12, column=0, columnspan=2, pady=10)

# Results
tk.Label(root, text="Cost per Egg:").grid(row=13, column=0, sticky="e")
label_cost_per_egg_val = tk.Label(root, text="$0.00")
label_cost_per_egg_val.grid(row=13, column=1, sticky="w")

tk.Label(root, text="Cost per Dozen:").grid(row=14, column=0, sticky="e")
label_cost_per_dozen_val = tk.Label(root, text="$0.00")
label_cost_per_dozen_val.grid(row=14, column=1, sticky="w")

tk.Label(root, text="Break-Even (Eating):").grid(row=15, column=0, sticky="e")
label_break_even_eating_val = tk.Label(root, text="0 mo")
label_break_even_eating_val.grid(row=15, column=1, sticky="w")

tk.Label(root, text="Break-Even (Selling):").grid(row=16, column=0, sticky="e")
label_break_even_selling_val = tk.Label(root, text="0 mo")
label_break_even_selling_val.grid(row=16, column=1, sticky="w")

# Clear Button
btn_clear = tk.Button(root, text="Clear", command=clear_fields)
btn_clear.grid(row=17, column=0, columnspan=2, pady=10)

root.mainloop()
