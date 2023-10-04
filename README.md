# Sprint_6_Pruebas Automatizadas para Urban Grocers
Este proyecto tiene como objetivo automatizar las pruebas de creación de kits de productos en la aplicación Urban Grocers. Las pruebas verifican diferentes escenarios según una lista de comprobación específica para garantizar que la funcionalidad de creación de kits funcione correctamente.

## Instrucciones

1. Clona este repositorio en tu máquina local.

2. Asegúrate de tener Python y las bibliotecas necesarias instaladas.

3. Ejecuta las pruebas con el siguiente comando:

   ```bash
   pytest create_kit_name_kit_test.py


## Requisitos

- Python 3.9.13
- Biblioteca `sender_stand_request.py`
- Biblioteca `create_kit_name_kit_test.py`

## Información Adicional

Asegúrate de configurar las rutas y URL de la API de Urban Grocers en `configuration.py` y de manejar adecuadamente los errores en el código. Para obtener más información, consulta la documentación de la API en <https://86df1590-e83d-4441-a16d-4c39eeaa5c8f.serverhub.tripleten-services.com/docs/>.

## Ejemplo de Uso

Aquí tienes un ejemplo de cómo ejecutar una prueba específica:

```bash
pytest create_kit_name_kit_test.py::test_valida_caracter_name_1_respuesta_200


