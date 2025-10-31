import pandas as pd


# Cargar el archivo (ajusta la codificación si es necesario)
df = pd.read_csv(r'c:\Users\Sheilyn Colina\Downloads\Datos Actividad 3.xlsx')

# Examinar la variable GarageCars
garage_counts = df['GarageCars'].value_counts().sort_index()

# Mostrar la moda
moda = garage_counts.idxmax()
print(f"El tamaño de garaje más común (número de coches) es: {moda}")
