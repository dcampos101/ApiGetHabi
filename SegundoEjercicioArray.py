# Declaracion de arreglo para pruebas
myArray = (8, 33, 0, 2, 7, 99, 0, 3, 0, 3, 2, 1)

# Creacion de listas una que sea tempral y la otra la final
bloque_actual = []
bloques_ordenados = []

# Ciclo para recorrer el arreglo 
for num in myArray:
    # condicion para validar si es el fin del bloque 
    if num != 0:
        bloque_actual.append(num)
    else:
        # Ordenar el bloque actual y convertirlo a cadena
        bloques_ordenados.append(''.join(map(str, sorted(bloque_actual))))
        bloque_actual = []

# Agregar el último bloque si no terminó en 0
if bloque_actual:
    bloques_ordenados.append(''.join(map(str, sorted(bloque_actual))))

# Unir bloques separados por espacio
resultado = ' '.join(bloques_ordenados)
print(resultado)