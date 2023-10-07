
import configuration
import requests
import data

def post_new_user():
    respuesta = requests.post(configuration.URL_SERVICE + configuration.USER_ENDPOINT, json=data.user_body)
    respuesta_json = respuesta.json()
    return respuesta_json['authToken']

def get_new_user_token():
    auth_token = post_new_user()
    authorization = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {auth_token}'
    }
    return authorization

authorization_header = get_new_user_token()
print(authorization_header)

def post_new_client_kit(name):
    respuesta= requests.post(configuration.URL_SERVICE + configuration.KIT_ENDPOINT,
                             json=name,
                             headers=authorization_header
                             )
    return respuesta











