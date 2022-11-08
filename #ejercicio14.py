#ejercicio14.py

#14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
#tareas:
#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
#es la distancia entre los ambientes, se debe cargar en metros;
#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;
#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el
#Smart Tv.

from grafo import Grafo
g=Grafo()
#A
g.insertar_vertice('cocina')
g.insertar_vertice('comedor')
g.insertar_vertice('cochera')
g.insertar_vertice('quincho')
g.insertar_vertice('banio 1')
g.insertar_vertice('banio 2')
g.insertar_vertice('habitacion 1')
g.insertar_vertice('habitacion 2')
g.insertar_vertice('sala de estar')
g.insertar_vertice('terraza')
g.insertar_vertice('patio')
#B
g.insertar_arista('cocina', 'comedor', 6)
g.insertar_arista('cocina', 'cochera', 5)
g.insertar_arista('cocina', 'quincho', 7)
g.insertar_arista('cocina', 'banio 1', 1)
g.insertar_arista('cocina', 'banio 2', 9)
g.insertar_arista('cocina', 'habitacion 1', 8)
g.insertar_arista('cocina', 'habitacion 2', 10)
g.insertar_arista('cocina', 'sala de estar', 4)
g.insertar_arista('cocina', 'terraza', 3)
g.insertar_arista('cocina', 'patio', 2)

g.insertar_arista('comedor', 'cocina', 6)
g.insertar_arista('comedor', 'cochera', 5)
g.insertar_arista('comedor', 'quincho', 7)
g.insertar_arista('comedor', 'banio 1', 4)
g.insertar_arista('comedor', 'banio 2', 8)
g.insertar_arista('comedor', 'habitacion 1', 9)
g.insertar_arista('comedor', 'habitacion 2', 1)
g.insertar_arista('comedor', 'sala de estar', 10)
g.insertar_arista('comedor', 'terraza', 2)
g.insertar_arista('comedor', 'patio', 3)

g.insertar_arista('cochera', 'cocina', 6)
g.insertar_arista('cochera', 'comedor', 5)
g.insertar_arista('cochera', 'quincho', 7)
g.insertar_arista('cochera', 'banio 1', 4)
g.insertar_arista('cochera', 'banio 2', 8)
g.insertar_arista('cochera', 'habitacion 1', 9)
g.insertar_arista('cochera', 'habitacion 2', 1)
g.insertar_arista('cochera', 'sala de estar', 10)
g.insertar_arista('cochera', 'terraza', 2)
g.insertar_arista('cochera', 'patio', 3)

g.insertar_arista('quincho', 'comedor', 7)
g.insertar_arista('quincho', 'cochera', 7)
g.insertar_arista('quincho', 'cocina', 7)
g.insertar_arista('quincho', 'banio 1', 4)
g.insertar_arista('quincho', 'banio 2', 8)
g.insertar_arista('quincho', 'habitacion 1', 9)
g.insertar_arista('quincho', 'habitacion 2', 1)
g.insertar_arista('quincho', 'sala de estar', 10)
g.insertar_arista('quincho', 'terraza', 2)
g.insertar_arista('quincho', 'patio', 3)


g.insertar_arista('banio 1', 'comedor', 4)
g.insertar_arista('banio 1', 'cochera', 5)
g.insertar_arista('banio 1', 'quincho', 7)
g.insertar_arista('banio 1', 'cocina', 1)
g.insertar_arista('banio 1', 'banio 2', 9)
g.insertar_arista('banio 1', 'habitacion 1', 8)
g.insertar_arista('banio 1', 'habitacion 2', 10)
g.insertar_arista('banio 1', 'sala de estar', 4)
g.insertar_arista('banio 1', 'terraza', 3)
g.insertar_arista('banio 1', 'patio', 2)

g.insertar_arista('banio 2', 'comedor', 8)
g.insertar_arista('banio 2', 'cochera', 5)
g.insertar_arista('banio 2', 'quincho', 8)
g.insertar_arista('banio 2', 'banio 1', 9)
g.insertar_arista('banio 2', 'cocina', 9)
g.insertar_arista('banio 2', 'habitacion 1', 8)
g.insertar_arista('banio 2', 'habitacion 2', 10)
g.insertar_arista('banio 2', 'sala de estar', 4)
g.insertar_arista('banio 2', 'terraza', 3)
g.insertar_arista('banio 2', 'patio', 2)

