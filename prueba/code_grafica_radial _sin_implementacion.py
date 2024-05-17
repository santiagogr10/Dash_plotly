from bases_datos import retirados, auxilios, prestamos, empleado_noviembre_2023_activo, empleado_diciembre_2023_consolidado, empleado_diciembre_2023_activo, rotacion_interna_acomulado, finalizacio_curso, solicitudes, vacantes_totales, basse_data, enfermedades_colaborales, sindicato
import pandas as pd
import matplotlib.pyplot as plt
import PyPDF2 as pdf
from IPython.display import display
from datetime import datetime, timedelta
import datetime
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np



Centro__de_Trabajo = "CENTRO DE DISTRIBUCION"   #OFICINA APOYO A TIENDAS     #CENTRO DE DISTRIBUCION       #ALMACEN CALLE 80
Id_Centro_Costo = "O003100201"     #GERENCIA COMERCIAL - O003003001 # AV. 68 SUR PRINCIPAL - O003100201
Cargo = "VENDEDOR"    #CAJERO    #VENDEDOR

#Centro_Costo_Gerentes = "GERENCIA COMERCIAL" 
#Macrogerencia = "GERENCIA COMERCIAL Y MARKETING"



Filtro = Cargo
nombre_columna = "Cargo"





# Opciones para los dropdowns
options_1 = ["Centro de Trabajo", "Id Centro Costo", "Cargo", "Centro Costo Gerentes", "Macrogerencia"]
options_2 = {
    "Centro de Trabajo": ["OFICINA APOYO A TIENDAS", "CENTRO DE DISTRIBUCION ", "ALMACEN CALLE 80"],
    "Id Centro Costo": ["O003003001", "O003100201"],
    "Cargo": ["CAJERO", "VENDEDOR"],
    "Centro Costo Gerentes": ["GERENCIA COMERCIAL"],
    "Macrogerencia": ["GERENCIA COMERCIAL Y MARKETING"]
}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("General"),
    dcc.Dropdown(
        id='general-dropdown',
        options=[{'label': k, 'value': k} for k in options_1],
        value=options_1[0]
    ),
    html.Label("Specific"),
    dcc.Dropdown(
        id='specific-dropdown',
    ),
    html.Button('Save', id='save-button'),
    html.Button('Close', id='close-button', n_clicks=0)
])

@app.callback(
    Output('specific-dropdown', 'options'),
    [Input('general-dropdown', 'value')]
)
def set_specific_options(selected_general):
    return [{'label': i, 'value': i} for i in options_2.get(selected_general, [])]

@app.callback(
    Output('general-dropdown', 'value'),
    [Input('close-button', 'n_clicks')]
)
def close_app(n_clicks):
    if n_clicks > 0:
        raise dash.exceptions.PreventUpdate
    return dash.no_update




tamaño_gerencia = empleado_diciembre_2023_activo.groupby(nombre_columna).size()[Filtro]
tamaño_gerencia


# ## **Compensación**

# ### **Auxilios**

# Vamos a filtrar la base principal, por los empleados que iniciarón antes del 2023




empleado_diciembre_2023_activo['Fecha de Ingreso'] = pd.to_datetime(empleado_diciembre_2023_activo['Fecha de Ingreso'], format='%d/%m/%Y')

# Filtrar los valores antes del año 2023
result = empleado_diciembre_2023_activo[empleado_diciembre_2023_activo['Fecha de Ingreso'].dt.year < 2023]


# Conexion entre base y auxilios




# Realiza la fusión de los datos
conex_auxilio = pd.merge(result, auxilios, on='ID')

