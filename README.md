Atajo ctrl + shif + v
# estructura proyecto
```
sodimac_dash_project/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   ├── app.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── radial_chart.py
│   ├── assets/
│   │   ├── style.css
│   ├── data/
│   │   └── data.csv
│   └── utils/
│       ├── __init__.py
│       ├── data_processing.py
├── tests/
│   ├── test_app.py
└── docs/
    ├── index.md
    ├── usage.md
    └── api.md
```
# Proyecto SODIMAC Dash

Este proyecto tiene como objetivo proporcionar una base para la creación de productos de visualización de datos y modelos de IA utilizando Dash. La primera implementación incluye una gráfica radial con métricas obtenidas de bases de datos.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/sodimac_dash_project.git
    cd sodimac_dash_project
    ```

2. Crea un entorno virtual y activa el entorno:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar la aplicación Dash:

```bash
python src/app.py



