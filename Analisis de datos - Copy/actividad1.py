import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Paso 1: Leer el archivo y preparar los datos
df = pd.read_excel(r'c:\Users\Sheilyn Colina\Downloads\Datos Actividad 1.xlsx')

# Renombrar la tercera columna (cambia el nombre si es diferente en tu archivo)
df.rename(columns={df.columns[2]: "Average Growth %"}, inplace=True)

# Convertir a porcentaje
df["Average Growth %"] = df["Average Growth %"] * 100


#Paso 2: Histogramas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df["HDI 2021"].dropna(), bins=10, color='skyblue')
plt.title("Histograma HDI 2021")

plt.subplot(1, 2, 2)
plt.hist(df["Average Growth %"].dropna(), bins=10, color='salmon')
plt.title("Histograma Average Growth %")

plt.tight_layout()
plt.show()


#Paso 3: Gráficos de densidad
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.kdeplot(df["HDI 2021"].dropna(), fill=True)
plt.title("Densidad HDI 2021")

plt.subplot(1, 2, 2)
sns.kdeplot(df["Average Growth %"].dropna(), fill=True)
plt.title("Densidad Average Growth %")

plt.tight_layout()
plt.show()


# Paso 4: Estadísticas descriptivas
variables = ["HDI 2021", "Average Growth %"]

for var in variables:
    serie = df[var].dropna()
    print(f"\n--- {var} ---")
    print(f"Media: {serie.mean():.4f}")
    print(f"Mediana: {serie.median():.4f}")
    print(f"Desviación estándar: {serie.std():.4f}")
    print(f"Coeficiente de variación: {serie.std() / serie.mean():.4f}")
    print(f"Rango intercuartílico (IQR): {serie.quantile(0.75) - serie.quantile(0.25):.4f}")
    print(f"Cuartiles: Q1={serie.quantile(0.25):.4f}, Q2={serie.quantile(0.5):.4f}, Q3={serie.quantile(0.75):.4f}")
    print(f"Mínimo: {serie.min():.4f}")
    print(f"Máximo: {serie.max():.4f}")


'''Conclusion:
• En ambas variables, la media y la mediana son similares (HDI: media = 0.7161, mediana = 0.7305; Crecimiento: media = 0.4463%, mediana = 0.39%), lo cual indica que la distribución no presenta sesgos importantes ni valores atípicos extremos que distorsionen la tendencia central.

• El HDI 2021 muestra una media de 0.716 con una desviación estándar de 0.156. Esto indica que la mayoría de los países tienen niveles de desarrollo humano medios a altos, con una dispersión moderada (IQR = 0.249). El valor mínimo es 0.385 y el máximo 0.962, lo que sugiere una amplia brecha de desarrollo entre los países más rezagados y los más avanzados.

• El Average Growth % presenta una media del 0.45% anual, pero con una desviación estándar de 0.46, lo cual es mayor que su media, dando como resultado un coeficiente de variación mayor a 1 (CV = 1.027). Esto indica alta dispersión y desigualdad en los ritmos de crecimiento del HDI. Algunos países incluso muestran valores negativos (mínimo = -1.21%), lo que implica un retroceso en desarrollo humano en ese periodo.

• En comparación, mientras el nivel actual de HDI muestra homogeneidad relativa, el crecimiento anual entre 2010 y 2021 ha sido muy desigual, reflejando diferencias significativas en las trayectorias de mejora entre países.

• El rango intercuartílico del crecimiento (IQR = 0.5%) es relativamente alto en relación con su media, reforzando la idea de gran variabilidad entre países en cuanto al progreso sostenido en el tiempo.
'''

