class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    # 1️⃣ Elimina el nodo que se encuentra en una posición específica
    def deleteNode(self, position):
        if self.head is None:  # Si la lista está vacía
            return

        if position == 0:  # Si se quiere eliminar la cabeza
            self.head = self.head.next
            return self.head

        index = 0
        current = self.head
        prev = self.head
        temp = self.head

        # Recorremos hasta la posición deseada
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    # 2️⃣ Inserta nodos al final de la lista
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 3️⃣ Inserta datos en orden ascendente
    def ord_asc(self, new_data):
        new_node = Node(new_data)

        # Caso 1: lista vacía o nuevo valor menor que la cabeza
        if self.head is None or new_data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        # Caso 2: recorrer hasta encontrar la posición adecuada
        current = self.head
        while current.next is not None and current.next.data < new_data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # 4️⃣ Ordena toda la lista existente de forma ascendente
    def sort_asc(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = linkedlist()
        current = self.head

        while current is not None:
            sorted_list.ord_asc(current.data)
            current = current.next

        self.head = sorted_list.head

    # 5️⃣ Muestra los elementos de la lista enlazada
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# 🔹 Función principal
if __name__ == '__main__':
    llist = linkedlist()

    # Insertar elementos de forma no ordenada
    llist.append(30)
    llist.append(10)
    llist.append(25)
    llist.append(15)
    llist.append(20)
    llist.append(5)

    print("Lista original:")
    llist.printList()

    # Eliminar posición 2 (el 25)
    llist.deleteNode(2)
    print("\nDespues de eliminar posicion 2 (25):")
    llist.printList()

    # Ordenar lista completa
    llist.sort_asc()
    print("\nLista ordenada ascendentemente:")
    llist.printList()

    # Insertar un nuevo valor en orden
    llist.ord_asc(45)
    llist.ord_asc(40)
    llist.ord_asc(25)
    llist.ord_asc(35)
    print("\nDespues de insertar 25 en orden ascendente:")
    llist.printList()

