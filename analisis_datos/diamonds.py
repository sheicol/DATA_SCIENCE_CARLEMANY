import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 1. Cargar el dataset diamonds
df = sns.load_dataset('diamonds')

# --- Tarea 2: Relación price vs clarity ---
# Gráfico con intervalos de confianza
plt.figure(figsize=(8,5))
sns.pointplot(x='clarity', y='price', data=df, capsize=0.2, errorbar=('ci', 95))
plt.title('Relación entre precio y claridad del diamante')
plt.show()

# Cálculo de eta cuadrado (price cuantitativa, clarity cualitativa)
groups = [df['price'][df['clarity'] == c] for c in df['clarity'].unique()]
ss_between = sum(len(g)*(g.mean()-df['price'].mean())**2 for g in groups)
ss_total = sum((y - df['price'].mean())**2 for y in df['price'])
eta_squared = ss_between / ss_total
print(f"Eta cuadrado (price vs clarity): {eta_squared:.4f}")

# --- Tarea 3: ANOVA price ~ color ---
anova_model = ols('price ~ C(color)', data=df).fit()
anova_table = sm.stats.anova_lm(anova_model, typ=2)
print("\nANOVA price ~ color")
print(anova_table)

# Si hay diferencias significativas -> Tukey HSD
tukey = pairwise_tukeyhsd(endog=df['price'], groups=df['color'], alpha=0.05)
print("\nTukey HSD")
print(tukey)

# --- Tarea 4: price vs depth ---
plt.figure(figsize=(6,4))
sns.scatterplot(x='depth', y='price', data=df)
plt.title('Relación entre profundidad y precio')
plt.show()

# Pearson (ambas cuantitativas)
corr, pval = pearsonr(df['depth'], df['price'])
print(f"Correlación Pearson (price vs depth): {corr:.4f}, p-valor: {pval:.4f}")

# --- Tarea 5: price vs depth según color ---
plt.figure(figsize=(8,5))
sns.lmplot(x='depth', y='price', hue='color', data=df, ci=95)
plt.title('Relación profundidad-precio según color')
plt.show()

# --- Tarea 6: Regresión lineal con interacción depth*color ---
model = ols('price ~ depth * C(color)', data=df).fit()
print("\nResumen modelo de regresión lineal:")
print(model.summary())
