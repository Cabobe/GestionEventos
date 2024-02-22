# GestionEventos
API RESTful utilizando Python para una plataforma de gestión de eventos.
Desarrollado desde entorno Visual Studio Code.

Carpeta Scripts base de datos
ScriptsDB

Archivo de requisitos:
requeriments.txt

Archivo con datos de conexion a Postgres y Endpoint Georeferenciacion (LocationIQ):
.env

Carpeta de codigo fuente: 
src

Localhost utilizado:
http://127.0.0.1:5000
___________________________________________________________________________________________

Comandos usados Terminal Visual Studio Code


instalacion de componentes
pip install flask flask-cors psycopg2 python-decouple python-dotenv requests

Lista de paquetes
pip freeze 

Crear archivo de dependencias
pip freeze > requirements.txt

Creacion de entorno virtual
python -m venv venv

Iniciar entorno
venv\Scripts\activate.bat

Ejecucion
python .\src\app.py

___________________________________________________________________________________________

Datos conexion a base de datos:
PG_SQL_HOST=localhost
PG_SQL_PORT=5432
PG_SQL_DATABASE=postgres
PG_SQL_USER=usr_gestion
PG_SQL_PASSWORD=Colombia2024
Version de Postgres usada: Postgres SQL V.15


Datos conexion a Endpoint Georeferenciacion (LocationIQ)
GEOREF_KEY=pk.3d8fc6948f51ea23ad0201ebc1d32c04
GEOREF_URL_REVERSE=https://us1.locationiq.com/v1/reverse?
GEOREF_URL_NEARBY=https://us1.locationiq.com/v1/nearby?
Documentacion de uso del endpoint : https://docs.locationiq.com/reference/search

___________________________________________________________________________________________

Metodos:

Listar todos los eventos
GET
http://127.0.0.1:5000//api/GestionEventos

Listar un evento por id
GET
http://127.0.0.1:5000//api/GestionEventos/id
Donde id corresponde al id_evento de la tabla Eventos

Insertar un nuevo evento
POST
http://127.0.0.1:5000//api/GestionEventos/addEvento
JSon de insumo
    {
        "nombre_evento": "Reunion de Provedores",
        "descripcion": "Reunion de todos los Provedores",
        "fecha": "2024-02-27",
        "hora": "10:00",
        "latitud": "5",
        "longitud": "6"    
    }

Actualizar un nuevo evento
POST
http://127.0.0.1:5000//api/GestionEventos/updateEvento
JSon de insumo
    {
        "id_evento": "1",
        "nombre_evento": "Reunion de Accionistas",
        "descripcion": "Reunion de Accionistas",
        "fecha": "2024-02-28",
        "hora": "8:00",
        "latitud": "4.616425853054133",
        "longitud": "-74.06891626731635"
    }

Eliminar un evento
POST
http://127.0.0.1:5000//api/GestionEventos/deleteEvento
Json de insumo
    {
        "id_evento": "2"    
    }

Consultar georeferenciacion inversa (direccion y sitios cercanos)
POST
http://127.0.0.1:5000/api/GestionEventos/GeoRefInv
Json de insumo
{
    "latitud": "4.631866206568354",
    "longitud": "-74.07117711827533"
}