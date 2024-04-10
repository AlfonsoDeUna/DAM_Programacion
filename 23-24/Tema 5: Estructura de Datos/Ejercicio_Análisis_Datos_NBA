# Ejercicio análisis de datos de la NBA

Descarga el fichero archive.zip

## Paso 1: Leer el fichero y mostar el data frame

puedes utilizar:
``` python
df=pd.read_csv(
```

tu código: 
``` pyhton

```

### ¿Cuántas filas y columnas? a través del dataframe muestra estsa información

tu código: 
``` pyhton

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

```

### Crea un índice de la columan season

``` python

```

## Paso 3: Undrafted. Jugadores que no han sido elegidos a través de este sorteo, a lo largo de la historia se han desarrollado varios “robos” o jugadores que han dejado huella en la liga,

```python
Undrafted= df_season_wise[df_season_wise['draft_year']=='Undrafted']
df_season_wise['draft_year']=df_season_wise['draft_year'].replace('Undrafted',np.NaN) 
```

  Realiza lo mismo para las columnas draft_round, draft_number

tu código: 
``` pyhton

```

## Paso 4: Muestra las estadísticas de la tabla


tu código: 
``` pyhton

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

### quitar repetidos

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

## Paso 8: Crea dos o tres visualizaciones con  el dataframe que quiereas el inicial o este último mostrando información contenida en él.

Pon aquí tu código.
```python

```
