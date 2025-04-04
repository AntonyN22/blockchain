import json
import hashlib
import os
import datetime
import tkinter as tk
from tkinter import scrolledtext

# Funzione per stampare i blocchi nella finestra di testo scorrevole
def stampa():
    data = load_data()
    output_txtbox.delete(1.0, tk.END)  # Pulisce il contenuto della casella di testo
    for i in data:
        timestamp = i.get('timestamp')
        hashprec = i.get('hash_prec') 
        transazione = i.get('transazione')
        nonce = i.get('nonce')
        difficolta = i.get('difficolta')
        hash = i.get('hash')
        output_txtbox.insert(tk.END, f"\nTimestamp: {timestamp}\nHash Prec: {hashprec}\nTransazione: {transazione}\nNonce: {nonce}\nDifficolta: {difficolta}\nHash: {hash}\n")

# Funzione per aggiungere un blocco tramite la GUI
def aggiungi_blocco():
    data = load_data()
    timestamp = get_date()
    transazione = entry_transazione.get()  # Ottieni il testo dalla casella di input
    hash_prec = ""
    for i in data:
        hash_prec = i.get('hash')
    nonce = 0
    difficolta = 5
    diff = "0" * difficolta
    hash = "11"
    while not hash.startswith(diff):
        hash = get_hash(timestamp + hash_prec + transazione + str(nonce) + str(difficolta))
        nonce += 1
    
    blocco = {
        "timestamp": timestamp,
        "hash_prec": hash_prec,
        "transazione": transazione,
        "nonce": nonce,
        "difficolta": difficolta,
        "hash": hash
    }
    data.append(blocco)
    save_data(data)
    #output_txtbox.insert(tk.END, f"Blocco aggiunto con successo!\n")
    stampa()  # Ristampa la blockchain aggiornata

# Funzione per ottenere la data corrente
def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Funzione per generare un hash
def get_hash(tohash):
    string = tohash.encode("utf-8")
    return hashlib.sha256(string).hexdigest()

# Funzione per caricare i dati esistenti dalla blockchain (file JSON)
def load_data():
    if os.path.exists("blockchain.json"):
        with open("blockchain.json", "r") as file:
            return json.load(file)
    return []

# Funzione per salvare i dati della blockchain nel file JSON
def save_data(data):
    with open("blockchain.json", "w") as file:
        json.dump(data, file, indent=4)

# Funzione per creare la blockchain iniziale se il file è vuoto
def create_blockchain():
    data = load_data()
    if data == []:
        date = get_date()
        difficolta = 5
        nonce = 0
        fingerprint = "11"
        diff = "0" * difficolta
        while not fingerprint.startswith(diff):
            fingerprint = get_hash(date + "GEN-000" + "creazione della blockchain" + str(nonce) + str(difficolta))
            nonce += 1        
        data.append({
            "timestamp": date,
            "hash_prec": "GEN-000",
            "transazione": "creazione della blockchain",
            "nonce": nonce,
            "difficolta": difficolta,
            "hash": fingerprint
        })
        save_data(data)

# Funzione per lanciare la GUI
def start_gui():
    # Creare la finestra principale
    root = tk.Tk()
    root.title("Blockchain GUI")

    # Casella di testo scorrevole per le stampe della blockchain
    global output_txtbox
    output_txtbox = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
    output_txtbox.pack(padx=10, pady=10)

    # Casella di input per inserire una nuova transazione
    global entry_transazione
    entry_transazione = tk.Entry(root, width=40)
    entry_transazione.pack(padx=10, pady=10)

    # Pulsante per aggiungere un blocco
    pulsante_aggiungi = tk.Button(root, text="Aggiungi Blocco", command=aggiungi_blocco)
    pulsante_aggiungi.pack(padx=10, pady=10)

    # Creare la blockchain se non esiste
    create_blockchain()

    # Mostra la blockchain iniziale
    stampa()

    # Avviare l'interfaccia grafica
    root.mainloop()

# Esegui l'interfaccia grafica
if __name__ == "__main__":
    start_gui()
