import data
import sender_stand_request as req

def validacion_positiva(kit_body):
    kit_response = req.crear_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


def validacion_negativa(name):
    kit_response = req.crear_kit(name)
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] != ""




def test_create_kit_name_1_letter_result_201():
    validacion_positiva(data.kit_body['prueba1'])


def test_create_kit_name_511_letter_result_201():
    validacion_positiva(data.kit_body['prueba2'])


def test_create_kit_name_caracther_letter_result_201():
    validacion_positiva(data.kit_body['prueba5'])


def test_create_kit_name_space_letter_result_201():
    validacion_positiva(data.kit_body['prueba6'])


def test_create_kit_name_number_letter_result_201():
    validacion_positiva(data.kit_body['prueba7'])



def test_create_kit_name_vacio_letter_result_400():
    validacion_negativa(data.kit_body['prueba3'])


def test_create_kit_name_512_letter_result_400():
    validacion_negativa(data.kit_body['prueba4'])


def test_create_kit_name_no_se_pasa_la_solicitud_letter_result_400():
    validacion_negativa(data.kit_body['prueba8'])



def test_create_kit_name_parametro_diferente_letter_result_400():
    validacion_negativa(data.kit_body['prueba9'])

