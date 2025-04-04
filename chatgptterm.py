import hashlib
import json
import os

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
def login(data):
    username = input("Nome utente: ")
    password = input("Password: ")

    # Verifica se l'utente esiste e la password è corretta
    for entry in data:
        if entry["user"] == username and entry["password"] == hash_password(password):
            print(f"Benvenuto {username}!")
            return
    print("User o password incorretti.")

# Funzione per la registrazione
def register(data):
    username = input("Nome utente: ")
    
    # Verifica se l'utente esiste già
    for entry in data:
        if entry["user"] == username:
            print("Nome utente già esistente.")
            return

    password=""
    while password=="":    
        password = input("Password: ")
    hashed_password = hash_password(password)

    # Aggiungi l'utente e la password (hashata) alla lista
    data.append({"user": username, "password": hashed_password})
    save_data(data)
    print(f"Registrazione completata per {username}!")

# Funzione principale
def main():
    data = load_data()

    while True:
        print("\n1. Login")
        print("2. Registrazione")
        print("3. Esci")
        choice = input("Scegli un'opzione: ")

        if choice == '1':
            login(data)
        elif choice == '2':
            register(data)
        elif choice == '3':
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
