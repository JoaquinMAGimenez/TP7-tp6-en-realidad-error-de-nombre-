#ejercicio15.py



#15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
#y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#uno en las naturales) y tipo (natural o arquitectónica);
#b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
#la distancia que las separa;
#c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;
#f. deberá utilizar un grafo no dirigido.

from grafo import Grafo

g=Grafo()

#A
g.insertar_vertice(
    'La Gran Muralla'
)
g.insertar_vertice(
    'Taj Mahal' 
)
g.insertar_vertice(
    'La Ciudad de Petra'
)
g.insertar_vertice(
    'El Coliseo Romano'
)
g.insertar_vertice(
    'El Machu Pichu'
)
g.insertar_vertice(
    'La Piramide de Chichen Itza'
)
g.insertar_vertice(
    'La estatua del Cristo Redentor'
)
g.insertar_vertice(
    'Parque Nacional del río subterráneo de Puerto Princea'
)
g.insertar_vertice(
    'Isla Jeju',
)
g.insertar_vertice(
    'Cataratas del Iguazu'
)
g.insertar_vertice(
    'Montania de la Mesa'
)
g.insertar_vertice(
    'Bahia de Ha_Long'
)
g.insertar_vertice(
    'Amazonas'
)
g.insertar_vertice(
    'Parque Nacional de Komodo'
)

#B

#relaciones entre las maravillas naturales

g.insertar_arista('Amazonas','Bahia de Ha_Long', 17750 )
g.insertar_arista('Amazonas','Cataratas del Iguazu',2760 )
g.insertar_arista('Amazonas','Isla Jeju',16423 )
g.insertar_arista('Amazonas','Montania de la Mesa',9809 )
g.insertar_arista('Amazonas','Parque Nacional del río subterráneo de Puerto Princea',19235 )
g.insertar_arista('Amazonas', 'Parque Nacional de Komodo',18575 )

g.insertar_arista('Bahia de Ha_Long','Amazonas',17750 )
g.insertar_arista('Bahia de Ha_Long','Cataratas del Iguazu',18055 )
g.insertar_arista('Bahia de Ha_Long','Isla Jeju',2359 )
g.insertar_arista('Bahia de Ha_Long','Montania de la Mesa',10482 )
g.insertar_arista('Bahia de Ha_Long','Parque Nacional del río subterráneo de Puerto Princea',1730 )
g.insertar_arista('Bahia de Ha_Long', 'Parque Nacional de Komodo',3536 )

g.insertar_arista('Cataratas del Iguazu','Amazonas',2760 )
g.insertar_arista('Cataratas del Iguazu','Bahia de Ha_Long',18055 )
g.insertar_arista('Cataratas del Iguazu','Isla Jeju',19132 )
g.insertar_arista('Cataratas del Iguazu','Montania de la Mesa',7606 )
g.insertar_arista('Cataratas del Iguazu','Parque Nacional del río subterráneo de Puerto Princea',18143 )
g.insertar_arista('Cataratas del Iguazu', 'Parque Nacional de Komodo', 4728)

g.insertar_arista('Isla Jeju','Amazonas',16423 )
g.insertar_arista('Isla Jeju','Bahia de Ha_Long',2359 )
g.insertar_arista('Isla Jeju','Cataratas del Iguazu',19132 )
g.insertar_arista('Isla Jeju','Montania de la Mesa',12802 )
g.insertar_arista('Isla Jeju','Parque Nacional del río subterráneo de Puerto Princea', 2702)
g.insertar_arista('Isla Jeju', 'Parque Nacional de Komodo',4728 )

g.insertar_arista('Montania de la Mesa','Amazonas',9809 )
g.insertar_arista('Montania de la Mesa','Bahia de Ha_Long',10482 )
g.insertar_arista('Montania de la Mesa','Cataratas del Iguazu',7606 )
g.insertar_arista('Montania de la Mesa','Isla Jeju',12802 )
g.insertar_arista('Montania de la Mesa','Parque Nacional del río subterráneo de Puerto Princea',11470 )
g.insertar_arista('Montania de la Mesa', 'Parque Nacional de Komodo',10073 )

g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea','Amazonas',19235 )
g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea','Bahia de Ha_Long',1730 )
g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea','Cataratas del Iguazu',18143 )
g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea','Isla Jeju',2702 )
g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea','Montania de la Mesa',11470 )
g.insertar_arista('Parque Nacional del río subterráneo de Puerto Princea', 'Parque Nacional de Komodo',2416 )

