def calculos(Filtro,nombre_columna,variables):
    retirados = variables[0]
    auxilios = variables[1]
    prestamos = variables[2]
    empleado_noviembre_2023_activo = variables[3]
    empleado_diciembre_2023_consolidado = variables[4]
    empleado_diciembre_2023_activo = variables[5]
    rotacion_interna_acomulado = variables[6]
    finalizacio_curso = variables[7]
    solicitudes = variables[8]
    vacantes_totales = variables[9]
    basse_data = variables[10]
    enfermedades_colaborales = variables[11]
    sindicato  = variables[12]

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
    else:
        # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
        print(f"No hay datos disponibles para {Filtro}.")


    recuento_uniq = auxil_data_frame['ID'].nunique()
    auxi = (recuento_uniq/tamaño_gerencia)*100
   


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
       
    else:
        # Imprime un mensaje indicando que no hay datos para el valor filtrado
        print(f"No hay datos disponibles para {Filtro}.")



    I_total = empleado_diciembre_2023_activo[pd.to_datetime(empleado_diciembre_2023_activo['Fecha de Ingreso']).dt.year == 2023]
    I_total_diciembre_2023 = I_total[pd.to_datetime(I_total['Fecha de Ingreso']).dt.month == 12]


    grupo_data = I_total_diciembre_2023.groupby(nombre_columna)

    # Verifica si el valor filtrado está presente en el índice
    if Filtro in grupo_data.groups:
        # Obtén los datos para el valor filtrado
        rot = grupo_data.size()[Filtro]
        base_ingreso = I_total_diciembre_2023.query(f"`{nombre_columna}` == '{Filtro}'")
        base_ingreso_nueva = 1
    else:
        base_ingreso_nueva = 0
        print(f"No hay datos disponibles para {Filtro}.")


    # Calcularemos retirados para todas las personas que se fueron en  diciembre 

    # In[78]:


    R = retirados[pd.to_datetime(retirados['Fecha de Retiro']).dt.year == 2023]
    R_diciembre_2023 = R[pd.to_datetime(R['Fecha de Retiro']).dt.month == 12]


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
       
    else:
        # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
        print(f"No hay datos disponibles para {Filtro}.")


    # FORMULA

    # In[82]:


    PE =( existentes_novi.shape[0] +existentes_dic.shape[0])/2


    # In[83]:


    if base_ingreso_nueva != 0:
        indice_rot = 100 - (((base_retiros.shape[0] + base_ingreso.shape[0])/2)*100)/PE
        
    else:
        indice_rot = 100 - (((base_retiros.shape[0] + base_ingreso_nueva)/2)*100)/PE
        


    # FORMULA GENERAL

    # In[84]:


    indic_gene = (((I_total_diciembre_2023.shape[0] + R_diciembre_2023.shape[0] )/2)*100)/((empleado_noviembre_2023_activo.shape[0] + empleado_diciembre_2023_activo.shape[0])/2)


    # Realiza la fusión de los datos
    conex_curso = pd.merge(empleado_diciembre_2023_activo, finalizacio_curso, on='ID')

    # Agrupa los datos por la columna deseada
    grupo_curso = conex_curso.groupby(nombre_columna)

    # Verifica si el valor filtrado está presente en el índice
    if Filtro in grupo_curso.groups:
        # Obtén los datos para el valor filtrado
        rot = grupo_curso.size()[Filtro]
        base_formacion = conex_curso.query(f"`{nombre_columna}` == '{Filtro}'")
    else:
        # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
        print(f"No hay datos disponibles para {Filtro}.")


    mascara = base_formacion['CategorÃ­a del Curso'] == "ONBOARDING"
    # Aplicar la máscara booleana para filtrar el DataFrame
    resultado = base_formacion[mascara]
    Cursos_realizados = resultado.groupby("ID").size()




    prom_cantidad_cursos = resultado.groupby("ID").size().mean()
    porcentaje_cursos = ((prom_cantidad_cursos)/12)*100
    porcentaje_cursos

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
    else:
        na_nueva = 0
        print(f"No hay datos disponibles para {Filtro}.")

    if na_nueva != 0:
        sanas = ((tamaño_gerencia - na.shape[0])/tamaño_gerencia)*100
    else:
        sanas = ((tamaño_gerencia -0)/tamaño_gerencia)*100

    if na_nueva == 0:
        promedio = 0
    else:
        basse_data_copia_sin_na = na.dropna(subset=['% Productividad'])
        filas_filtradas_100 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('100%')].shape[0]
        filas_filtradas_75 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('75%')].shape[0]
        filas_filtradas_50 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('50%')].shape[0]
        filas_filtradas_0 = basse_data_copia_sin_na[basse_data_copia_sin_na['% Productividad'].str.contains('No cumple%')].shape[0]
        promedio = (filas_filtradas_100*100 + filas_filtradas_75*75 + filas_filtradas_50*50 +filas_filtradas_0*0)/(filas_filtradas_100+filas_filtradas_75+filas_filtradas_50+filas_filtradas_0)

    conex_colab = pd.merge(empleado_diciembre_2023_activo, enfermedades_colaborales, on='ID')

    # Agrupa los datos por la columna deseada
    grupo_colab = conex_colab.groupby(nombre_columna)

    # Verifica si el valor filtrado está presente en el índice
    if Filtro in grupo_colab.groups:
        # Obtén los datos para el valor filtrado
        rot = grupo_colab.size()[Filtro]
        base_colab = conex_colab.query(f"`{nombre_columna}` == '{Filtro}'")
    else:
        # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
        print(f"No hay datos disponibles para {Filtro}.")

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
    else:
        # Imprime un mensaje indicando que no hay datos disponibles para el valor filtrado
        base_sindi2_nueva = 0
        print(f"No hay datos disponibles para {Filtro}.")



    if base_sindi2_nueva != 0:
        no_pertenece = ((tamaño_gerencia - base_sindi2.shape[0])/tamaño_gerencia)*100
    else:
        no_pertenece = ((tamaño_gerencia - 0)/tamaño_gerencia)*100

    return [no_pertenece, sanas, promedio, porcentaje_cursos, auxi, indice_rot]


