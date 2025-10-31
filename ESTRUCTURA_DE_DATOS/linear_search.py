#busqueda lineal con dos if
def search (arr,search_Element):  
    left = 0                #empieza desde el inicio del arreglo (posicion 0).
    lenght =len(arr)       
    right = lenght - 1     #empieza desde el final del arreglo (posición len(arr)-1)
    position = -1
    
#bucle de 0 a right.

    for left in range(0, right, 1):  #Se hacen dos comprobaciones en cada iteración:

           
#condicion de elemento encontrado con la variable left. PRIMERA COMPORBACION
        if (arr[left] == search_Element):
            position = left
            print('Elemento encontrado en la posicion ', position + 1, ' en ', left +1, 'pasos')
            break
        
#condicion de elemento encontrado con la variable right. SEGUNDA COMPROBACION

        if (arr[right] == search_Element):
            position = right
            print('Elemento encontrado en la posicion ', position + 1, ' en ', lenght - right, 'pasos')
            break
        left += 1
        right -= 1
        
# el algoritmo busca desde ambos extremos hacia el centro.
        
#Caso en que el elemento no se encuentra
    if (position == -1):
        print('Elemento no encontrado ', left, 'pasos')
        
#ejemplo
arr = [1,2,3,4,5]
search_Element = 5

search(arr, search_Element)