g.insertar_arista('Parque Nacional de Komodo','Amazonas',3536 )
g.insertar_arista('Parque Nacional de Komodo','Bahia de Ha_Long',3536 )
g.insertar_arista('Parque Nacional de Komodo','Cataratas del Iguazu',4728 )
g.insertar_arista('Parque Nacional de Komodo','Isla Jeju',4728 )
g.insertar_arista('Parque Nacional de Komodo','Montania de la Mesa',10073 )
g.insertar_arista('Parque Nacional de Komodo','Parque Nacional del río subterráneo de Puerto Princea',2416 )

#relaciones entre las maravillas arrquitectonicas

g.insertar_arista('La Gran Muralla','La estatua del Cristo Redentor',17538 )
g.insertar_arista('La Gran Muralla','La Piramide de Chichen Itza',12659 )
g.insertar_arista('La Gran Muralla','El Machu Pichu',16366 )
g.insertar_arista('La Gran Muralla','El Coliseo Romano',8337 )
g.insertar_arista('La Gran Muralla','La Ciudad de Petra',7594 )
g.insertar_arista('La Gran Muralla','Taj Mahal',4078 )

g.insertar_arista('La estatua del Cristo Redentor','La Gran Muralla',17538 )
g.insertar_arista('La estatua del Cristo Redentor','La Piramide de Chichen Itza',6906 )
g.insertar_arista('La estatua del Cristo Redentor','El Machu Pichu',3780 )
g.insertar_arista('La estatua del Cristo Redentor','El Coliseo Romano',9203 )
g.insertar_arista('La estatua del Cristo Redentor','La Ciudad de Petra',10268 )
g.insertar_arista('La estatua del Cristo Redentor','Taj Mahal',14132 )

g.insertar_arista('La Piramide de Chichen Itza','La Gran Muralla',12659 )
g.insertar_arista('La Piramide de Chichen Itza','La estatua del Cristo Redentor',6906 )
g.insertar_arista('La Piramide de Chichen Itza','El Machu Pichu',4149 )
g.insertar_arista('La Piramide de Chichen Itza','El Coliseo Romano',9356 )
g.insertar_arista('La Piramide de Chichen Itza','La Ciudad de Petra',11775 )
g.insertar_arista('La Piramide de Chichen Itza','Taj Mahal',14503 )

g.insertar_arista('El Machu Pichu','La Gran Muralla',16366 )
g.insertar_arista('El Machu Pichu','La estatua del Cristo Redentor',3780 )
g.insertar_arista('El Machu Pichu','La Piramide de Chichen Itza',4149 )
g.insertar_arista('El Machu Pichu','El Coliseo Romano',10866 )
g.insertar_arista('El Machu Pichu','La Ciudad de Petra',12837 )
g.insertar_arista('El Machu Pichu','Taj Mahal',16972 )

g.insertar_arista('El Coliseo Romano','La Gran Muralla',8337 )
g.insertar_arista('El Coliseo Romano','La estatua del Cristo Redentor',9203 )
g.insertar_arista('El Coliseo Romano','La Piramide de Chichen Itza',9356 )
g.insertar_arista('El Coliseo Romano','El Machu Pichu',10866 )
g.insertar_arista('El Coliseo Romano','La Ciudad de Petra',2420 )
g.insertar_arista('El Coliseo Romano','Taj Mahal',6072 )

g.insertar_arista('La Ciudad de Petra','La Gran Muralla',7594 )
g.insertar_arista('La Ciudad de Petra','La estatua del Cristo Redentor',10268 )
g.insertar_arista('La Ciudad de Petra','La Piramide de Chichen Itza',11775 )
g.insertar_arista('La Ciudad de Petra','El Coliseo Romano',2420 )
g.insertar_arista('La Ciudad de Petra','El Machu Pichu',12837 )
g.insertar_arista('La Ciudad de Petra','Taj Mahal',4140 )

g.insertar_arista('Taj Mahal','La Gran Muralla',4078 )
g.insertar_arista('Taj Mahal','La estatua del Cristo Redentor', 14132)
g.insertar_arista('Taj Mahal','La Piramide de Chichen Itza',14503 )
g.insertar_arista('Taj Mahal','El Coliseo Romano',6072 )
g.insertar_arista('Taj Mahal','El Machu Pichu',16972 )
g.insertar_arista('Taj Mahal','La Ciudad de Petra',4140 )

g.barrido_vertice()
print()


#c
arbol_min = g.kruskal()
arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    print(nodo)
    nodo = nodo.split(';')

    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el peso total es {peso_total}")


#D

paises = g.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])


#E    
