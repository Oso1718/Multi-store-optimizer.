import scrapy
from urllib.parse import quote
import unicodedata
import re


class GranBodegaSearchSpider(scrapy.Spider):
    
    name = "gran_bodega_search" # Nombre del spider
    allowed_domains = ["lagranbodega.com.mx"] # Dominio permitido para el spider

    # El constructor del spider para recibir la lista de productos a buscar
    def __init__(self, productos_a_buscar=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.productos_a_buscar = productos_a_buscar or []

    def normalizar(self, texto):
        # texto = texto.lower()

        # quitar acentos
        texto = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )

        # quitar espacios extras
        texto = re.sub(r"\s+", " ", texto).strip()

        return texto

    
    def coincide_busqueda(self, nombre_producto, busqueda):
        nombre = self.normalizar(nombre_producto)
        busqueda = self.normalizar(busqueda)

        palabras = busqueda.split()

        # Requiere que al menos la mitad de las palabras coincidan
        coincidencias = sum(1 for palabra in palabras if palabra in nombre)

        return coincidencias >= max(1, len(palabras) // 2)



    def start_requests(self):
        for producto in self.productos_a_buscar:
            query = quote(producto)
            url = (
                f"https://www.lagranbodega.com.mx/{query}"
                f"?&utmi_p=_&utmi_pc=BuscaFullText&utmi_cp={query}"
            )

            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"busqueda": producto}
            )

    def parse(self, response):

        busqueda_original = response.meta["busqueda"]

        productos = response.css("article.article--secondary")

        for p in productos:
            nombre = p.css("h6 a::text").get()
            precio = p.css("span.newPrice strong::text").get()
            url = p.css("h6 a::attr(href)").get()
            url = response.urljoin(url)


            if not nombre or not precio:
                continue

            if self.coincide_busqueda(nombre, busqueda_original):
                precio = re.sub(r"[^\d.]", "", precio)
                precio = float(precio)
                #precio = float(precio.replace("$", "").strip())

                yield {
                    "busqueda": busqueda_original,
                    "producto": nombre,
                    "precio": precio,
                    "tienda": "La Gran Bodega",
                    "url": url
                }

