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
- Utiliza dos parámetros en la función para crear un nuevo kit de producto: kit_body (el cuerpo de solicitud) y auth_token (el token de autenticación).

## Funciones de aserción
Hemos incorporado funciones de aserción para resultados válidos e inválidos en las pruebas. Estas funciones se encuentran en el archivo create_kit_name_kit_test.py y son útiles para verificar los resultados de las solicitudes HTTP. Aquí están las funciones y cómo utilizarlas:
 
## assert_valid_result(response_json, test_name)
 

Esta función se utiliza para verificar resultados válidos. Verifica que el código de estado sea 201 y que el mensaje en el cuerpo de respuesta coincida con el campo 'name' en el cuerpo de solicitud.

## Ejemplo de uso:

```bash
response = create_kit(kit_body_1, auth_token)
response_json = response.json()
assert_valid_result(response_json, "prueba1")
```
## assert_invalid_result(response_json, test_name, expected_error_code)

Esta función se utiliza para verificar resultados inválidos. Verifica que el código de estado sea 400 y que el código de error en el cuerpo de respuesta coincida con el código esperado.

## Ejemplo de uso:

```bash
response = create_kit(kit_body_3, auth_token)
response_json = response.json()
assert_invalid_result(response_json, "prueba3", expected_error_code=400)
```
## Aquí tienes ejemplos de cómo ejecutar pruebas específicas:

```bash
pytest create_kit_name_kit_test.py::test_create_kit_name_1_letter_result_201
```


## Información Adicional

Asegúrate de configurar las rutas y URL de la API de Urban Grocers en `configuration.py` y de manejar adecuadamente los errores en el código. Para obtener más información, consulta la documentación de la API en <https://86df1590-e83d-4441-a16d-4c39eeaa5c8f.serverhub.tripleten-services.com/docs/>.




