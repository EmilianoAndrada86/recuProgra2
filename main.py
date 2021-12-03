from Classes import *
from MetodosStaticos import *
listaBoyas=[Boya("B-1234","12-12-12-N","13-13-13-O","Norte","Adriatico","Pacifico"),Boya("B-5625","70-55-31-S","88-33-25-E","Sur","Caribe","Atlantico")]
listaTormentas=[Huracan(36.00,listaBoyas[0],200,1000,600000,["Buenos Aires","Cordoba"]),Tormenta(24.00,listaBoyas[1])]
print(listaTormentas[0])
seleccion=10
while seleccion!=0:
    seleccion=menu()
    if seleccion==1:
        altaBoya(listaBoyas)
    elif seleccion==2:
        modBoya(listaBoyas)
    elif seleccion==3:
        bajaaBoya(listaBoyas)
    elif  seleccion==4:
        altaTormenta(listaBoyas,listaTormentas)
    elif seleccion==5:
        modTormenta(listaTormentas)
    elif seleccion==6:
        bajaTormenta(listaTormentas)
    elif seleccion==7:
        listarTormentas(listaTormentas)
    elif seleccion==0:
        print("Gracias por Utilizar el programa")
    else:
        print("Ingrese un valor entre 1-7 o el 0 para finalizar")