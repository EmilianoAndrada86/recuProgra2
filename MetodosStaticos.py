from Classes import *
import re
@staticmethod
def menu():
    print("Ingrese 1 Para dar de alta una boya")
    print("Ingrese 2 Para Modificar una boya")
    print("Ingrese 3 Para dar de Baja una boya")
    print("Ingrese 4 Para dar de alta una tormenta ")
    print("Ingrese 5 Para modificar una tormenta ")
    print("Ingrese 6 Para dar de baja una tormenta ")
    print("Ingrese 7 Para listar las tormentas ")
    print("Ingrese 0 Para Finalizar ")
    try:
        seleccion=int(input("Ingrese su seleccion: "))
        if seleccion<8 and seleccion>=0:
             return seleccion
    except ValueError:
        print("Ingrese un Numero Valido")
@staticmethod
def altaBoya(listaBoya):
    val=False
    while not val:
        id=input("Ingrese Primero el id de la boya recuerde que el formato es B-XXXX donde x es un numero: ")
        val=re.search('B-([0-9]){4}',id)
    val=False
    while not val:
        latitud=input("Ingrese La latitud con el siguiente formato xxx/xx-xx-xx-n/s ejemplo 12-12-12-N: ")
        val=re.search('((1[0-7][0-9])|(180)|[0-9]{2})-[0-9]{2}-[0-9]{2}-(n|s|N|S)',latitud)
    val=False
    while not val:
        longitud=input("Ingrese La longitud con el siguiente formato xx-xx-xx-e/o, ejemplo 12-12-12-E:  ")
        val=re.search('[0-9]{2}-[0-9]{2}-[0-9]{2}-(e|o|E|O)',longitud)
    mar=input("Ingrese el mar de la boya: ")
    oceano=input("Ingrese el oceano de la boya: ")
    if latitud[9]=="N" or latitud[9]=="n":
        hemisferio="Norte"
    else:
        hemisferio="Sur"
    nuevaBoya=Boya(id,latitud,longitud,hemisferio,mar,oceano)
    listaBoya.append(nuevaBoya)
@staticmethod
def modBoya(listaBoya):
    print("Seleccione la boya que desea Modificar")
    i=1
    for boya in listaBoya:
        print(str(i)+"-"+"id:"+boya.id+" ubicacion: "+str(boya.ubicacion)+" Mar: "+boya.mar+" Oceano: "+boya.oceano)
        i+=1
    try:
        seleccion=int(input("Seleccione el numero de boya a modificar: "))
        if seleccion<=len(listaBoya):
            val=False
            while not val:
                latitud=input("Ingrese La latitud con el siguiente formato xxx/xx-xx-xx-n/s ejemplo 12-12-12-N: ")
                val=re.search('((1[0-7][0-9])|(180)|[0-9]{2})-[0-9]{2}-[0-9]{2}-(n|s|N|S)',latitud)
            val=False
            while not val:
                longitud=input("Ingrese La longitud con el siguiente formato xx-xx-xx-e/o, ejemplo 12-12-12-E:  ")
                val=re.search('[0-9]{2}-[0-9]{2}-[0-9]{2}-(e|o|E|O)',longitud)
            mar=input("Ingrese el mar de la boya: ")
            oceano=input("Ingrese el oceano de la boya: ")
            if latitud[9]=="N" or latitud[9]=="n":
                hemisferio="Norte"
            else:
                hemisferio="Sur"
            listaBoya[seleccion-1].ubicacion['latitud']=latitud
            listaBoya[seleccion-1].ubicacion['longitud']=longitud
            listaBoya[seleccion-1].mar=mar
            listaBoya[seleccion-1].oceano=oceano
        else:
            print("Error seleccione una sonda valida")

        
    except ValueError:
        print("Error Numero no valido")   
@staticmethod
def bajaaBoya(listaBoya):
    print("Seleccione la boya que desea Modificar")
    i=1
    for boya in listaBoya:
        print(str(i)+"-"+"id:"+boya.id+" ubicacion: "+str(boya.ubicacion)+" Mar: "+boya.mar+" Oceano: "+boya.oceano)
        i+=1
    try:
        seleccion=int(input("Indique El numero de la boya que desea eliminar: "))
        if(seleccion<=len(listaBoya)):
            boyaremovida=listaBoya.pop(seleccion-1)
            print("Boya: "+boyaremovida.id+" Ah sido eliminada con exito")
        else:
            print("Ingrese el numero de una Boya Valida")
    except ValueError:
        print("Ingrese un numero valido")