g.insertar_arista('habitacion 1', 'comedor', 9)
g.insertar_arista('habitacion 1', 'cochera', 5)
g.insertar_arista('habitacion 1', 'quincho', 9)
g.insertar_arista('habitacion 1', 'banio 1', 8)
g.insertar_arista('habitacion 1', 'banio 2', 8)
g.insertar_arista('habitacion 1', 'cocina', 8)
g.insertar_arista('habitacion 1', 'habitacion 2', 10)
g.insertar_arista('habitacion 1', 'sala de estar', 4)
g.insertar_arista('habitacion 1', 'terraza', 3)
g.insertar_arista('habitacion 1', 'patio', 2)

g.insertar_arista('habitacion 2', 'comedor', 1)
g.insertar_arista('habitacion 2', 'cochera', 5)
g.insertar_arista('habitacion 2', 'quincho', 1)
g.insertar_arista('habitacion 2', 'banio 1', 10)
g.insertar_arista('habitacion 2', 'banio 2', 9)
g.insertar_arista('habitacion 2', 'habitacion 1', 10)
g.insertar_arista('habitacion 2', 'cocina', 10)
g.insertar_arista('habitacion 2', 'sala de estar', 4)
g.insertar_arista('habitacion 2', 'terraza', 3)
g.insertar_arista('habitacion 2', 'patio', 2)

g.insertar_arista('sala de estar', 'comedor', 10)
g.insertar_arista('sala de estar', 'cochera', 5)
g.insertar_arista('sala de estar', 'quincho', 10)
g.insertar_arista('sala de estar', 'banio 1', 4)
g.insertar_arista('sala de estar', 'banio 2', 4)
g.insertar_arista('sala de estar', 'habitacion 1', 4)
g.insertar_arista('sala de estar', 'habitacion 2', 4)
g.insertar_arista('sala de estar', 'cocina', 4)
g.insertar_arista('sala de estar', 'terraza', 3)
g.insertar_arista('sala de estar', 'patio', 2)

g.insertar_arista('terraza', 'comedor', 2)
g.insertar_arista('terraza', 'cochera', 5)
g.insertar_arista('terraza', 'quincho', 2)
g.insertar_arista('terraza', 'banio 1', 3)
g.insertar_arista('terraza', 'banio 2', 3)
g.insertar_arista('terraza', 'habitacion 1', 3)
g.insertar_arista('terraza', 'habitacion 2', 3)
g.insertar_arista('terraza', 'sala de estar', 3)
g.insertar_arista('terraza', 'cocina', 3)
g.insertar_arista('terraza', 'patio', 2)

g.insertar_arista('patio', 'comedor', 3)
g.insertar_arista('patio', 'cochera', 5)
g.insertar_arista('patio', 'quincho', 3)
g.insertar_arista('patio', 'banio 1', 2)
g.insertar_arista('patio', 'banio 2', 2)
g.insertar_arista('patio', 'habitacion 1', 2)
g.insertar_arista('patio', 'habitacion 2', 2)
g.insertar_arista('patio', 'sala de estar', 2)
g.insertar_arista('patio', 'terraza', 2)
g.insertar_arista('patio', 'cocina', 2)

g.barrido_vertice()
print()
#C
arbol_min = g.kruskal()
arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    print(nodo)
    nodo = nodo.split(';')

    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el total de cable es {peso_total}")
print(arbol_min)

#D
if(g.existe_paso("habitacion 1", "sala de estar")):
    aux = g.dijkstra("habitacion 1")
    camino = g.camino(aux, "habitacion 1", "sala de estar")
    print("El camino más corto entre la habitación 1 y la sala de estar es:", camino['camino'])

    print("La cantidad minima de cable necesaria para conectar el router con el smart tv es de", camino['costo'], "metros")

else:
    print("No existe paso desde habitacion 1 hasta saka de estar")
