import hashlib
str_da_controllare="ciao"
hashed_str=hashlib.sha256(str_da_controllare.encode("utf-8")).hexdigest()
hash_es1=input("incolla l'hash dell'esercizio precedente che hai calcolato per la parola 'ciao':")
if(hashed_str==hash_es1):
    print("la stringa è integra!")
else:
    print("la stringa non è integra!")
