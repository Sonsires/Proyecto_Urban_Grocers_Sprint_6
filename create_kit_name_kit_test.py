
import data
import sender_stand_request as req


def test_valida_caracter_name_1_respuesta_200():
    respuesta = req.crear_kit(data.kit["prueba1"])
    res_json = respuesta.json()
    assert respuesta.status_code == 201
    assert res_json["name"] == data.kit["prueba1"]["name"]

def test_valida_caracter_name_511_respuesta_200():
    respuesta = req.crear_kit(data.kit["prueba2"])
    res_json = respuesta.json()
    assert respuesta.status_code == 201
    assert res_json["name"] == data.kit["prueba2"]["name"]

def test_invalida_caracter_name_0_respuesta_400():
    respuesta = req.crear_kit(data.kit["prueba3"])
    res_json = respuesta.json()
    assert respuesta.status_code == 400
    assert res_json["name"] == data.kit["prueba3"]["name"]

def test_invalida_caracter_name_512_respuesta_400():
    respuesta = req.crear_kit(data.kit["prueba4"])
    res_json = respuesta.json()
    assert respuesta.status_code == 400
    assert res_json["name"] == data.kit["prueba4"]["name"]

def test_valida_caracter_especiales_name_respuesta_200():
    respuesta = req.crear_kit(data.kit["prueba5"])
    res_json = respuesta.json()
    assert respuesta.status_code == 201
    assert res_json["name"] == data.kit["prueba5"]["name"]

def test_valida_caracter_espacios_name_respuesta_200():
    respuesta = req.crear_kit(data.kit["prueba6"])
    res_json = respuesta.json()
    assert respuesta.status_code == 201
    assert res_json["name"] == data.kit["prueba6"]["name"]

def test_valida_caracter_numeros_name_respuesta_200():
    respuesta = req.crear_kit(data.kit["prueba7"])
    res_json = respuesta.json()
    assert respuesta.status_code == 201
    assert res_json["name"] == data.kit["prueba7"]["name"]

def test_invalida_caracter_no_se_pasa_en_la_solicitud_name_respuesta_400():
    respuesta = req.crear_kit(data.kit["prueba8"])
    res_json = respuesta.json()
    assert respuesta.status_code == 400
    assert res_json["name"] == data.kit["prueba8"]["name"]

def test_invalida_caracter_parametro_diferente_name_respuesta_400():
    respuesta = req.crear_kit(data.kit["prueba9"])
    res_json = respuesta.json()
    assert respuesta.status_code == 400
    assert res_json["name"] == data.kit["prueba9"]["name"]


