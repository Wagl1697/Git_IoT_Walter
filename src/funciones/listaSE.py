# -*- coding: utf-8 -*-

# TAD Lista Simplemente Enlazada
# Implementar el tipo abstracto de dato (TAD) Lista utilizando la estructura de datos (ED) 
# de nodos simplemente enlazados para almacenar elementos de cualquier tipo. 
# Utilizar un TAD Nodo para gestionar la estructura de datos interna. 
#La lista debe permitir las siguientes operaciones:
    # Crear una lista vacía (implementar inicializador).
    # Destruir la lista (implementar destructor).
    # Copiar la lista (implementar método “copiar”) para generar una copia profunda.
    # Agregar un elemento en cualquier posición de la lista. La posición debe ser válidaw.
    # Invertir el orden de los elementos de la lista.
    # Iterar sobre la lista.
    # eOrdenar de “menor a mayor” los elementos de la lista.

class Nodo:
    def __init__(self, p_dato):
        self.dato = p_dato
        self.siguiente = None
        
    def __str__(self):
        return f'Nodo({self.dato})'


class Lista:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
        
        
    def agregar(self, p_posicion, p_dato):
        
        if not 0 <= p_posicion <= self.tamanio:
            raise IndexError('Indice de la lista fuera de rango')
        
        # Se cumple: 0 <= p_posicion <= self.tamanio
        
        nuevo_nodo = Nodo(p_dato)
        
        # caso 1: no hay nodos en la lista.
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            
        # caso 2: se agrega al inicio de la lista
        elif p_posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
        # caso 3: se agrega en alguna posición posterior al inicio
        else:
            nodo_antecesor = self.cabeza
            # se avanza nodo hasta la posición anterior donde se desea insertar el nodo.
            for _ in range(p_posicion - 1):
                nodo_antecesor = nodo_antecesor.siguiente
            nuevo_nodo.siguiente = nodo_antecesor.siguiente
            nodo_antecesor.siguiente = nuevo_nodo
            
        self.tamanio += 1
        pass
    
    def __setitem__(self, p_posicion, p_dato):
        self.agregar(p_posicion, p_dato)
        
    
    def devolver(self, p_posicion):
        
        if not 0 <= p_posicion <= self.tamanio - 1:
            raise IndexError('Indice de la lista fuera de rango')
            
        # Se cumple: 0 <= p_posicion < self.tamanio
        
        nodo_aux = self.cabeza
        
        for _ in range(p_posicion):   # o "self.tamanio - 1"
            nodo_aux = nodo_aux.siguiente
        
        return nodo_aux.dato
    
        
    def __getitem__(self, p_posicion):
        return self.devolver(p_posicion)
    
    
    def __iter__(self):
        nodo = self.cabeza
        while nodo is not None:      # nodo != None
            yield nodo.dato
            nodo = nodo.siguiente

    
    def __str__(self):
        cad = ''
        for dato in self:
            cad += str(dato) + ' -> '
        cad = cad[:-4]
        return cad
    
    
    def __del__(self):
        self.vaciar()

    
    def copiar(self):
        '''
        Crea una copia profunda de la lista y retorna una referencia a la misma.

        Returnsw
        -------
        lis_copia : Lista
            Copia de la lista original.

        '''
        lis_copia = Lista()
        lis_copia.vaciar()
        nodo_aux = self.cabeza
        for _ in self:
            lis_copia.agregar(lis_copia.get_longitud(), nodo_aux.dato)
            nodo_aux = nodo_aux.siguiente

        return lis_copia
    
    
    def invertir(self):
        
        nodo_actual = self.cabeza
        nodo_previo = None
        nodo_siguiente = None
        while nodo_actual != None:
            nodo_siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_previo
            nodo_previo = nodo_actual
            nodo_actual = nodo_siguiente
        self.cabeza = nodo_previo

        pass
  
    
  
    def ordenar(self):
        
        nodo_actual = self.cabeza
        nodo_siguiente = nodo_actual.siguiente
        dato = 0
    
        while nodo_actual.siguiente != None:
            nodo_siguiente = nodo_actual.siguiente
            while nodo_siguiente != None:
                if nodo_actual.dato > nodo_siguiente.dato:
                    dato = nodo_siguiente.dato
                    nodo_siguiente.dato = nodo_actual.dato
                    nodo_actual.dato = dato
                nodo_siguiente = nodo_siguiente.siguiente
            nodo_actual = nodo_actual.siguiente
            nodo_siguiente = nodo_actual.siguiente
    
    
    def __len__(self):
        return self.get_longitud()
    
    
    def get_longitud(self):
        return self.tamanio
    
    
    def esta_vacia(self):
        '''
        Retorna True si la lista está vacía.

        Returns
        -------
        Verdadero si la lista está vacía.

        '''
        return True if self.tamanio == 0 else False
   
    def vaciar(self):
        self.cabeza = None
        self.tamanio = 0
    
    # def borrar(self, pos):
    #     nodo_aux = self.cabeza
    #     nodo_borrar = None
    #     if pos >= 0 and pos <= self.tamanio:
    #         if pos > 0:
    #             for i in self[pos-1]:
    #                 nodo_aux = nodo_aux.siguiente
    #             nodo_borrar = nodo_aux.siguiente
    #             nodo_aux.siguiente = nodo_borrar.siguiente
    #         else:
    #             nodo_borrar = self.cabeza
    #             self.cabeza = self.cabeza.siguiente
    #         --self.tamanio
    #     else:
    #         raise IndexError('Indice de la lista fuera de rango')
    #     pass
    
if __name__ == '__main__':
    n1 = Nodo(1)
    n2 = Nodo(2)
    
    # print(n1)
    # print(n2)
    print(str(n1))
    print(str(n2))
    
    














