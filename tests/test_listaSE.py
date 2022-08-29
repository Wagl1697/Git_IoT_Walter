# -*- coding: utf-8 -*-

'''
Módulo para probar el TAD Lista de nodos simplemente enlazados.
'''
import sys
print(sys.path)
import unittest
import random
from modulos.listaSE import Lista


class TestListaSE(unittest.TestCase):
    
    def setUp(self):
        # Permite inicializar CADA test.
        
        self.lista_vacia = Lista()
        
        self.lista_no_vacia = Lista()       # *
        self.lista_no_vacia.agregar(0, 10)  # 10
        self.lista_no_vacia.agregar(0, 20)  # 20 -> 10
        self.lista_no_vacia[1] = 30         # 20 -> 30 -> 10
        

    def test_imprimir_lista(self):
        self.assertEqual(str(self.lista_no_vacia), '20 -> 30 -> 10')
    

    def test_verificar_tamaño_lista_vacia(self):
        self.assertEqual(0, len(self.lista_vacia))
        
        
    def test_tamaño_lista_no_vacia(self):
        self.assertEqual(3, len(self.lista_no_vacia))
        
        
    def test_suma_de_elementos(self):
        suma_correcta = 60
        suma = 0
        for elemento in self.lista_no_vacia:
            suma += elemento
        self.assertEqual(suma, suma_correcta)
    
    
    def test_verificar_lista_vacia(self):
        vacia = self.lista_vacia.esta_vacia()
        self.assertTrue(vacia)
        
        
    def test_lista_no_vacia(self):
        # se prueba método
        self.assertEqual(self.lista_no_vacia.devolver(0), 20)
        self.assertEqual(self.lista_no_vacia.devolver(1), 30)
        self.assertEqual(self.lista_no_vacia.devolver(2), 10)
        # se prueba sobrecarga
        self.assertEqual(self.lista_no_vacia[0], 20)
        self.assertEqual(self.lista_no_vacia[1], 30)
        self.assertEqual(self.lista_no_vacia[2], 10)
            
    
    def test_copiar(self):
        
        lista_copia = self.lista_no_vacia.copiar()
        for i in range(len(lista_copia)):
            self.assertEqual(self.lista_no_vacia[i], lista_copia[i]) # son objetos con el mismo valor.

        
    def test_verificar_lista_invertida(self):
        
        self.lista_no_vacia.vaciar()
        
        for i in range(0,10):
            self.lista_no_vacia.agregar(0, random.randint(-100,100))
        
        datos = []
        for dato in self.lista_no_vacia:
            datos.append(dato)
        
        datos = []
        for dato in self.lista_no_vacia:
            datos.append(dato)
        self.lista_no_vacia.invertir()
        i = len(datos)
        
        for dato in self.lista_no_vacia:
            self.assertEqual(datos[i-1], dato)
            i -= 1

    def test_ordenamiento(self):

        for i in range(0,10):
            self.lista_no_vacia.agregar(0, random.randint(-100,100))
            
        datos = []
        for dato in self.lista_no_vacia:
            datos.append(dato)
        datos.sort()

        self.lista_no_vacia.ordenar()

        for i in range(len(datos)):
            self.assertEqual(self.lista_no_vacia[i], datos[i])
    
if __name__ == '__main__':
    unittest.main()
    