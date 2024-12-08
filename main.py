import tkinter as tk
from tkinter import messagebox
from inmemorydb import InMemoryDB

db = InMemoryDB()

def user_interface():
    def handle_get():
        key = key_entry.get()
        value = db.get(key)
        messagebox.showinfo("Get Result", f"Value for key '{key}': {value}")

    def handle_put():
        key = key_entry.get()
        try:
            value = int(value_entry.get())
            db.put(key, value)
            messagebox.showinfo("Success", f"Key '{key}' set to {value} (in transaction)")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the value.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_begin_transaction():
        try:
            db.begin_transaction()
            messagebox.showinfo("Transaction", "Transaction started.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_commit():
        try:
            db.commit()
            messagebox.showinfo("Transaction", "Transaction committed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def handle_rollback():
        try:
            db.rollback()
            messagebox.showinfo("Transaction", "Transaction rolled back.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Data Processing and Storage Assignment")

    root.geometry("400x270")
    root.resizable(False, False)

    # Configure grid layout to ensure elements are aligned
    root.grid_columnconfigure(0, weight=1, minsize=100)
    root.grid_columnconfigure(1, weight=1, minsize=100)

    # Key Input
    tk.Label(root, text="Key:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    key_entry = tk.Entry(root)
    key_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Value Input
    tk.Label(root, text="Value:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    value_entry = tk.Entry(root)
    value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Buttons
    tk.Button(root, text="Get", command=handle_get).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Put", command=handle_put).grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Begin Transaction", command=handle_begin_transaction).grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Commit", command=handle_commit).grid(row=5, column=0, columnspan=2, padx=10, pady=5,)
    tk.Button(root, text="Rollback", command=handle_rollback).grid(row=6, column=0, columnspan=2, padx=10, pady=5,)


    root.mainloop()

user_interface()