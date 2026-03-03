mezcla = [5, "A", 2, "B"]

# key=str convierte temporalmente el 5 en "5" y el 2 en "2"
resultado = sorted(mezcla, key=str)

print(resultado) 
# Salida: [2, 5, 'A', 'B']
