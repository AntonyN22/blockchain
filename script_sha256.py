import hashlib
print("inserisci una stringa di cui vuoi ottenere l'hash sha256: ")
stringa=input()
stringa2=stringa.encode("utf-8")
hashed_string=hashlib.sha256(stringa2).hexdigest()
print("impronta: ",hashed_string)
print("impronta in binario: ",bin(int(hashed_string,16)))