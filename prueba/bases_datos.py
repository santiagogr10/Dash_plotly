import pandas as pd

retirados = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Data empleado\12. Empleados Diciembre 2023 Talento.xlsx", sheet_name="Retirados")
auxilios = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Compensación\Prestamos y Auxilios\Prestamos & Auxilios 2023.xlsx", sheet_name= "BASE DE AUXILIOS")
prestamos = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Compensación\Prestamos y Auxilios\Prestamos & Auxilios 2023.xlsx", sheet_name= "BASE DE PRESTAMOS")
empleado_noviembre_2023_activo = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Data empleado\11. Empleados Noviembre 2023 Talento.xlsx", sheet_name="Activos")
empleado_diciembre_2023_consolidado = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Data empleado\12. Empleados Diciembre 2023 Talento.xlsx", sheet_name="Consolidado")
empleado_diciembre_2023_activo = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Data empleado\12. Empleados Diciembre 2023 Talento.xlsx", sheet_name="Activos")
rotacion_interna_acomulado  = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Data empleado\ROTACION INTERNA ACUMULADA.xlsx", sheet_name="INTERNA")
finalizacio_curso = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Desarrollo y talento humano\Formación\finalizacin_de_cursos_Dic 2023.xlsx")
solicitudes = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Desarrollo y talento humano\Selección\Sodimac Colombia - Reporte de solicitudes  20231227.xlsx")
vacantes_totales = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Desarrollo y talento humano\Selección\reporte_vacantes_totales.xlsx",sheet_name="27.12.2023")
basse_data = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Relaciones laborales y SST\Accidentalidad\Base para data 12-2023.xlsx")
enfermedades_colaborales = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Relaciones laborales y SST\Accidentalidad\ENFERMEDADES LABORALES CONSOLIDADO 12-2023.xlsx",sheet_name ="Enfermedades laborales" )
sindicato = pd.read_excel(r"C:\Users\Asus\Desktop\SODIMAC\BASE DE DATOS\OneDrive_1_2-14-2024\Relaciones laborales y SST\Sindicatos\INFORMACION SINDICAL.xlsx", sheet_name= "INFORMACION SINDICAL")


empleado_noviembre_2023_activo.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
retirados.rename(columns={'Número de Identificación': 'ID'}, inplace=True)



auxilios.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
prestamos.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
empleado_diciembre_2023_consolidado.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
empleado_diciembre_2023_activo.rename(columns={'Número de Identificación': 'ID'}, inplace=True)
rotacion_interna_acomulado.rename(columns={'Nº de documento C.C.': 'ID'}, inplace=True)
finalizacio_curso.rename(columns={'NÃºmero de ID del usuario': 'ID'}, inplace=True)
basse_data.rename(columns={'Cédula': 'ID'}, inplace=True)
enfermedades_colaborales.rename(columns={'Cédula': 'ID'}, inplace=True)
sindicato.rename(columns={'Cédula': 'ID'}, inplace=True)



vacantes_totales.rename(columns={'CARGO PLANTA':'Cargo'},inplace=True)




finalizacio_curso = finalizacio_curso[["ID", "Nombre del Curso", "CrÃ©ditos","CategorÃ­a del Curso","CalificaciÃ³n"]]
