class Node:
   def __init__(self,data):
       self.data = data
       self.next = None 
    
class linkedlist():
    def __init__(self):
        self.head = None

    #Funcion de linkedlist
    #1._elimina el nodo que se encuentra en una posición específica
    
    def deleteNode(self, position):
        if self.head is None: #Verificar si la lista esta vacia, no hay nada que eliminar y se sale de la funcion
            return
        if position == 0:          #si la posicion es 0, queremos eliminar la cabeza     
            self.head = self.head.next    #movemos la cabeza al siguiente nodo
            return self.head
       
       #variables para recorrer lista
        index = 0    #contador posicion actual
        current = self.head     #nodo actual que estamos examinando
        prev = self.head          #nodo anterior
        temp = self.head           #usamos esta variable para guardar el nodo temporal que se conectara despues
        
        #recorremos la lista nodo por nodo hasta que encontramos el nodo que queremos eliminar
        while current is not None:
            if index == position:   #-> encontramos el nodo que queremos eliminar
                temp = current.next  #guardamos el siguiente nodo 
                break                 #salimos del bucle
            #conectamos el nodo anterior driectamente al siguiente del nodo eliminado
            prev = current          
            current = current.next
            index +=1
        prev.next = temp
        return prev
    
    #este metodo inserta nodos al final de la lista
    def append(self,new_data):
        new_node = Node(new_data)    #creamos el nuevo nodo. anadimos los datos a este elemento y asignamos a su puntero un valor nulo.
        if self.head is None:      #VErificar si la lista enlazada esta vacia. En este caso, el nuevo nodo, seria la cabeza   
            self.head = new_node
            return
        
        #recorremos la lista hasta el final
        last = self.head
        while (last.next) :
            last = last.next
        #modificamos el puntero siguiente del final de la lista al nuevo nodo.
        last.next = new_node
        
    #Funcion que inserta los datos de forma ordenada ascendente
    '''
1️⃣ Si la lista está vacía → el nuevo nodo se convierte en la cabeza.
2️⃣ Si el nuevo valor es menor que la cabeza, se inserta al inicio.
3️⃣ Si no, recorremos la lista hasta encontrar el primer nodo mayor que el nuevo valor.
4️⃣ Insertamos el nuevo nodo justo antes de ese nodo.'''
    def ord_asc(self,new_data):
        new_node = Node(new_data)
        if self.head is None or new_data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next is not None and current.next.data < new_data:
            current = current.next
            new_node.next = current.next
            current.next = new_node
        

   #funcion que recorre y muestra los elementos de la lista enlazada   
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = ' ')
            temp = temp.next
            
            

#Funcion principal

if __name__ == '__main__':
    
    #inicialmente creamos la lista vacia
    llist = linkedlist()
    
    #Insertamos un elemento, 6
    llist.append(5)
    llist.append(10)
    llist.append(15)
    llist.append(20)
    llist.append(25)
   

    
    print('La lista creada es: ')
    llist.printList()
    
    llist.deleteNode(2)
    print(" Despues de eliminar posicion 2 (15): " )
    llist.printList()
