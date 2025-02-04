# 📊 Proyecto SODIMAC Dash

Este proyecto tiene como objetivo principal la creación de tableros interactivos para la visualización de datos y el análisis de métricas de rotación de empleados, apoyado con modelos de Machine Learning. Utilizamos **Dash** y **Plotly** para una experiencia visual enriquecida y fácil de interpretar.

## 🚀 Características

- **Gráfico Radial Interactivo:** Visualización de métricas clave relacionadas con los empleados.
- **Análisis de Datos:** Procesamiento y análisis de datos provenientes de múltiples fuentes.
- **Modelo de Clustering:** Identificación de patrones de rotación de empleados mediante Machine Learning.
- **Interfaz Intuitiva:** Dashboards dinámicos para una navegación sencilla.

```

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/sodimac_dash_project.git
cd sodimac_dash_project
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/MacOS:
source venv/bin/activate
```

3. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución de la Aplicación

Para iniciar la aplicación Dash:

```bash
python src/app.py
```

Luego, abre tu navegador y accede a:

```
http://localhost:8050
```

## 📊 Métricas Analizadas

- **Sindicato:** Porcentaje de empleados que no pertenecen al sindicato.
- **Incapacidad:** Porcentaje de empleados sin incapacidades.
- **Productividad en Incapacidad:** Nivel de productividad durante incapacidades.
- **Educación:** Porcentaje de cursos completados por los empleados.
- **Auxilios:** Porcentaje de empleados que han utilizado auxilios.
- **Índice de Rotación:** Análisis del porcentaje de rotación del personal.

## 🤖 Modelos de Machine Learning

Implementamos modelos de **Clustering** para identificar patrones de rotación de empleados según características demográficas, de desempeño y participación en programas de formación.

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

---

Hecho con ❤️ y Python por el equipo de análisis de datos de SODIMAC.
