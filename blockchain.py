import json
import hashlib
import os
import datetime



def stampa():
    data = json.load(open('blockchain.json', 'r'))
    for i in data:
        timestamp = i.get('timestamp')
        hashprec = i.get('hash_prec') 
        transazione = i.get('transazione')
        nonce=i.get('nonce')
        difficolta=i.get('difficolta')
        hash = i.get('hash')
        print(f"\nTimestamp: {timestamp} \nhashprec: {hashprec} \ntransazione: {transazione} \nnonce: {nonce} \ndifficolta: {difficolta}\nhash: {hash}")

def aggiungi_blocco():
    data=load_data()
    timestamp=get_date()
    transazione=input("\ninserisci descrizione della transazione: ")
    hash_prec=""
    for i in data:
        hash_prec=i.get('hash')
    nonce=0
    difficolta=5
    diff=""
    for i in range(difficolta):
        diff+="0"
    hash="11"
    while not hash.startswith(diff):
        hash=get_hash(timestamp+hash_prec+transazione+str(nonce)+str(difficolta))
        nonce+=1
    
    
    blocco = {
        "timestamp": timestamp,
        "hash_prec": hash_prec,
        "transazione":transazione,
        "nonce":nonce,
        "difficolta":difficolta,
        "hash":hash
    }
    data.append(blocco)
    # Salviamo i dati aggiornati nel file JSON
    with open('blockchain.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Blocco aggiunto con successo!")
    

     
def get_date():
    return datetime.datetime.now().strftime("%d %m %Y %H %M %S")

def get_hash(tohash):
    string=tohash.encode("utf-8")
    return hashlib.sha256(string).hexdigest()

def load_data():
    if os.path.exists("blockchain.json"):
        with open("blockchain.json", "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open("blockchain.json", "w") as file:
        json.dump(data, file, indent=4)

def create_blockchain():
    data=load_data()
    if data==[]:
        date=get_date()
        difficolta=5
        nonce=0
        fingerprint="11"
        diff=""
        for i in range(difficolta):
            diff+="0"
        while not fingerprint.startswith(diff):
            fingerprint=get_hash(date+"GEN-000"+"creazione della blockchain"+str(nonce)+str(difficolta))
            nonce+=1        
        data.append({
            "timestamp":date,
            "hash_prec":"GEN-000",
            "transazione":"creazione della blockchain",
            "nonce":nonce,
            "difficolta":difficolta,
            "hash":fingerprint
        })
        save_data(data)


def main():
    create_blockchain()
    stampa()
    aggiungi_blocco()
    #aggiungi_blocco()
    stampa()


if __name__ == "__main__":
    main()





