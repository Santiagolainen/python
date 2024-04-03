mediciones = [37.15,37.21,36.95,36.87,37.05,37.11,37.09,36.93,37.21,37.14,37.27,37.39,37.47,37.24,37.28,37.28,37.35,
              36.31,37.23,37.17,37.27,37.12,37.32,37.53,37.79,37.92,37.81,37.36,36.26,37.18]

errores = [0.47,0.22,0.57,0.09,0.04,0.11,0.09,0.64,0.26,0.12,0.25,0.05,0.11,0.26,0.22,
          0.78,0.43,0.32,0.6,0.67,0.01,0.72,0.37,0.36,0.53,0.64,0.09,0.25,0.2,0.26]

numMediciones = len(mediciones)
deltaPromedio = 0
deltaD = 0

for j in range(len(mediciones)):
    deltaPromedio += mediciones[j]

promedioM = (deltaPromedio)/len(mediciones)

for i in range(len(mediciones)):
    deltaD += pow(mediciones[i]- promedioM,2)



desviacion = ((deltaD/(numMediciones - 1)))**1/2

incertidumbre = desviacion/pow(numMediciones,1/2)

print(promedioM)

print(round(desviacion,2))
print(round(incertidumbre,2))