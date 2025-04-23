import tkinter as tk
from tkinter import ttk

# Sample data
data = [
    ("1", "Alice", "Engineer"),
    ("2", "Bob", "Doctor"),
    ("3", "Charlie", "Teacher"),
]

def show_selected():
    selected_item = tree.focus()  # get currently selected item
    if selected_item:
        values = tree.item(selected_item, "values")
        print("Selected Row:", values)

# Create main window
root = tk.Tk()
root.title("DataTable with Tkinter")
root.geometry("400x300")

# Create Treeview
tree = ttk.Treeview(root, columns=("ID", "Name", "Profession"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Profession", text="Profession")

# Insert data into the Treeview
for row in data:
    tree.insert("", tk.END, values=row)

tree.pack(pady=20)

# Create Show button
show_button = tk.Button(root, text="Show", command=show_selected)
show_button.pack()

# Run the app
root.mainloop()
