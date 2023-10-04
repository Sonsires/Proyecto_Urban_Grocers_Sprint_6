import requests
import configuration
import data

def obtener_token():
   respuesta = requests.post(configuration.BASE_URL + configuration.USER_ENDPOINT,
                             json=data.user)
   res_json = respuesta.json()
   auth_token = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {res_json['authToken']}"
   }
   return auth_token







def crear_kit(name):
    token = obtener_token()
    respuesta = requests.post(configuration.BASE_URL + configuration.KIT_ENDPOINT,
                              json=name,
                              headers=token
                              )

    return respuesta



