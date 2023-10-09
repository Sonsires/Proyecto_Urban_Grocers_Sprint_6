

import requests
import configuration
import data

def obtener_token():
    respuesta = requests.post(configuration.URL_SERVICE + configuration.USER_ENDPOINT,
                              json=data.user)
    resp_json = respuesta.json()
    return resp_json['authToken']

auth_token = obtener_token()
data.authorization["Authorization"] = f'Bearer {auth_token}'


def crear_kit(name):

    respuesta = requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                              json=name,
                              headers=data.authorization)
    return respuesta










