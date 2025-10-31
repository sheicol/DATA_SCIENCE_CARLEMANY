def padovan(N):
    P = [[0,1,1],   
         [1,0,0],    
         [0,1,0]]   


    if (N <= 2):
        return 1
    power(P, N-2)
    return P[0][0]*1 + P[0][1]*1 + P[0][2]*1

def multiply (P, M):
    
    a00 = P[0][0]*M[0][0] + P[0][1]*M[1][0] + P[0][2]*M[2][0]
    a01 = P[0][0]*M[0][1] + P[0][1]*M[1][1] + P[0][2]*M[2][1]
    a02 = P[0][0]*M[0][2] + P[0][1]*M[1][2] + P[0][2]*M[2][2]

    a10 = P[1][0]*M[0][0] + P[1][1]*M[1][0] + P[1][2]*M[2][0]
    a11 = P[1][0]*M[0][1] + P[1][1]*M[1][1] + P[1][2]*M[2][1]
    a12 = P[1][0]*M[0][2] + P[1][1]*M[1][2] + P[1][2]*M[2][2]

    a20 = P[2][0]*M[0][0] + P[2][1]*M[1][0] + P[2][2]*M[2][0]
    a21 = P[2][0]*M[0][1] + P[2][1]*M[1][1] + P[2][2]*M[2][1]
    a22 = P[2][0]*M[0][2] + P[2][1]*M[1][2] + P[2][2]*M[2][2]


 # asignamos de vuelta a P (en sitio)
    P[0][0], P[0][1], P[0][2] = a00, a01, a02
    P[1][0], P[1][1], P[1][2] = a10, a11, a12
    P[2][0], P[2][1], P[2][2] = a20, a21, a22
    
    
def power(P,N):
    if (N == 0 or N == 1):
        return
    M = [[0,1,1],[1,0,0],[0,1,0]]

    power(P,N//2)
    multiply(P, P)

    if (N % 2 != 0):
        multiply(P, M)

N = int(input('numero de terminos:'))

if N<=0:
    print('Introduce un numero positivo')
print('Series de Padovan:')
print(padovan(N))
    
