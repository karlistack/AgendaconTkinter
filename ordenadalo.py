import csv

# ----------------- FUNCTION FOR READ THE CSV FILE ---------------------------------------------

def ordenalphabetico():
    orden = []
    fila = []
    with open('contacts_list.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            nombre = str(row[0])
            telefono = str(row[1])
            email = str(row[2])
            fila = [nombre, telefono, email]
            orden.append(fila)
    ordenalphabetico_list = ordenamiento_por_mezcla(orden)
    return ordenalphabetico_list
    

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[ : medio]
        derecha = lista[medio : ]
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        i = 0
        j = 0
        k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = derecha[j]
                j += 1
            else:
                lista[k] = izquierda[i]
                i += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha [j]
            j += 1
            k += 1
    return lista