# Agrupa los datos por la columna deseada
grupo = conex_auxilio.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo.groups:
    # Obtén los datos para el valor filtrado
    aux = grupo.size()[Filtro]
    auxil_data_frame = conex_auxilio.query(f"`{nombre_columna}` == '{Filtro}'")
    print(auxil_data_frame.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


recuento_uniq = auxil_data_frame['ID'].nunique()
auxi = (recuento_uniq/tamaño_gerencia)*100
auxi


# ### **Prestamos**



# Realiza la fusión de los datos
conex_prestamos = pd.merge(empleado_diciembre_2023_activo, prestamos, on='ID')

# Agrupa los datos por la columna deseada
grupo = conex_prestamos.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo.groups:
    # Obtén los datos para el valor filtrado
    pres = grupo.size()[Filtro]
    prestamos_data_frame = conex_prestamos.query(f"`{nombre_columna}` == '{Filtro}'")
    print(prestamos_data_frame.shape)
else:
    # Imprime un mensaje indicando que no hay datos para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# Los prestamos que se utilizaron 

# ## **Data empleado**

# ### Rotacion interna acomulada

# #### Indice de rotación

# -   I = Ingresos 
# -   R = Retirados
# -   PE = (Planta inicio +planta final)/2
# 
# FORMULA
# 
# $$\frac{\left(\frac{I + R}{2}\right)}{PE}$$
# 

# Calcularemos los Ingreso, filtrando la columna de fecha de ingreso, por todas las personas que entrarón en noviembre y Diciembre 

# In[76]:


I_total = empleado_diciembre_2023_activo[pd.to_datetime(empleado_diciembre_2023_activo['Fecha de Ingreso']).dt.year == 2023]
I_total_diciembre_2023 = I_total[pd.to_datetime(I_total['Fecha de Ingreso']).dt.month == 12]
I_total_diciembre_2023.shape[0]


# In[77]:


grupo_data = I_total_diciembre_2023.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_data.groups:
    # Obtén los datos para el valor filtrado
    rot = grupo_data.size()[Filtro]
    base_ingreso = I_total_diciembre_2023.query(f"`{nombre_columna}` == '{Filtro}'")
    base_ingreso_nueva = 1
    print(base_ingreso.shape)
else:
    base_ingreso_nueva = 0
    print(f"No hay datos disponibles para {Filtro}.")


# Calcularemos retirados para todas las personas que se fueron en  diciembre 

# In[78]:


R = retirados[pd.to_datetime(retirados['Fecha de Retiro']).dt.year == 2023]
R_diciembre_2023 = R[pd.to_datetime(R['Fecha de Retiro']).dt.month == 12]
R_diciembre_2023.shape[0]


# In[79]:


if nombre_columna == "Centro Costo Gerentes":
    nombre_columna_unico = "Centro Costo" 
    grupo_data = R_diciembre_2023.groupby(nombre_columna_unico)
elif nombre_columna == "Centro  de Trabajo":
    nombre_columna_unico = "Lugar de Trabajo"
else:
    nombre_columna_unico = nombre_columna
grupo_data = R_diciembre_2023.groupby(nombre_columna_unico)
# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_data.groups:
    # Obtén los datos para el valor filtrado
    base_retiros = R_diciembre_2023.query(f"`{nombre_columna_unico}` == '{Filtro}'")
    print(base_retiros.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# empleados existentes en Noviembre

# In[80]:


existentes_noviembre = empleado_noviembre_2023_activo.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_data.groups:
    # Obtén los datos para el valor filtrado
    existentes_novi = empleado_noviembre_2023_activo.query(f"`{nombre_columna}` == '{Filtro}'")
    print(existentes_novi.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# empleados existentes en Diciembre

# In[81]:


existentes_noviembre = empleado_diciembre_2023_activo.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_data.groups:
    # Obtén los datos para el valor filtrado
    existentes_dic = empleado_diciembre_2023_activo.query(f"`{nombre_columna}` == '{Filtro}'")
    print(existentes_dic.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# FORMULA

# In[82]:


PE =( existentes_novi.shape[0] +existentes_dic.shape[0])/2


# In[83]:


if base_ingreso_nueva != 0:
    indice_rot = 100 - (((base_retiros.shape[0] + base_ingreso.shape[0])/2)*100)/PE
    print(indice_rot)
else:
    indice_rot = 100 - (((base_retiros.shape[0] + base_ingreso_nueva)/2)*100)/PE
    print(indice_rot)


# FORMULA GENERAL

# In[84]:


indic_gene = (((I_total_diciembre_2023.shape[0] + R_diciembre_2023.shape[0] )/2)*100)/((empleado_noviembre_2023_activo.shape[0] + empleado_diciembre_2023_activo.shape[0])/2)
indic_gene


# ## **Desarrollo y talento humano**

# ### Formación

# Conexion con base de datos

# In[85]:



# Realiza la fusión de los datos
conex_curso = pd.merge(empleado_diciembre_2023_activo, finalizacio_curso, on='ID')

# Agrupa los datos por la columna deseada
grupo_curso = conex_curso.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_curso.groups:
    # Obtén los datos para el valor filtrado
    rot = grupo_curso.size()[Filtro]
    base_formacion = conex_curso.query(f"`{nombre_columna}` == '{Filtro}'")
    print(base_formacion.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# Vamos a filtrar por los cursos obligatorios. HAY 12 CURSOS EN LA BASE DE DATOS:


# HAY 15 CURSOS EN LA BASE DE DATOS

#cursos_obligatorios = ["PROTECCIÃ“N DE DATOS PERSONALES", "Curso de Ã‰tica Empresarial", "LAVADO DE ACTIVOS, FINANCIACIÃ“N DEL TERRORISMO, SOBORNO Y CORRUPCIÃ“N", "POLITICA DE SEGURIDAD DE LA INFORMACIÃ“N","SEGURIDAD DE LA INFORMACIÃ“N","LEAL Y LIBRE COMPETENCIA","RESPONSABILIDAD SOCIAL","SENSIBILIZACIÃ“N EN DERECHOS HUMANOS", "CURSO DE RELACIONAMIENTO CON PROVEEDORES", "OEA","Asistencia InducciÃ³n","Refuerzo Anual de Seguridad de la InformaciÃ³n y ProtecciÃ³n de Datos"]
#resultado_filtrado = base_formacion[base_formacion['Nombre del Curso'].isin(cursos_obligatorios)]
mascara = base_formacion['CategorÃ­a del Curso'] == "ONBOARDING"
# Aplicar la máscara booleana para filtrar el DataFrame
resultado = base_formacion[mascara]
Cursos_realizados = resultado.groupby("ID").size()




prom_cantidad_cursos = resultado.groupby("ID").size().mean()
porcentaje_cursos = ((prom_cantidad_cursos)/12)*100
porcentaje_cursos


# ### Selección

# ## **Relaciones laborales y SST**

# ### Accidentalidad - salud

# Base_data

# Mirar la conexión con la base de datos principal

# In[88]:



# Realiza la fusión de los datos
conex_basedata = pd.merge(empleado_diciembre_2023_activo, basse_data, on='ID')

# Agrupa los datos por la columna deseada
grupo_data = conex_basedata.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_data.groups:
    # Obtén los datos para el valor filtrado
    rot = grupo_data.size()[Filtro]
    na = conex_basedata.query(f"`{nombre_columna}` == '{Filtro}'")
    na_nueva = 1
    print(na.shape)
else:
    na_nueva = 0
    print(f"No hay datos disponibles para {Filtro}.")


# ¿Cuántas personas están sanas dentro del equipo?

# In[89]:


if na_nueva != 0:
    sanas = ((tamaño_gerencia - na.shape[0])/tamaño_gerencia)*100
    print(sanas)
else:
      sanas = ((tamaño_gerencia -0)/tamaño_gerencia)*100
      print(sanas)


# ¿ Cuál es la productividad de las personas que están sanas ?

# In[90]:


if na_nueva == 0:
    promedio = 0
else:
    basse_data_copia_sin_na = na.dropna(subset=['% Productividad'])
    filas_filtradas_100 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('100%')].shape[0]
    filas_filtradas_75 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('75%')].shape[0]
    filas_filtradas_50 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('50%')].shape[0]
    filas_filtradas_0 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('No cumple%')].shape[0]
    promedio = (filas_filtradas_100*100 + filas_filtradas_75*75 + filas_filtradas_50*50 +filas_filtradas_0*0)/(filas_filtradas_100+filas_filtradas_75+filas_filtradas_50+filas_filtradas_0)
    print(promedio)


# **Enfermedades Laborales**

# Conexión con base de datos principal

# In[91]:



# Realiza la fusión de los datos
conex_colab = pd.merge(empleado_diciembre_2023_activo, enfermedades_colaborales, on='ID')

# Agrupa los datos por la columna deseada
grupo_colab = conex_colab.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_colab.groups:
    # Obtén los datos para el valor filtrado
    rot = grupo_colab.size()[Filtro]
    base_colab = conex_colab.query(f"`{nombre_columna}` == '{Filtro}'")
    print(base_colab.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    print(f"No hay datos disponibles para {Filtro}.")


# ### SINDICATOS

# Conexion base de datos con principal

# In[92]:



# Realiza la fusión de los datos
conex_sindi = pd.merge(empleado_diciembre_2023_activo, sindicato, on='ID')

# Agrupa los datos por la columna deseada
grupo_colab = conex_sindi.groupby(nombre_columna)

# Verifica si el valor filtrado está presente en el índice
if Filtro in grupo_colab.groups:
    # Obtén los datos para el valor filtrado
    rot = grupo_colab.size()[Filtro]
    base_sindi2 = conex_sindi.query(f"`{nombre_columna}` == '{Filtro}'")
    base_sindi2_nueva = 1
    print(base_sindi2.shape)
else:
    # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
    base_sindi2_nueva = 0
    print(f"No hay datos disponibles para {Filtro}.")


# Se quiere mirar que porcentaje de la gerencia no pertenece al sindicato

# In[93]:


if base_sindi2_nueva != 0:
    no_pertenece = ((tamaño_gerencia - base_sindi2.shape[0])/tamaño_gerencia)*100
    no_pertenece
else:
    no_pertenece = ((tamaño_gerencia - 0)/tamaño_gerencia)*100
    no_pertenece


# Se quiere ver el número de personas por cada sindicato

# In[94]:


if base_sindi2_nueva != 0:
    import matplotlib.pyplot as plt

    # Contar los valores únicos en la columna "ORGANIZACIÓN"
    conteo_organizacion = base_sindi2["CALIDAD"].value_counts()



# # **DASHBOARD GENERAL**

# In[95]:




# Datos
categorias = ["Sindicato", 'Incapacidad', 'Product. Incapacidad', 'Educación', 'Auxilios', 'Índice de rotación']
valores = [no_pertenece, sanas, promedio, porcentaje_cursos, auxi, indice_rot]  # Valores de cada categoría
valores += valores[:1]  # Añadir el primer valor al final para cerrar el gráfico

# Número de categorías
num_categorias = len(categorias)

# Ángulos para cada categoría
angulos = np.linspace(0, 2 * np.pi, num_categorias, endpoint=False).tolist()
angulos += angulos[:1]  # Añadir el primer ángulo al final para cerrar el gráfico

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=valores,
    theta=categorias,
    fill='toself',
    name='Categorías'
))

# Personalizar el gráfico
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    title={
        'text': Filtro,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    showlegend=False
)

# Mostrar el gráfico
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True, port = 8051)
# In[ ]:




