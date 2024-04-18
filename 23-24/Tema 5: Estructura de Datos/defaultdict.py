
# Un diccionario por defecto en el que no sé las claves en un momento dado
# puedo crear claves y ponerles un valor por defecto.

from collections import defaultdict

cadena = "Sí  perdió el atlieti y hoy ganará el Real Madrid Madrid"
lines = cadena.split()

word_counts = defaultdict(int)

for word in lines:
    word_counts[word] += 1
    
    
print (word_counts)