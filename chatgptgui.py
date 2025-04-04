
import hashlib
import json
import os
import tkinter as tk
from tkinter import messagebox

# Funzione per caricare i dati dal file JSON
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return []

# Funzione per salvare i dati nel file JSON
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Funzione per fare l'hash della password usando SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funzione per il login
def login(data, username, password):
    for entry in data:
        if entry["user"] == username and entry["password"] == hash_password(password):
            messagebox.showinfo("Login", f"Benvenuto {username}!")
            return
    messagebox.showerror("Login", "User o password incorretti.")

# Funzione per la registrazione
def register(data, username, password):
    for entry in data:
        if entry["user"] == username:
            messagebox.showerror("Registrazione", "Nome utente già esistente.")
            return

    

    hashed_password = hash_password(password)
    data.append({"user": username, "password": hashed_password})
    save_data(data)
    messagebox.showinfo("Registrazione", f"Registrazione completata per {username}!")

# Funzione principale per la GUI
def main_gui():
    data = load_data()
    
    root = tk.Tk()
    root.title("Autenticazione")

    def on_login():
        username = entry_username.get()
        password = entry_password.get()
        login(data, username, password)

    def on_register():
        username = entry_username.get()
        password = entry_password.get()
        register(data, username, password)

    # Layout
    tk.Label(root, text="Nome utente:").grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(root, text="Login", command=on_login).grid(row=2, column=0, columnspan=2)
    tk.Button(root, text="Registrati", command=on_register).grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
