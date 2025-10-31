# Las listas enlazadas se pueden programar con clases, y los nodos de la lista como otra clase de objetos.

#Clase Nodo. (bloque basico) crea los ladrillos individuales de la lista
class Node:
    #funcion que crea un objeto nodo
    def __init__(self,data):
        self.data = data #asignamos data al elemento
        self.next = None #puntero al siguiente nodo,  inicialmente la lista está vacía.

# Clase ListaEnlazada. Contiene un objeto nodo.  Estructura que organiza los nodos. 
# Es una estructura que contiene y gestiona todos los nodos.       
class LinkedList:
    def __init__(self):
        self.head = None #primer nodo de la lista. La cabeza
        

#Funcion de la clase LinkesList

###insertar un nodo al inicio. push### /4 pasos/
    def push(self,new_data):       
        new_node = Node(new_data)    #creamos un nuevo nodo y asignamos los datos al elemento
        new_node.next = self.head     #el nuevo nodo, se anade previo a la cabeza
        self.head = new_node       #LA nueva cabeza de la lista es este nuevo nodo.
        


#Funcion de la clase LinkesList

###insertar un nodo en una posicion especifica. ### /5 pasos/
    def insertAfter(self,prev_node, new_data):    
        if prev_node is None:                              #verificar si el nodo previo existe, si no esta vacio.
            print('El nodo previo, no existe en la lista')
            return
        
        new_node = Node(new_data)    #creamos el nuevo nodo y anadimos los datos al elemento
        new_node.next = prev_node.next  # el elemento siguiente del nuevo nodo es el nodo siguiente anterior
        prev_node.next = new_node      #el siguiente nodo, del nodo previo es el nuevo nodo.
        
        

#Funcion de la clase LinkesList

###insertar un nodo al final. ### 6 pasos
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
     
    #funcion que recorre y muestra los elementos de la lista enlazada   
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = ' ')
            temp = temp.next

#Funcion principal

if __name__ == '__main__':
    
    #inicialmente creamos la lista vacia
    llist = LinkedList()
    
    #Insertamos un elemento, 6
    llist.append(6)
    
    #Insertamos un nodo con dato 7 al inicio
    llist.push(7)
    
    #insertamos ahora un 4 al final
    llist.append(4)
    
    #insertamos un dato 8, despues del nodo cabeza con el 7
    llist.insertAfter(llist.head.next, 8)
    
    print('La lista creada es: ')
    llist.printList()
    
    
        
        