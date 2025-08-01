# validaciones.py

import re

# validaciones.py (Code moved here for direct use in the notebook)
def validar_correo(correo):
    if not correo:
        return False
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def test_correo_valido():
    assert validar_correo("usuario@dominio.com") == True

def test_correo_vacio():
    assert validar_correo("") == False

def test_correo_invalido():
    assert validar_correo("usuario.com") == False
