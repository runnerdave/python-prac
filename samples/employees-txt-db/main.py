# main.py

from datetime import datetime

Legajo = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009,
          5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019]
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
A_Jub = 0.11
A_O_soc = 0.03
A_Sind = 0.03
A_ley1254 = 0.015

# convierto la lista de sueldo a un diccionario para facilitar la busqueda
sueldo_dict = {sueldo[i]: sueldo[i + 1] for i in range(0, len(sueldo), 2)}

def count_years_from_date(date: str):
    input_date = datetime.strptime(date, "%d/%m/%Y")
    current_date = datetime.now()
    years_difference = current_date.year - input_date.year

    if (current_date.month, current_date.day) < (input_date.month, input_date.day):
        years_difference -= 1
    return years_difference


def list_by_legajo_no(no: int):
    try:
        # obtengo el indice en el legajo
        i = Legajo.index(int(no))
        # print(f"El Legajo {no} tiene el siguiente indice: {index}")
        space = "    "
        header = f"Legajo{space}Apellido{space}Nombre{space}Obra Social{space}Planta{space}Puesto{space}Sueldos B{space}Antigüedad en Años"
        separator = ''.join(["_" for _ in range(100)])
        values = f"{Legajo[i]}{space}{Apellido[i]}{space}{Nombre[i]}{space}{Obra_Social[i]}{space}{Planta[i]}{space}{Puesto[i]}{space}{sueldo_dict[Puesto[i]]}{space}{space}{count_years_from_date(Fecha_Ing[i])}"
        return header + "\n" + separator + "\n" + values
    except ValueError:
        print(f"El legajo {no} no esta en la lista.")


def list_by_planta(name: str):
    pass


def list_by_year(name: str):
    pass


def main():
    print("Base de datos de empleados por legajo\nSeleccione su opcion de búsqueda de la siguientes opciones:")
    print("Consultar por número de Legajo(1)")
    print("Consultar por Planta          (2)")
    print("Consultar por Año             (3)")

    option = input("Seleccione su opción:          ")
    if option == "1":
        legajo_no = input("Ingrese el número de Legajo a consultar: ")
        print(list_by_legajo_no(legajo_no))
    elif option == "2":
        planta = input("Ingrese la Planta a consultar: ")
        print(list_by_planta(planta))


if __name__ == "__main__":
    main()
