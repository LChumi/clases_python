import pandas as pd

print("Versión de pandas:", pd.__version__)

# Crear un DataFrame simple
df = pd.DataFrame({
    'X': [7, 8, 9],
    'Y': [10, 11, 12]
})

print("Proyecto 2 - DataFrame de Pandas 2:")
print(df)