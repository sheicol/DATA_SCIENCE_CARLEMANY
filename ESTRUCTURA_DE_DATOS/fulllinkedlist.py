#Clase Nodo
class Node:
    #funcion que crea un objeto nodo. Crea los ladrillos individuales de la lista
    def __init__(self,data):
        self.data = data    #asignamos data al elemento
        self.next = None     #puntero al siguiente nodo, vacio inicialmente

#Clase lista Enlazada. contiene un objeto nodo.Estructura que gestiona o contiene todos los nodos.
# mostrar, anadir, eliminar, etc

class LinkedList:
    #Funcion que crea la lista inicial con un nodo cabeza.
    def __init__(self):    
        self.head = None 
    
    #Mostramos los elementos de la lista enlazadas, empezando por la cabeza
    def printList(self):  
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next 
            
#Funcion principal
if __name__ =='__main__':
        #creamos la lista, vacia inicialmente
    llist = LinkedList()
    
    llist.head = Node('I')  #creamos 3 nodos
    second = Node('<3')
    third  = Node('U')
    
llist.head.next = second;  #enlazamos la cabeza con el segundo
second.next = third;       #enlazamos el segundo con el tercero

llist.printList()        #mostramos la lista