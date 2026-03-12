# Separacion de las listas de productos recibidos para mejorar la busqueda.
import re

### Funciones
import unicodedata

def normalizar(texto: str) -> str:
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode()

    return texto

def separar_productos(texto):
    """
    Convierte:
    'huevo, leche, carne'
    en:
    ['huevo', 'leche', 'carne']
    """

    if not texto:
        return []

    # separar por coma
    productos = texto.split(",")

    # limpiar espacios y normalizar
    productos = [normalizar(p.strip()) for p in productos if p.strip()]

    return productos
###
'''
def parse_products(input_text: str) -> list[str]:
    """
    Convierte:
    'huevo, leche, carne'
    'huevo leche carne'
    'huevo; leche'
    -> ['huevo', 'leche', 'carne']
    """

    if not input_text:
        return []

    # separar por coma, punto y coma o espacio
    productos = re.split(r"[,\n;]+", input_text)

    # limpiar espacios y lowercase
    products = [
        p.strip().lower()
        for p in productos
        if p.strip()
    ]

    return products
'''