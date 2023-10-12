from datetime import datetime
import pandas as pd
from tabulate import tabulate

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
A_Jub = 0.11
A_O_soc = 0.03
A_Sind = 0.03
A_ley1254 = 0.015

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


def get_row_by_legajo(legajo):
    """
    Get the row of the DataFrame based on the Legajo.

    Parameters:
    - legajo: int, the Legajo to search for.

    Returns:
    - pandas.Series or None: The row of the DataFrame if found, otherwise None.
    """
    row = df[df['Legajo'] == legajo]
    if not row.empty:
        return row.iloc[0]  # Return the first row (there should be only one)
    else:
        return None
    
def get_row_by_planta(planta):
    """
    Get the row of the DataFrame based on the Planta.

    Parameters:
    - planta: int, the Planta to search for.

    Returns:
    - pandas.Series or None: The row of the DataFrame if found, otherwise None.
    """
    result_df = df[df['Planta'] == planta]
    if not result_df.empty:
        return result_df
    else:
        return None
    
def get_row_by_year(year):
    """
    Get the row of the DataFrame based on the Fecha_Ing.

    Parameters:
    - year: int, the Fecha_Ing to search for.

    Returns:
    - pandas.Series or None: The row of the DataFrame if found, otherwise None.
    """
    # Extract the year from 'Fecha_Ing' column
    df['Year'] = pd.to_datetime(df['Fecha_Ing'], format='%d/%m/%Y').dt.year

    # Filter by the specified year
    result_df = df[df['Year'] == year].copy()

    # Drop the temporary 'Year' column
    result_df.drop(columns=['Year'], inplace=True)

    if not result_df.empty:
        return result_df
    else:
        return None
    
def modify_fecha_ing(df):
    """
    Modify the 'Fecha_Ing' column to represent the age in years relative to the current date.

    Parameters:
    - df: pandas.DataFrame, the DataFrame to modify.

    Returns:
    - pandas.DataFrame: The modified DataFrame.
    """
    # Convert 'Fecha_Ing' to datetime
    df['Fecha_Ing'] = pd.to_datetime(df['Fecha_Ing'], format='%d/%m/%Y')

    # Calculate age in years relative to the current date
    current_date = datetime.now()
    df['Antigüedad en Años'] = (current_date - df['Fecha_Ing']).dt.days // 365  # Approximate age in years

    return df
    
print("legajo 5003")
result_row = get_row_by_legajo(5003)
result_df = pd.DataFrame(result_row).transpose()
modify_fecha_ing(result_df)
result_df.drop(columns=['Fecha_Ing'], inplace=True)
print(tabulate(result_df, headers='keys', tablefmt='pretty', showindex=False))

print("planta Pilar")
result_df = get_row_by_planta("Pilar")
with pd.option_context('mode.chained_assignment', None):
    result_df['jubilacion'] = result_df['sueldo']*A_Jub
    result_df['obra social'] = result_df['sueldo']*A_O_soc
    result_df['Ley'] = result_df['sueldo']*A_ley1254
    result_df['Sueldo neto'] = result_df['sueldo']-result_df['jubilacion']-result_df['obra social']-result_df['Ley']
print(tabulate(result_df, headers='keys', tablefmt='pretty', showindex=False))

print("año 1990")
result_df = get_row_by_year(1990)
print(tabulate(result_df, headers='keys', tablefmt='pretty', showindex=False))

