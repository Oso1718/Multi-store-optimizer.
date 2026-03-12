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
    Convierte listas complejas como:
    'huevo, leche, carne'
    en items separados:
    ['huevo', 'leche', 'carne']
    """

    if not texto:
        return []

    # separar por coma
    productos = texto.split(",")

    # limpiar espacios y normalizar
    productos = [normalizar(p.strip()) for p in productos if p.strip()]

    return productos
