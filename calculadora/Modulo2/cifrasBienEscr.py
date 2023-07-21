import re
import wolframalpha
from decouple import config

def crear_restricciones(request):
    try :
        contenido=request.data
        cifras=contenido.get("cifras")
        numeros = cifras.split(";")
        restricciones = []
        for num in numeros:
            base = num[num.index('(') + 1:num.index(')')]
            digitos = num[0:num.index('(')]
            restricciones.extend(construir_expresiones(digitos, base))
        return wolframalphaSend(';'.join(restricciones))
    except Exception as e:
       return  {"Status":"false","Mensaje":"Error verificar si son numeros bien escritos,comprobar el formato"}
    

def construir_expresiones(elementos, valor):
    expresiones = []
    for elemento in elementos:
        if elemento.isalpha() or valor.isalpha():
          expresion = f"{elemento}<{valor}"
          expresiones.append(expresion)
    return expresiones


def wolframalphaSend(expresion):
    # Crea una instancia del cliente de Wolfram Alpha
    cliente_wolfram = wolframalpha.Client(config("wolframalphaID"))
    # Envía la consulta a Wolfram Alpha
    respuesta = cliente_wolfram.query(expresion)
    resultado = None
    for pod in respuesta.results:
        if pod["@title"] == "Integer solution":
            resultado = pod["subpod"]["plaintext"]
            break
    if resultado is not None:
       return {"Status":"True","Mensaje":"Numero bien escritos","solucion":resultado}
    else:
       return  {"Status":"false","Mensaje":"Error verificar si son numeros bien escritos"}