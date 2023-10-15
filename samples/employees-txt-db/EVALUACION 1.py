Legajo=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019]
Apellido=["HALLE SAIN","GHAMEN AHMED","García","VELAZQUEZ","PEREIRA","CATCOF","RAMIREZ SUAREZ","HEREDIA","Rocatagliata","MANGANELLI","RODRIGUEZ","FERNANDEZ","RIVERO","MODARELLI","CUADRADO","GUZMAN","VIEGAS","DOMINUTTI","MRENDE"]
Nombre=["Martín","Liliana Cruz","Israel","María Marta","Miguel Angel","Roberto","Azucena","Carlos Manuel","Manuel","ANGEL LUIS","SINIA","MARIA ESTHER","DIGNA","JORGE JOSE","HAYDEE ELENA","MARIO GUSTAVO","MARIO","LUIS","ELFO"]
Fecha_Ing=["29/8/1981","20/8/2009","16/4/1999","12/11/1991","10/4/1999","5/8/1991","27/11/1990","16/7/1993","17/8/2004","2/6/1992","17/7/1990","27/8/1981","2/9/1981","25/4/1991","19/9/1990","30/8/1981","26/8/1991","23/8/2010","9/3/1992"]
Obra_Social=["Ossos","Ossos","Cefran","Ospla","Ossos","Osecac","Osecac","Ospla","Cefran","Cefran","Osecac","Cefran","Ospla","Osecac","Cefran","Osecac","Cefran","Osecac","Ossos"]
Planta=["Bernal","San Martin","Pilar","Moron","Bernal","Pilar","Moron","Campana","San Martin","Moron","Pilar","San Martin","San Martin","Moron","Moron","Campana","Capital Federal","Pilar","Capital Federal"]
Puesto=["Administrativo","Ventas","Ventas","Recursos","Ventas","Cadete","Administrativo","Cadete","Ingeniería","Administrativo","Administrativo","Diseño","Diseño","Ventas","Recursos","Ventas","Administrativo","Administrativo","Jefe de Sector"]
sueldo=["Cadete",275000,"Ventas",248000,"Administrativo",301000,"Diseño",364000,"Jefe de Sector",443000,"Recursos",287000,"Ingeniería",400000]
A_Jub=0.11
A_O_soc=0.03
A_Sind = 0.03
A_ley1254= 0.015
from datetime import datetime
hoy=datetime.now()
añoactual= hoy.year
#print(añoactual)
suel=0
#print(len(Fecha_Ing))
consulegajo=int(input("Ingrese el Numero de Legajo A Consultar : ".rjust(110)))
print("")
print("Legajo".center(7),"Apellido".center(10),"Nombre".center(20),"Obra Social".center(15),"Planta".center(15),"Puesto".center(15),"Sueldos B".center(18),"Antiguedad en Años".rjust(23))
print("-----------------------------------------------------------------------------------------------------------------------------------")
for z in range (19):
   if Legajo[z]==consulegajo:
      for y in range (14) :
            if Puesto[z]==sueldo[y]:
                suel=sueldo[y+1]
                #for x in range (19):
                fecha_dt=datetime.strptime(Fecha_Ing[z],"%d/%m/%Y") 
                años=fecha_dt.year
                añostot=añoactual-años
                if Legajo[z]==consulegajo:
                    print(str(Legajo[z]).center(7),Apellido[z].center(10),Nombre[z].center(20),Obra_Social[z].center(15),Planta[z].center(15), Puesto[z].center(15),str(suel).center(18),str(añostot).center(20))
print("")                     
print("")    
consulplanta=input("Ingrese La Planta A Consultar : ".rjust(110))
print("")
print("Legajo".center(8),"Apellido".center(13),"Nombre".center(19),"Obra Social".center(12),"Planta".center(14),"Puesto".center(16),"Sueldos B".center(16),"Jubilacion".center(9), "Odra Social".center(16),"Ley".center(10),"Sueldo Neto".center(15))
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
for z in range (19):
    if Planta[z]==consulplanta: 
       for y in range (14) :
           if Puesto[z]==sueldo[y]:
            suel=sueldo[y+1] 
            jubilacion=suel*A_Jub
            osocial=suel*A_O_soc
            ley=suel*A_ley1254
            sueneto=suel-jubilacion-osocial-ley
            print(str(Legajo[z]).center(10),Apellido[z].ljust(16),Nombre[z].ljust(16),Obra_Social[z].ljust(12),Planta[z].ljust(16), Puesto[z].ljust(14),str(suel).center(13),str(jubilacion).center(13),str(osocial).center(13),str(ley).center(12),str(sueneto).center(12))
print("")
print("")
consultaaño=int(input(" Que Año desea Consultar : ".rjust(110)))
print(" ")
print("Legajo".center(8),"Apellido".center(13),"Nombre".center(18),"Obra Social".center(17),"Planta".center(15),"Puesto".center(20),"Fecha de Ingreso".center(18))
for x in range (19):
    fecha_dt=datetime.strptime(Fecha_Ing[x],"%d/%m/%Y")
    año=fecha_dt.year
    if año==consultaaño:
      print(str(Legajo[x]).center(10),Apellido[x].ljust(16),Nombre[x].ljust(16),Obra_Social[x].ljust(19),Planta[x].ljust(16), Puesto[x].ljust(16),Fecha_Ing[x].center(12))