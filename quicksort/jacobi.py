
import matplotlib.pyplot as plt

def norma_infinito(vector):
    """
    Calcula la norma infinito (máximo valor absoluto) de un vector.

    Entrada:
    - vector: lista de valores

    Salida:
    - norma: valor máximo absoluto
    """
    return max(abs(x) for x in vector)


def resta_vectores(v1, v2):
    """
    Resta dos vectores elemento a elemento.

    Entradas:
    - v1, v2: listas del mismo tamaño

    Salida:
    - lista con v1 - v2
    """
    return [v1[i] - v2[i] for i in range(len(v1))]


def metodo_jacobi(A, b, x0, tolerancia, max_iter=1000):
    """
    Implementa el método iterativo de Jacobi.

    Entradas:
    - A: matriz de coeficientes
    - b: vector independiente
    - x0: vector inicial
    - tolerancia: valor de convergencia
    - max_iter: número máximo de iteraciones

    Salida:
    - x: solución aproximada
    - iteraciones: número de iteraciones realizadas
    - historial: lista de vectores x por iteración
    """
    n = len(A)
    x_ant = x0[:]
    x_nuevo = x0[:]
    historial = [x0[:]]

    for iteracion in range(1, max_iter + 1):
        for i in range(n):
            suma = sum(A[i][j] * x_ant[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        historial.append(x_nuevo[:])
        error = norma_infinito(resta_vectores(x_nuevo, x_ant))
        if error < tolerancia:
            return x_nuevo, iteracion, historial
        x_ant = x_nuevo[:]

    return x_nuevo, iteracion, historial


def metodo_gauss_seidel(A, b, x0, tolerancia, max_iter=1000):
    """
    Implementa el método iterativo de Gauss-Seidel.

    Entradas:
    - A: matriz de coeficientes
    - b: vector independiente
    - x0: vector inicial
    - tolerancia: valor de convergencia
    - max_iter: número máximo de iteraciones

    Salida:
    - x: solución aproximada
    - iteraciones: número de iteraciones realizadas
    - historial: lista de vectores x por iteración
    """
    n = len(A)
    x = x0[:]
    historial = [x0[:]]

    for iteracion in range(1, max_iter + 1):
        x_old = x[:]
        for i in range(n):
            suma1 = sum(A[i][j] * x[j] for j in range(i))
            suma2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - suma1 - suma2) / A[i][i]
        historial.append(x[:])
        error = norma_infinito(resta_vectores(x, x_old))
        if error < tolerancia:
            return x, iteracion, historial

    return x, iteracion, historial


# Sistema de ecuaciones
A = [
    [4, 1, 2, 0],
    [-2, 6, 1, 2],
    [2, -3, 7, 1],
    [0, -2, 1, 4]
]

b = [7, -5.5, 28.5, 18.5]
x0 = [0, 0, 0, 0]
tolerancia = 1e-9

# Jacobi
sol_jacobi, it_jacobi, hist_jacobi = metodo_jacobi(A, b, x0, tolerancia)

# Gauss-Seidel
sol_gs, it_gs, hist_gs = metodo_gauss_seidel(A, b, x0, tolerancia)

# Resultados
print("Jacobi:")
print("Solución:", sol_jacobi)
print("Iteraciones:", it_jacobi)

print("\nGauss-Seidel:")
print("Solución:", sol_gs)
print("Iteraciones:", it_gs)



# Solución exacta
sol_exacta = [1, -2, 2.5, 3]

# Cálculo del error absoluto por iteración
def errores_por_iteracion(historial, solucion_exacta):
    """
    Calcula el error absoluto en norma infinito por iteración.

    Entradas:
    - historial: lista de vectores x(k)
    - solucion_exacta: vector solución exacta

    Salida:
    - lista de errores por iteración
    """
    errores = []
    for xk in historial[:50]:  # Solo 50 iteraciones
        error = norma_infinito(resta_vectores(xk, solucion_exacta))
        errores.append(error)
    return errores

errores_jacobi = errores_por_iteracion(hist_jacobi, sol_exacta)
errores_gs = errores_por_iteracion(hist_gs, sol_exacta)

# Gráfico
plt.figure(figsize=(10,6))
plt.plot(errores_jacobi, label='Jacobi', marker='o')
plt.plot(errores_gs, label='Gauss-Seidel', marker='x')
plt.yscale('log')
plt.xlabel('Iteración')
plt.ylabel('Error absoluto (norma ∞)')
plt.title('Evolución del error en Jacobi vs Gauss-Seidel')
plt.legend()
plt.grid(True)
plt.show()
