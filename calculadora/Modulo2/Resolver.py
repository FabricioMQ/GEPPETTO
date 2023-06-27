from sympy import symbols, solve 
import re

def encontrar_variables_numeros_bien_escritos(request):
    expresion_latex=request.data.get("expresion_latex")
    numeros = expresion_latex.split(";")
    paso1 = []
    incognitas=[]#es temporal

    #paso 1 leer el latex
    for num in numeros:
        digitos, base = obtener_digitos_y_bases(num.strip())
        paso1.append({"num":digitos,"base":base})
    
    #paso 2 hacer la operacion logica
    #en este apartado se debe que crear la logica de cada num
    for num in paso1:
      if num["num"] is not None and num["base"] is not None:
        digitos = num["num"]
        base = num["base"]

        # Verificar si los dígitos contienen letras o son variables
        if re.search(r"[a-z]", digitos):
            incognitas.append(digitos)

        # Verificar si la base contiene letras o es una variable
        if re.search(r"[a-z]", base):
            incognitas.append(base)

        # Verificar si la base es un número válido
        if base.isdigit():
            if 2 <= int(base) <= 62:
                incognitas.append(base)

    return incognitas

def obtener_digitos_y_bases(numero_latex):
    # Buscar el patrón de dígitos y base en el número LaTeX
    patron = r"\\overline{([a-fA-F0-9]+)}_{\(([a-fA-F0-9])\)}"
    coincidencias = re.search(patron, numero_latex)

    if coincidencias:
        digitos = coincidencias.group(1)
        base = coincidencias.group(2)
        return digitos, base
    else:
        return None, None