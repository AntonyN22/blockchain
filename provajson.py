import json
import hashlib



def genera_hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest() 


def aggiungi_utente():
    user = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")

    password_hash = genera_hash_password(password)

    
    
    with open('data.json', 'r') as file:
        dati_utenti = json.load(file)
   

    
    nuovo_utente = {
        "user": user,
        "password": password_hash
    }
    dati_utenti.append(nuovo_utente)

    # Salviamo i dati aggiornati nel file JSON
    with open('data.json', 'w') as file:
        json.dump(dati_utenti, file, indent=4)

    print(f"Utente {user} aggiunto con successo!")


def stampa(): 
    data = json.load(open('data.json', 'r'))
    for i in data:
        user = i.get('user')
        password = i.get('password') 
        #print(f"User: {user} - Password: {password}")
        print("user: ",user," - password: ",password)

def rimuovi_utente():
    user_da_rimuovere = input("Inserisci il nome utente da rimuovere: ")

    # Carichiamo i dati esistenti dal file JSON
    dati_utenti = json.load(open('data.json', 'r'))

    # Cerchiamo l'utente da rimuovere
    utente_trovato = False
    for utente in dati_utenti:
        if utente["user"] == user_da_rimuovere:
            dati_utenti.remove(utente)
            utente_trovato = True
            break

    if utente_trovato:
        # Salviamo i dati aggiornati nel file JSON
        with open('data.json', 'w') as file:
            json.dump(dati_utenti, file, indent=4)
        print(f"Utente {user_da_rimuovere} rimosso con successo!")
    else:
        print(f"L'utente {user_da_rimuovere} non è stato trovato.")


stampa()
rimuovi_utente()
aggiungi_utente()
stampa()


        


