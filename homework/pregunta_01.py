"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'.
    - Misma estructura que el archivo original.
    - Columnas en minúsculas con guiones bajos.
    - Palabras clave separadas por coma + un espacio.
    """

    # Leer archivo completo (líneas crudas)
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    data = []
    current_cluster = None
    current_cantidad = None
    current_porcentaje = None
    palabras = []

    # Expresión regular para filas principales
    regex = r"^\s*(\d+)\s+(\d+)\s+(\d+,\d)\s+%(.*)$"

    for line in lines:
        
        match = re.match(regex, line)
        if match:
            # Guardar el registro anterior
            if current_cluster is not None:
                texto = " ".join(palabras)
                texto = re.sub(r"\s+", " ", texto)
                texto = texto.replace(".,", ".").strip()
                if texto.endswith('.'):
                    texto = texto[:-1]
                data.append([
                    int(current_cluster),
                    int(current_cantidad),
                    float(current_porcentaje.replace(",", ".")),
                    texto,
                ])

            # Nuevo registro
            current_cluster = match.group(1)
            current_cantidad = match.group(2)
            current_porcentaje = match.group(3)
            palabras = [match.group(4).strip()]

        else:
            # Línea de continuación
            continuation = line.strip()
            if continuation:
                palabras.append(continuation)

    # Guardar el último registro
    if current_cluster is not None:
        texto = " ".join(palabras)
        texto = re.sub(r"\s+", " ", texto)
        texto = texto.replace(".,", ".").strip()
        if texto.endswith('.'):
            texto = texto[:-1]
        data.append([
            int(current_cluster),
            int(current_cantidad),
            float(current_porcentaje.replace(",", ".")),
            texto,
        ])

    # Convertir a DataFrame
    df = pd.DataFrame(
        data,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ]
    )

    return df

df = pregunta_01()
print(df)
