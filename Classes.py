import random
class Boya:
    def __init__(self,id,latitud,longitud,hemisferio,mar,oceano):
        self.id=id
        self.ubicacion={
            "latitud":latitud,
            "longitud":longitud
        }
            
        self.hemisferio=hemisferio
        self.mar=mar
        self.oceano=oceano

    def sensarTemperatura(self):
        temp=round(random.uniform(20,40),2)
        return temp

class Tormenta:
    def __init__(self,temperaturaAgua,boya):
        self.temperaturaAgua=temperaturaAgua
        self.boya=boya
    def __str__(self):
        aux="Tormenta Tropical-Temperatura del Agua: "+str(self.temperaturaAgua)+"- Sondeado por: "+self.boya.id
        return aux

class Huracan(Tormenta):
    def __init__(self,temperaturaAgua,boya,velViento,cantVictFatales,costoDaño,ciudadesAfectadas):
        super().__init__(temperaturaAgua,boya)
        self.velViento=velViento
        self.cantVictFatales=cantVictFatales
        self.costoDaño=costoDaño
        self.ciudadesAfectadas=ciudadesAfectadas
        self.categoria=0
        self.__definirCategoria(velViento)

    def __definirCategoria(self,vViento):
        if vViento>119 and vViento<=153:
            self.categoria=1
        elif vViento>153 and vViento<=177:
            self.categoria=2
        elif vViento>177 and vViento<=209:
            self.categoria=3
        elif vViento>209 and vViento<=249:
            self.categoria=4
        else:
            self.categoria=5
    def __str__(self):
        aux="Huracan-Categoria: "+str(self.categoria)+"\n"+"-Velocidad del Viento: "+str(self.velViento)+"-Cantidad de Victimas Fatales: "+str(self.cantVictFatales)+"-Costo de Daños: "+str(self.costoDaño)+" Dolares"+"\n"+"-Ciudades Afectadas: "
        for  c in self.ciudadesAfectadas:
            aux+=c+"/"
        return aux