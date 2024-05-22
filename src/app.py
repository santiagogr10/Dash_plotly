import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import base64
import io
from utils.data_cleaning import limpiar_retirados, limpiar_auxilios

def dash_interfaz():
    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    
    app.layout = html.Div([
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='Cargar archivos', value='tab-1'),
            dcc.Tab(label='Gráfica Radial', value='tab-2'),
        ]),
        html.Div(id='tabs-content')
    ])

    def generate_upload_space(id_prefix, num_spaces):
        nombre_variables = [
            "Retirados", "Auxilios", "Prestamos", "Empleado_Noviembre_2023_Activo",
            "Empleado_Diciembre_2023_Consolidado", "Empleado_Diciembre_2023_Activo",
            "Rotacion_Interna_Acumulado", "Finalizacion_Curso", "Solicitudes",
            "Vacantes_Totales", "Base_Data", "Enfermedades_Colaborales", "Sindicato"
        ]

        upload_spaces = []
        for i in range(num_spaces):
            upload_space = html.Div([
                html.Label(nombre_variables[i]),
                dcc.Upload(
                    id={'type': 'upload', 'index': i, 'name': nombre_variables[i]},
                    children=html.Div(['Arrastra y suelta o ', html.A('selecciona un archivo')]),
                    style={
                        'width': '100%', 'height': '60px', 'lineHeight': '60px',
                        'borderWidth': '1px', 'borderStyle': 'dashed',
                        'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
                    },
                    multiple=False
                ),
                html.Div(id={'type': 'upload-success-message', 'index': i}),
                html.Hr()
            ])
            upload_spaces.append(upload_space)
        return upload_spaces

    @app.callback(
        Output('tabs-content', 'children'),
        Input('tabs', 'value')
    )
    def render_content(tab):
        if tab == 'tab-1':
            return html.Div([
                html.H2('Carga de archivos'),
                *generate_upload_space('upload-data', 13)
            ])
        elif tab == 'tab-2':
            return html.Div([
                html.H2("Análisis"),
                dcc.Graph(id='grafico-radial')
            ])

    @app.callback(
        Output({'type': 'upload-success-message', 'index': dash.dependencies.ALL}, 'children'),
        Input({'type': 'upload', 'index': dash.dependencies.ALL}, 'contents'),
        State({'type': 'upload', 'index': dash.dependencies.ALL}, 'filename'),
        State({'type': 'upload', 'index': dash.dependencies.ALL}, 'name')
    )
    def update_output(list_of_contents, list_of_names, list_of_labels):
        if list_of_contents is not None:
            children = []
            for contents, filename, label in zip(list_of_contents, list_of_names, list_of_labels):
                if contents is not None:
                    df = parse_contents(contents)
                    df_limpio = limpiar_datos_por_tipo(df, label)
                    children.append(html.Div([
                        html.H5(f'Archivo {filename} ({label}) cargado y limpiado exitosamente')
                    ]))
            return children
        return ['']

    def parse_contents(contents):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        return df

    def limpiar_datos_por_tipo(df, tipo):
        if tipo == "Retirados":
            return limpiar_retirados(df)
        elif tipo == "Auxilios":
            return limpiar_auxilios(df)
        # Agrega más casos según sea necesario
        else:
            return df  # Devuelve el DataFrame sin cambios si no coincide ningún tipo

    if __name__ == '__main__':
        app.run_server(debug=True, port=8053)

# Ejecución de la función
dash_interfaz()
