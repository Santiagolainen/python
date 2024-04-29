mediciones = [28.45,29.14,28.35,29.01,28.88,29.03,28.87,29.56,28.66,29.04,28.67,28.87,29.03,28.66,29.14,28.71,
              29.35,29.24,28.32,29.59,28.93,29.64,28.55,28.56,29.45,29.56,29.01,28.67,29.12,28.66]

errores = [0.22,0.05,0.32,0.01,0.01,0.01,0.01,0.41,0.07,0.01,0.06,0.01,0.01,0.07,0.05,0.04,0.19,0.1,0.36,0.45,0.01,0.52
    ,0.14,0.13,0.28,0.41,0.01,0.06,0.04,0.07]

numMediciones = len(mediciones)
deltaPromedio = 0
deltaD = 0

for j in range(len(mediciones)):
    deltaPromedio += mediciones[j]

promedioM = 28.92

for i in range(len(mediciones)):
    deltaD += pow(mediciones[i]- promedioM,2)
    print(round(pow(mediciones[i] - 28.92,2), 3))

sumaErrores = 0


for k in range(len(errores)):
    sumaErrores += errores[k]

desviacion = ((deltaD/(numMediciones - 1)))**1/2

incertidumbre = desviacion/pow(numMediciones,1/2)

print(promedioM)
print(sumaErrores)
print(round(desviacion,2))
print(round(incertidumbre,2))
print(deltaD)


