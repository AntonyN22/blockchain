import locale
import datetime

# Impostare la localizzazione per l'Italia
#locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

# Ottieni la data e l'orario attuali
now = datetime.datetime.now()

# Stampa la data in formato italiano
print(now.strftime("%d %m %Y"))
