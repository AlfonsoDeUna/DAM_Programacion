# ciencia de datos con python. Numpy, pandas y matplotlib

```python

import pandas as pd
import matplotlib.pyplot as plt

df_h = pd.read_csv("./Hurricanes.csv",delimiter=";")

print (df_h.to_string())

# seleccionar columnas de dataframe ( tabla )
print (df_h[['name','year']])

# visualiza los primros datos del dataframe
print (df_h.head())

# visualiza los últimos datos del dataframe
print (df_h.tail())

# da información estadística de los datos del dataframe
print (df_h.describe())

# información sobre filas y columnas de datafrae
print (df_h.shape)

print (df_h.info())

# configurar un indice y loc obtener los valores de un dato de ese indice
df_h_index = df_h.set_index("name")
print (df_h_index.loc["Barbara"])

df_h_index.loc["Barbara"] = df_h_index.loc["Barbara"].replace (1,2)
print (df_h_index.loc["Barbara"])
df_h_index.loc["Barbara"] = df_h_index.loc["Barbara"].replace (2,1)

# dibujar columnas 
#pp = df_h.plot (x="name" , y="deaths", kind="")
#plt.show()

# selección
print (df_h[0:3])

# muertes anuales
muertes_anuales = df_h.groupby("year")["deaths"].sum()
muertes_anuales.plot(x="year", y="deaths" , kind="bar")
plt.show()
```
