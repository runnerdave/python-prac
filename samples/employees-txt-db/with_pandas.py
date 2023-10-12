import pandas as pd

# Provided lists
Legajo = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019]
Apellido = ["HALLE SAIN", "GHAMEN AHMED", "García", "VELAZQUEZ", "PEREIRA", "CATCOF", "RAMIREZ SUAREZ", "HEREDIA", "Rocatagliata",
            "MANGANELLI", "RODRIGUEZ", "FERNANDEZ", "RIVERO", "MODARELLI", "CUADRADO", "GUZMAN", "VIEGAS", "DOMINUTTI", "MRENDE"]
Nombre = ["Martín", "Liliana Cruz", "Israel", "María Marta", "Miguel Angel", "Roberto", "Azucena", "Carlos Manuel", "Manuel",
          "ANGEL LUIS", "SINIA", "MARIA ESTHER", "DIGNA", "JORGE JOSE", "HAYDEE ELENA", "MARIO GUSTAVO", "MARIO", "LUIS", "ELFO"]
Fecha_Ing = ["29/8/1981", "20/8/2009", "16/4/1999", "12/11/1991", "10/4/1999", "5/8/1991", "27/11/1990", "16/7/1993", "17/8/2004",
             "2/6/1992", "17/7/1990", "27/8/1981", "2/9/1981", "25/4/1991", "19/9/1990", "30/8/1981", "26/8/1991", "23/8/2010", "9/3/1992"]
Obra_Social = ["Ossos", "Ossos", "Cefran", "Ospla", "Ossos", "Osecac", "Osecac", "Ospla", "Cefran",
               "Cefran", "Osecac", "Cefran", "Ospla", "Osecac", "Cefran", "Osecac", "Cefran", "Osecac", "Ossos"]
Planta = ["Bernal", "San Martin", "Pilar", "Moron", "Bernal", "Pilar", "Moron", "Campana", "San Martin", "Moron",
          "Pilar", "San Martin", "San Martin", "Moron", "Moron", "Campana", "Capital Federal", "Pilar", "Capital Federal"]
Puesto = ["Administrativo", "Ventas", "Ventas", "Recursos", "Ventas", "Cadete", "Administrativo", "Cadete", "Ingeniería", "Administrativo",
          "Administrativo", "Diseño", "Diseño", "Ventas", "Recursos", "Ventas", "Administrativo", "Administrativo", "Jefe de Sector"]
sueldo = ["Cadete", 275000, "Ventas", 248000, "Administrativo", 301000,
          "Diseño", 364000, "Jefe de Sector", 443000, "Recursos", 287000, "Ingeniería", 300000]

sueldo_dict = {sueldo[i]: sueldo[i + 1] for i in range(0, len(sueldo), 2)}

def asignar_sueldo(puestos):
    return [sueldo_dict[s] for s in puestos]

# print(asignar_sueldo(Puesto))
# Create a dictionary with the lists
data = {
    'Legajo': Legajo,
    'Apellido': Apellido,
    'Nombre': Nombre,
    'Fecha_Ing': Fecha_Ing,
    'Obra_Social': Obra_Social,
    'Planta': Planta,
    'Puesto': Puesto,
    'sueldo': asignar_sueldo(Puesto)
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)