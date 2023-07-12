import json
import re
import wolframalpha
from decouple import config

def encontrar_variables_numeros_bien_escritos(request):
    expresion_latex=request.data.get("expresion_latex")
    numeros = expresion_latex.split(";")
    paso1 = []

    #paso 1 leer el latex 
    for num in numeros:
        digitos, base = obtener_digitos_y_bases(num.strip())
        paso1.append({"num":digitos,"base":base})

 
    ecuaciones_latex ="2+2"
    # Crea una instancia del cliente de Wolfram Alpha
    cliente_wolfram = wolframalpha.Client(config("wolframalphaID"))

    # Envía la consulta a Wolfram Alpha
    respuesta = cliente_wolfram.query(ecuaciones_latex)

    resultado = None
    for pod in respuesta.results:
        if pod["@title"] == "Integer solution":
            resultado = pod["subpod"]["plaintext"]
            break

    if resultado is not None:
       return {"Status":"True","Mensaje":"Numero bien escritos","solucion":resultado}
    else:
     return  {"Status":"false","Mensaje":"Error verificar si son numeros bien escritos"}

def obtener_digitos_y_bases(numero_latex):
    # Buscar el patrón de dígitos y base en el número LaTeX
    patron = r"\\overline{([a-zA-Z0-9]+)}_{\(([a-zA-Z0-9])\)}"
    coincidencias = re.search(patron, numero_latex)

    if coincidencias:
        digitos = coincidencias.group(1)
        base = coincidencias.group(2)
        return digitos, base
    else:
        return None, None