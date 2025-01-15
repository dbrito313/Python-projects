


import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from datetime import datetime, timedelta


orders_df = pd.DataFrame(columns=["order_id", "product_code", "quantity", "material_needed", "production_date", "raw_material"])


product_materials = {
    "00001": {"raw_material": "Inox AISI 303 Ø8", "quantity_per_1000": 100},
    "00002": {"raw_material": "Sc1 Ø11", "quantity_per_1000": 80},
}


suppliers = {
    "Inox AISI 303 Ø8": {"Acerol": 21, "Blausthal": 14, "Premium Steel": 30},
    "Sc1 Ø11": {"Ramada": 10, "Ósorio": 14},
}

def calculate_material_needed(product_code, quantity):
    if product_code in product_materials:
        quantity_per_1000 = product_materials[product_code]["quantity_per_1000"]
        total_needed = (quantity / 1000) * quantity_per_1000  # Calculate total material needed
        raw_material = product_materials[product_code]["raw_material"]
        return raw_material, total_needed
    else:
        return None, None


def show_dashboard():
    dashboard_window = tk.Toplevel()
    dashboard_window.title("Materials Dashboard")

  
    style = ttk.Style()
    style.configure("Treeview", bordercolor="black", borderwidth=2, rowheight=30, font=("Arial", 10))
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#d9d9d9")

    tree = ttk.Treeview(dashboard_window, columns=("order_id", "raw_material", "quantity_needed", "lead_time", "urgency"), show='headings')


    tree.heading("order_id", text="Order ID")
    tree.heading("raw_material", text="Raw Material")
    tree.heading("quantity_needed", text="Quantity Needed (kg)")
    tree.heading("lead_time", text="Lead Time (days)")
    tree.heading("urgency", text="Urgency (days left)")


    tree.column("order_id", width=100, stretch=True)
    tree.column("raw_material", width=200, stretch=True)
    tree.column("quantity_needed", width=150, stretch=True)
    tree.column("lead_time", width=100, stretch=True)
    tree.column("urgency", width=100, stretch=True)


    urgent_materials = []

    for index, order in orders_df.iterrows():
        product_code = order["product_code"]
        quantity = order["quantity"]
        production_date = order["production_date"]
        raw_material, material_needed = calculate_material_needed(product_code, quantity)

        if raw_material:
            due_date = datetime.strptime(production_date, "%d-%m-%Y")
            lead_time_days = min(suppliers[raw_material].values())  # Pick the shortest lead time for urgency
            urgency = (due_date - datetime.now()).days - lead_time_days


            urgent_materials.append((order["order_id"], raw_material, material_needed, lead_time_days, urgency))

   
    urgent_materials.sort(key=lambda x: x[4])  

  
    for material_info in urgent_materials:
        tree.insert("", "end", values=material_info)

    
    scrollbar = ttk.Scrollbar(dashboard_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(expand=True, fill='both')

def show_orders():
    orders_window = tk.Toplevel()
    orders_window.title("All Orders")
    
    style = ttk.Style()
    style.configure("Treeview", bordercolor="black", borderwidth=2, rowheight=30, font=("Arial", 10))
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#d9d9d9")

    tree = ttk.Treeview(orders_window, columns=("order_id", "product_code", "quantity", "material_needed", "production_date", "raw_material"), show='headings')
    
    tree.heading("order_id", text="Order ID")
    tree.heading("product_code", text="Product Code")
    tree.heading("quantity", text="Quantity")
    tree.heading("material_needed", text="Material Needed (kg)")
    tree.heading("production_date", text="Production Date")
    tree.heading("raw_material", text="Raw Material")
    
    tree.column("order_id", width=100, stretch=True)
    tree.column("product_code", width=100, stretch=True)
    tree.column("quantity", width=100, stretch=True)
    tree.column("material_needed", width=150, stretch=True)
    tree.column("production_date", width=150, stretch=True)
    tree.column("raw_material", width=150, stretch=True)

    for index, row in orders_df.iterrows():
        if index % 2 == 0:
            tree.insert("", "end", values=row.tolist(), tags=('evenrow',))
        else:
            tree.insert("", "end", values=row.tolist(), tags=('oddrow',))

    style.configure("evenrow", background="#f0f0f0")
    style.configure("oddrow", background="white")

    scrollbar = ttk.Scrollbar(orders_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    tree.pack(expand=True, fill='both')

def add_order():
    global orders_df  

    order_id = order_id_entry.get()
    product_code = product_code_entry.get()
    quantity = quantity_entry.get()
    production_date = production_date_entry.get()

    if not (order_id and product_code and quantity and production_date):
        messagebox.showerror("Input Error", "All fields must be filled out.")
        return

    if order_id in orders_df["order_id"].values:
        messagebox.showerror("Duplicate Error", f"Order with ID {order_id} already exists.")
        return

    try:
        quantity = float(quantity)
    except ValueError:
        messagebox.showerror("Input Error", "Quantity must be a number.")
        return

    try:
        production_date_obj = datetime.strptime(production_date, "%d-%m-%Y")
        production_date = production_date_obj.strftime("%d-%m-%Y")
    except ValueError:
        messagebox.showerror("Input Error", "Production date must be in dd-mm-yyyy format.")
        return

    raw_material, material_needed = calculate_material_needed(product_code, quantity)
    if raw_material is None:
        messagebox.showerror("Input Error", "Invalid product code.")
        return

    new_order = pd.DataFrame([{
        "order_id": order_id,
        "product_code": product_code,
        "quantity": quantity,
        "material_needed": material_needed,
        "production_date": production_date,
        "raw_material": raw_material,
    }])

    orders_df = pd.concat([orders_df, new_order], ignore_index=True)

    messagebox.showinfo("Success", "Order added successfully!")


app = tk.Tk()
app.title("Production Order App")

tk.Label(app, text="Order ID").pack()
order_id_entry = tk.Entry(app)
order_id_entry.pack()

tk.Label(app, text="Product Code").pack()
product_code_entry = tk.Entry(app)
product_code_entry.pack()

tk.Label(app, text="Quantity").pack()
quantity_entry = tk.Entry(app)
quantity_entry.pack()

tk.Label(app, text="Production Date (DD-MM-YYYY)").pack()
production_date_entry = tk.Entry(app)
production_date_entry.pack()

tk.Button(app, text="Add Order", command=add_order).pack()
tk.Button(app, text="Show All Orders", command=show_orders).pack()
tk.Button(app, text="Show Dashboard", command=show_dashboard).pack()

app.mainloop()
