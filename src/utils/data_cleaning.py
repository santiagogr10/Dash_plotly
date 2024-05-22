# utils/data_processing.py

import pandas as pd

def limpiar_retirados(df):
    # Suponiendo que no hay renombramientos específicos para 'Retirados'
    return df

def limpiar_auxilios(df):
    df.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
    return df

def limpiar_prestamos(df):
    df.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
    return df

def limpiar_empleado_noviembre(df):
    df.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
    return df

def limpiar_empleado_diciembre_consolidado(df):
    df.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
    return df

def limpiar_empleado_diciembre_activo(df):
    df.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
    return df

def limpiar_rotacion_interna(df):
    df.rename(columns={'Nº de documento C.C.': 'ID'}, inplace=True)
    return df

def limpiar_finalizacion_curso(df):
    df.rename(columns={'NÃºmero de ID del usuario': 'ID'}, inplace=True)
    df = df[["ID", "Nombre del Curso", "CrÃ©ditos", "CategorÃ­a del Curso", "CalificaciÃ³n"]]
    return df

def limpiar_solicitudes(df):
    # Suponiendo que no hay renombramientos específicos para 'Solicitudes'
    return df

def limpiar_vacantes_totales(df):
    df.rename(columns={'CARGO PLANTA': 'Cargo'}, inplace=True)
    return df

def limpiar_base_data(df):
    df.rename(columns={'Cédula': 'ID'}, inplace=True)
    return df

def limpiar_enfermedades_colaborales(df):
    df.rename(columns={'Cédula': 'ID'}, inplace=True)
    return df

def limpiar_sindicato(df):
    df.rename(columns={'Cédula': 'ID'}, inplace=True)
    return df
