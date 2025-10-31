import pandas as pd

# 1️⃣ Cargar el archivo Excel
df = pd.read_excel(r"c:/Users/Sheilyn Colina/Downloads/Temperatura_Ambiente_del_Aire_20250919.xlsx")

# 2️⃣ Convertir la columna de fecha-hora a solo fecha
# Reemplaza "Fecha" por el nombre exacto de tu columna de fecha
df["FechaObservacion"] = pd.to_datetime(df["FechaObservacion"]).dt.date

# 3️⃣ Agrupar para tener solo una fila por día (promediando la temperatura)
df_diario = df.groupby("FechaObservacion", as_index=False).agg({
    "ValorObservado": "mean",     # Ajusta con el nombre exacto de tu columna de temperatura
    # Si quieres conservar otras columnas puedes agregar: "Columna": "first"
})
df_diario = df.groupby("FechaObservacion", as_index=False).agg({
    "ValorObservado": "mean",          # ajusta si tu columna de temperatura se llama distinto
    "CodigoEstacion": "first",
    "CodigoSensor": "first",
    "NombreEstacion": "first",
    "Departamento": "first",
    "Municipio": "first",
    "ZonaHidrografica": "first",
    "Latitud": "first",
    "Longitud": "first",
    "DescripcionSensor": "first",
    "UnidadMedida": "first"
})

# 4️⃣ Eliminar duplicados por si acaso
df_diario = df_diario.drop_duplicates(subset="FechaObservacion")

# 5️⃣ Quitar valores atípicos con el método IQR
Q1 = df_diario["ValorObservado"].quantile(0.25)
Q3 = df_diario["ValorObservado"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_limpio = df_diario[(df_diario["ValorObservado"] >= lower) & (df_diario["ValorObservado"] <= upper)]

# 6️⃣ Guardar el resultado
df_limpio.to_excel("Temperatura_Ambiente_Limpia.xlsx", index=False)

print("Archivo limpio guardado como Temperatura_Ambiente_Limpia.xlsx")

