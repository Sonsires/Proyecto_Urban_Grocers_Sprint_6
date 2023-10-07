import data
import sender_stand_request

def validacion_positiva(name):
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body[name])
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] != ""
    assert kit_response.json()["name"] == data.kit_body[name]["name"]
    print("Resultado de la creación del kit:", kit_response.json())

def validacion_negativa(name):
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body[name])
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] != ""
    print(kit_response.status_code)



def test_create_kit_name_1_letter_result_201():
    validacion_positiva('prueba1')
    print(test_create_kit_name_1_letter_result_201)

def test_create_kit_name_511_letter_result_201():
    validacion_positiva('prueba2')
    print(test_create_kit_name_511_letter_result_201)

def test_create_kit_name_caracther_letter_result_201():
    validacion_positiva('prueba5')
    print(test_create_kit_name_caracther_letter_result_201)

def test_create_kit_name_space_letter_result_201():
    validacion_positiva('prueba6')
    print(test_create_kit_name_space_letter_result_201)

def test_create_kit_name_number_letter_result_201():
    validacion_positiva('prueba7')
    print(test_create_kit_name_number_letter_result_201)


def test_create_kit_name_vacio_letter_result_400():
    validacion_negativa('prueba3')
    print(test_create_kit_name_vacio_letter_result_400)

def test_create_kit_name_512_letter_result_400():
    validacion_negativa('prueba4')
    print(test_create_kit_name_512_letter_result_400)

def test_create_kit_name_no_se_pasa_la_solicitud_letter_result_400():
    validacion_negativa('prueba8')
    print(test_create_kit_name_no_se_pasa_la_solicitud_letter_result_400)


def test_create_kit_name_parametro_diferente_letter_result_400():
    validacion_negativa('prueba9')
    print(test_create_kit_name_parametro_diferente_letter_result_400)

