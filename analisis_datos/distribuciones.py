import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo
df = pd.read_excel(r'c:\Users\Sheilyn Colina\Downloads\Datos Actividad 3.xlsx')

# Filtrar variables necesarias y limpiar
df_interes = df[['SalePrice']].dropna()

# Extraer la columna como array
sale_prices = df_interes["SalePrice"].values

# Fijar semilla
np.random.seed(450)

# Función para generar medias de submuestras
def generar_medias_submuestras(data, n_submuestras, tamaño_muestra):
    medias = []
    for _ in range(n_submuestras):
        muestra = np.random.choice(data, size=tamaño_muestra, replace=True)
        medias.append(np.mean(muestra))
    return np.array(medias)

# Submuestras de 20 y 300
medias_20 = generar_medias_submuestras(sale_prices, 300, 20)
medias_300 = generar_medias_submuestras(sale_prices, 300, 300)

# Cálculo de estadísticas
media_20 = np.mean(medias_20)
std_20 = np.std(medias_20)

media_300 = np.mean(medias_300)
std_300 = np.std(medias_300)

# Visualización
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(medias_20, kde=True, color='skyblue')
plt.title(f'Submuestras de 20\nMedia: {media_20:.2f}, STD: {std_20:.2f}')
plt.xlabel('Media de submuestra (n=20)')

plt.subplot(1, 2, 2)
sns.histplot(medias_300, kde=True, color='salmon')
plt.title(f'Submuestras de 300\nMedia: {media_300:.2f}, STD: {std_300:.2f}')
plt.xlabel('Media de submuestra (n=300)')

plt.tight_layout()
plt.show()