@staticmethod
def altaTormenta(listaBoya,listaTormentas):
    print("Seleccione la boya que va a Sensar la temperatura del agua")
    i=1
    for boya in listaBoya:
        print(str(i)+"-"+"id:"+boya.id+" ubicacion: "+str(boya.ubicacion)+" Mar: "+boya.mar+" Oceano: "+boya.oceano)
    try:
        seleccion=int(input("Ingrese el Numero de la boya: "))
        if seleccion<=len(listaBoya):
            temp=listaBoya[seleccion-1].sensarTemperatura()
            if temp<26.51:
                nuevaTormenta=Tormenta(temp,listaBoya[seleccion-1])
                listaTormentas.append(nuevaTormenta)
                print("Tormenta Tropical Sensada temperatura del agua: "+str(temp))
            else:
                print("La tormenta es un Huracan")
                try:
                    velViento=int(input("Ingrese la velocidad el viento: "))
                    cantVict=int(input("Ingrese la cantidad de victimas: "))
                    costoDaño=int(input("Ingrese el Costo de daños en dolares: "))
                    ciudadesAfect=[]
                    aux=10
                    while aux!=0:
                        ciudad=input("Agregue Una ciudad. Indique 0 para finalizar la ciudad")
                        if(ciudad=="0"):
                            aux=0
                        else:
                            ciudadesAfect.append(ciudad)
                    nuevaTormenta=Huracan(temp,listaBoya[seleccion-1],velViento,cantVict,costoDaño,ciudadesAfect)
                    listaTormentas.append(nuevaTormenta)
                    print(str(nuevaTormenta.categoria))
                except ValueError:
                    print("Ingrese un Numero valido")    
        else:
            print("Error ingrese una boya valida")
    except ValueError:
        print("Ingrese un Numero")
@staticmethod
def modTormenta(listaTormentas):
    print("Seleecione la tormenta que desea modificar: ")
    i=1
    for c in listaTormentas:
            print(str(i)+"-"+str(c))
            i+=1
    try:
        
        seleccion=int(input("Ingrese la tormenta que desea modificar: "))
        if seleccion<=len(listaTormentas):
            tormentaAModificar=listaTormentas[seleccion-1]
            if isinstance(tormentaAModificar,Huracan):
                velViento=int(input("Velocidad del Viento Actual: "+str(tormentaAModificar.velViento)+", Ingrese la nueva velocidad o 0 para no modificar: "))
                if(velViento!=0):
                    tormentaAModificar.velViento=velViento
                cantVictFatales=int(input("Cantidad de Victimas: "+str(tormentaAModificar.cantVictFatales)+"Ingrese una nueva cantidad de victimas o 0 para no modificar: "))
                if(cantVictFatales!=0):
                    tormentaAModificar.cantVictFatales=cantVictFatales
                costoDaño=int(input("Costo Daño en Dolares: "+str(tormentaAModificar.costoDaño)+", Ingrese el nuevo costo de daños o 0 para no modificar: "))
                if costoDaño!=0:
                    tormentaAModificar.costoDaño=costoDaño
                i=1
                for c in tormentaAModificar.ciudadesAfectadas:
                    ciudad=input("Ciudad "+str(i)+" Nombre: "+c+"\n"+"Ingrese el nuevo nombre o 0 para no modificar: ")
                    if(ciudad!="0"):
                        tormentaAModificar.ciudadesAfectadas[i-1]=ciudad
                listaTormentas[seleccion-1]=tormentaAModificar
            else:
                print("Las tormentas tropicales no son modificables.")
        else:
            print("Error Selecione un tormenta valida")       

    except ValueError:
        print("Ingrese un numero valido")
@staticmethod
def bajaTormenta(listaTormentas):
    i=1
    for tormenta in listaTormentas:
        print(str(i)+"-"+str(tormenta))
        i+=1
    try:
        seleccion=int(input("Ingrese el numero de la tormenta que desea eliminar: "))
        if(seleccion<=len(listaTormentas)):
            listaTormentas.pop(seleccion-1)
        else:
            print("Ingrese un valor de tormenta valido")
    except ValueError:
        print("Ingrese un numero Valido")
@staticmethod
def listarTormentas(listaTormentas):
    listaHuracanes=[]
    listaTorTropical=[]
    for tormenta in listaTormentas:
        if isinstance(tormenta,Huracan):
            listaHuracanes.append(tormenta)
        else:
            listaTorTropical.append(tormenta)
    listaHuracanes.sort(key=lambda x: x.categoria, reverse=True)
    listaHuracanes.extend(listaTorTropical)
    for tormen in listaHuracanes:
        print(tormen)