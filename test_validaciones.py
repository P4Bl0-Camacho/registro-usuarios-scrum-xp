# test_validaciones.py

from validaciones import validar_correo

def test_correo_valido():
    assert validar_correo("usuario@dominio.com") == True

def test_correo_vacio():
    assert validar_correo("") == False

def test_correo_invalido():
    assert validar_correo("usuario.com") == False
