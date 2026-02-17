class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# Clase Listas enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacia
    def vacio(self):
        if self.cabeza == None:
            print("Está vacia")
        else:
            print("Lista no vacia")

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
    
    # Insertar al final
    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    #Agregar algo antes de un elemento x
    def insertarAntes(self,x,data):
        #Para lista vacía
        if self.cabeza is None:
            print("Lista vacía, no se puede insertar.")
            return
        #Para X siendo el primero
        if self.cabeza.data==x:
            nuevo_nodo=Nodo(data)
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza=nuevo_nodo
            return
        #Buscar X en la lista
        actual=self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data == x:
                nuevo_nodo= Nodo(data)
                nuevo_nodo.siguiente=actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual=actual.siguiente
        print(f"El elemento {x} no se encuentra en la lista.")
    
    #Añadir un elemento después de X
    def insertarDsp(self,x,data):
        #Para lista vacía
        if self.cabeza is None:
            print("Lista vacía, no se puede insertar.")
            return
        #Para X siendo el primero
        if self.cabeza.data==x:
            nuevo_nodo=Nodo(data)
            nuevo_nodo.siguiente=self.cabeza.siguiente
            self.cabeza.siguiente=nuevo_nodo
            return
        #Buscar X en la lista
        actual=self.cabeza
        while actual.siguiente is not None:
            if actual.data==x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente=actual.siguiente
                actual.siguiente=nuevo_nodo



        
    # Método para recorrer e imprimir la lista
    def imprimir(self):
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía")
            return
        
        print("Elementos de la lista:")
        while actual is not None:
            print(f"[{actual.data}]", end=" -> ")
            actual = actual.siguiente
        print("None")

# --- USO DEL CÓDIGO (Sin espacios al inicio) ---
mi_lista = ListaSE()
mi_lista.agregarFinal(10)
mi_lista.agregarFinal(20)
mi_lista.agregarFinal(30)

print("Antes de insertar:")
mi_lista.imprimir()

mi_lista.insertarAntes(20, 15) # Insertar 15 antes del 20

print("Despues de insertar:")
mi_lista.imprimir()