import re
import sympy as sp

def resolver_ecuacion_latex(request):
    ecuacion = request.data.get("expresion_latex")

    expresiones = [
        "\\overline{c42}_{(8)}",
        "\\overline{43}_{(a)}",
        "\\overline{a5}_{(b)}",
        "\\overline{b42}_{(c)}"
    ]

    resultados = []

    for expresion in expresiones:
        # Extraer el numeral y la base de la expresión
        numeral, base = re.findall(r"\\overline{(.+?)}_{\((.+?)\)}", expresion)[0]

        # Obtener las incógnitas y la base en orden ascendente
        incognitas = sorted(list(set(re.findall(r"([a-z])", expresion))))
        base_valor = ord(base) - ord('a') + 1

        # Crear los símbolos para las incógnitas
        symbols = [sp.Symbol(incognita) for incognita in incognitas]

        # Obtener los valores máximos y mínimos permitidos para las incógnitas
        max_valores = [base_valor - i - 1 for i in range(len(incognitas))]
        min_valor = 1

        # Construir la lista de restricciones para las incógnitas
        restricciones = [sp.And(incognita < max_val, incognita >= min_valor)
                         for incognita, max_val in zip(symbols, max_valores)]

        # Construir la expresión simbólica
        expr = 0
        for i, digit in enumerate(reversed(numeral)):
            if digit.isdigit():
                digit_value = int(digit)
            else:
                digit_value = ord(digit.lower()) - ord('a') + 10
            expr += digit_value * base_valor**i

        # Resolver la expresión simbólicamente utilizando solve_poly_system
        sistema_ecuaciones = [expr - incognita for incognita in symbols]
        resultado = sp.solve_poly_system(sistema_ecuaciones)

        # Filtrar los resultados que satisfacen las restricciones
        resultados_validos = []
        for solucion in resultado:
            if all(restric.subs(zip(symbols, solucion)) for restric in restricciones):
                resultados_validos.append(solucion)

        # Agregar el resultado a la lista de resultados
        resultados.append(resultados_validos)

    # Imprimir los resultados
    for expresion, resultado in zip(expresiones, resultados):
        print(f"El resultado de {expresion} es: {resultado}")

    return resultados
