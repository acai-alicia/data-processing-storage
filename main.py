import tkinter as tk
from tkinter import messagebox
from inmemorydb import InMemoryDB

db = InMemoryDB()

# user interface to interact with InMemoryDB
def user_interface():
    def handle_get():
        key = key_entry.get()
        value = db.get(key) # retrieve value
        messagebox.showinfo("Get Result", f"Value for key '{key}': {value}")

    def handle_put():
        key = key_entry.get()
        try:
            value = int(value_entry.get()) # convert the input to an integer
            db.put(key, value) # store value
            messagebox.showinfo("Success", f"Key '{key}' set to {value} (in transaction)")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the value.") # invalid value error
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
    root.resizable(False, False) # keeps box size fixed/prevents resize

    root.grid_columnconfigure(0, weight=1, minsize=100)
    root.grid_columnconfigure(1, weight=1, minsize=100)

    tk.Label(root, text="Key:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    key_entry = tk.Entry(root)
    key_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    tk.Label(root, text="Value:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    value_entry = tk.Entry(root)
    value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    
    # button styling and positioning
    tk.Button(root, text="Get", command=handle_get).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Put", command=handle_put).grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Begin Transaction", command=handle_begin_transaction).grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(root, text="Commit", command=handle_commit).grid(row=5, column=0, columnspan=2, padx=10, pady=5,)
    tk.Button(root, text="Rollback", command=handle_rollback).grid(row=6, column=0, columnspan=2, padx=10, pady=5,)


    root.mainloop()

user_interface()


'''

steps:
----------------------------------------------------------------------------------------
1. type "A" in key then press "get"
    this should return none, because "A" doesn't exist in the DB yet
    
2. type "A" in key, type "5" in the value, then press "put"
    this should throw an error, because a transaction is not in progress
    
3. press "begin transaction"
    this starts a new transaction!
    
4. type "A" in key, type "5" in the value, then press "put"
    this sets value of A to 5, but it's not committed yet
    
5. type "A" in key, press "get"
    this should return none, because updates to A are not committed yet
    
6. type "A" in key, type "6" in the value, press "put"
    this should update the value of A to 6
    
7. press "commit"
    this should commit the open transaction
    
8. type "A" in key, press "get"
    this should return 6; that was the last value of A to be committed
    
9. press "commit"
    this should throw an error because there is no open transaction
    
10. press "rollback"
    this should throw an error because there is no ongoing transaction
    
11. type "B" in key, press "get"
    this should return none, because "B" doesn't exist in the DB yet
    
12. press "begin transaction"
    this starts a new transaction
    
13. type "B" in key, type "10" in the value, then press "put"
    this sets value of B to 10, but it's not committed yet

14. press "rollback"
    this should revert any changes made to B
    
15. type "B" in key, press "get"
    this should return none because changes to B were rolled back
    
**feel free to press "get" after putting and committing a value to the key to make sure it is there 
    
'''
