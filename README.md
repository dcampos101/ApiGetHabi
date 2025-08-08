# ApiGetHabi
Prueba técnica backend Python
Para el desarrollo del API se utilizaran las siguientes herramientas y librerias:
-Jupyter Notebooks: creación, edicion y compilacion de codigo y librerias.
-FastAPI: para conexión y consulta del API.

Desarrollo:
1. Definir los estados posibles de los inmuebles
2. Definir el modelo de respuesta del API con los datos que va retornar al consultar y filtrar.
3. Creacion de un JSON para simular la información almacenada en BD.
4. Crear la funcion principal donde se definan los parametros de entrada para la consulta y filtro de información en el API.
5. Crear ciclo para que devuelva toda la informacion por los estados permitidos a excepcion de reservado
6. Creacion de condiciones para filtrado por estado, ciudad y anio.
7. Ejecucion de pruebas con FastAPI, validando cada uno de los filtros creados.

Instalcion de libreria fastapi:
pip install fastapi uvicorn sqlalchemy mysql-connector-python nest-asyncio 
