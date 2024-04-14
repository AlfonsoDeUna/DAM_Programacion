# Ejercicio análisis de datos de la NBA

Descarga el fichero archive.zip

## Paso 1: Leer el fichero y mostrar el data frame

puedes utilizar:
``` python
df=pd.read_csv(
```

tu código: 
``` pyhton
df = pd.read_csv("C:/Users/thepi/Desktop/Python/arrays/all_seasons.csv")
print(df.to_string())
```

### ¿Cuántas filas y columnas? a través del dataframe muestra esta información

tu código: 
``` pyhton
print(df.shape[0])
print(df.shape[1])
```

## Paso 2: Quitar valores NULL (o valores nulos)

```python
#checking for null values
df.dropna(inplace=True)
df.shape
```

### ¿Cuántas filas y columnas? a través del dataframe muestra estsa información ahora.

### Mostrar toda la información del dataframe, tipos de datos de las columnas

tu código: 
``` pyhton
print(df.info())
```

### Crea un índice de la columan season

``` python
df.set_index("season", inplace=True)
```

### Cuenta los valores de la columna edad. value_conts()

``` python
print(df["age"].value_counts())
```

### Qué jugador tiene más minutos. sort_values() => Ordena valores

```python
df.sort_values(by="Total day minutes", ascending=False).head()
```

### Saca la media de edad de los jugadores de la NBA. mean()
ejemplo
```python
df["columna"].mean()
```
tu código:
```python
print(df["age"].mean())
```

### Saca la media de los jugadores estadounidenses
```python
df[df["NOMBRE_COLUMNA"] == "VALOR"].mean()
```
tu código:
```python
 print(df[df["country"] == "USA"]["age"].mean())
```

### Añade alguna columna más para que ordene

Cuenta cuantos valores hay de alguna columna más


## Paso 3: Undrafted. Jugadores que no han sido elegidos a través de este sorteo, a lo largo de la historia se han desarrollado varios “robos” o jugadores que han dejado huella en la liga,

```python
Undrafted= df_season_wise[df_season_wise['draft_year']=='Undrafted']
df_season_wise['draft_year']=df_season_wise['draft_year'].replace('Undrafted',np.NaN) 
```

  Realiza lo mismo para las columnas draft_round, draft_number

tu código: 
``` pyhton
df['draft_round'] = df['draft_round'].replace('Undrafted', np.NaN) 
df['draft_number'] = df['draft_number'].replace('Undrafted', np.NaN)
```

## Paso 4: Muestra las estadísticas de la tabla


tu código: 
``` pyhton
print(df.describe())
```

## Paso 5: Seleccionamos las columnas 

```python
import matplotlib.pyplot as plt
import numpy as np

#selecting columns required for analysis
col_need=['age','player_height','player_weight','gp','pts','reb','ast','net_rating','oreb_pct','dreb_pct','usg_pct','ts_pct','ast_pct']
ana_df=df[col_need]
ana_df
```

### quitar datos repetidos

tu código:
```python
ana_df.duplicated().values.any()
```


## Paso 6: Muestra tu tabla de correlación a partir del dataframe ana_df

EL método que hay que usar es el corr()

La correlación intenta buscar relaciones entre columnas su valor va entre 0 y 1. 

### ¿Qué columnas tiene mayor correlación?

tu respuesta: 


## Paso 7: Muestra la gráfica de la correlación

```python
pd.plotting.scatter_matrix(ana_df,figsize=(20,20),alpha=0.5);
```

### Prueba esta visualización. ¿Cuál es mejor? ¿ Por qué?

```python
#better visualization
import seaborn as sns
sns.pairplot(ana_df)
```

### gráfico para contabilizar 
```python
sns.countplot(x="COLUMNA", hue="COLUMNA", data=df);
```

## Paso 8: Crea dos o tres visualizaciones con  el dataframe que quiereas el inicial o este último mostrando información contenida en él.

Pon aquí tu código.
```python
posicion_puntos =df.plot(x="position", y="pts", kind="bar")
plt.show()
posicion_puntos =df.plot(x="position", y="pts", kind="point")
plt.show()
```
# Refereencias

* https://www.kaggle.com/code/chats351/introduction-to-numpy-pandas-and-matplotlib
* https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas
  
