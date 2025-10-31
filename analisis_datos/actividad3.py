

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo Excel (ajusta la ruta si es necesario)
df = pd.read_excel(r'c:\Users\Sheilyn Colina\Downloads\Datos Actividad 3.xlsx')  # Ej: "Datos Actividad 3.xlsx"

# Seleccionar solo las variables de interés
variables = ['SalePrice', 'GarageCars', 'LotArea', 'LotConfig', 'LotShape']
df_interes = df[variables].copy()

# Eliminar filas con valores faltantes
df_interes.dropna(inplace=True)

# =====================
# MATRIZ DE CORRELACIÓN
# =====================
correlacion = df_interes[['SalePrice', 'GarageCars', 'LotArea']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matriz de correlación")
plt.show()

# =====================
# SCATTERPLOTS
# =====================
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
sns.scatterplot(data=df_interes, x='GarageCars', y='SalePrice', alpha=0.6)
plt.title('SalePrice vs GarageCars')

plt.subplot(1, 3, 2)
sns.scatterplot(data=df_interes, x='LotArea', y='SalePrice', alpha=0.6)
plt.title('SalePrice vs LotArea')

plt.subplot(1, 3, 3)
sns.scatterplot(data=df_interes, x='GarageCars', y='LotArea', alpha=0.6)
plt.title('GarageCars vs LotArea')

plt.tight_layout()
plt.show()

# =====================
# BOXPLOTS: variables cualitativas vs SalePrice
# =====================
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=df_interes, x='LotConfig', y='SalePrice')
plt.title("SalePrice según LotConfig")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.boxplot(data=df_interes, x='LotShape', y='SalePrice')
plt.title("SalePrice según LotShape")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# =====================
# TABLAS RESUMEN POR CATEGORÍA
# =====================
# SalePrice por LotConfig
print("Resumen SalePrice por LotConfig:")
print(df_interes.groupby("LotConfig")["SalePrice"].describe())

# SalePrice por LotShape
print("\nResumen SalePrice por LotShape:")
print(df_interes.groupby("LotShape")["SalePrice"].describe())

