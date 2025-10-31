def intercambio(lista, i, j):
    """Intercambia los elementos en las posiciones i y j de la lista."""
    lista[i], lista[j] = lista[j], lista[i]

def partir(lista, inicio, fin):
    indice_pivot = fin
    indice_partido = inicio
    for indice in range(inicio, fin):
        if lista[indice] < lista[indice_pivot]:
            intercambio(lista, indice_partido, indice)
            indice_partido +=1
    intercambio(lista, indice_partido, indice_pivot)
    indice_pivot = indice_partido
    return indice_pivot



def quick_sort(lista, inicio, fin):
    if inicio < fin:
        pivot = partir(lista, inicio, fin)
        quick_sort(lista, inicio, pivot-1)
        quick_sort(lista, pivot+1, fin)

[8,4,3,5,2,9,1]  
    
    
    
    
    
    
                