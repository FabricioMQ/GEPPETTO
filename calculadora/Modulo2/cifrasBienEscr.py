import re

def crear_restricciones(request):
    contenido=request.data
    cifras=contenido.get("cifras")
    numeros = cifras.split(";")
    restricciones = []
    incognitas = {"incognita": [], "valores": []}
    for num in numeros:
        base = num[num.index('(') + 1:num.index(')')]
        digitos = num[0:num.index('(')]
        expresiones = construir_expresiones(digitos, base)
        for exp in expresiones:
            restricciones.append(exp)
        incognitas = agregar_incognitas(incognitas, digitos)
    incognitas = calcular_incognitas(restricciones, incognitas)
    valores_incognitas=ordenar_valores(incognitas, restricciones)
    return {"Status":"True","Mensaje":f"Los valores de las incognitas son:" ,"Incognitas":valores_incognitas}


def construir_expresiones(elementos, valor):
    expresiones = []
    for elemento in elementos:
        expresion = f"{elemento}<{valor}"
        expresiones.append(expresion)
    return expresiones


def agregar_incognitas(incognitas, elementos):
    for elemento in elementos:
        if elemento.isalpha() and elemento not in incognitas["incognita"]:
            incognitas["incognita"].append(elemento)
            incognitas["valores"].append(None)
    return incognitas


def calcular_incognitas(restricciones, incognitas):
    for restriccion in restricciones:
        coincidencias = re.findall(r'\d+', restriccion)
        numLetra = re.search(r'\d.*[a-zA-Z]|[a-zA-Z].*\d', restriccion)
        if len(coincidencias) > 0 and numLetra:
            if restriccion.index(coincidencias[0]) == 0:
                if incognitas["valores"][incognitas["incognita"].index(restriccion[2])] is None or int(coincidencias[0]) > incognitas["valores"][incognitas["incognita"].index(restriccion[2])]:
                    incognitas["valores"][incognitas["incognita"].index(
                        restriccion[2])] = int(coincidencias[0])+1
            else:
                if incognitas["valores"][incognitas["incognita"].index(restriccion[0])] is None or int(coincidencias[0]) < incognitas["valores"][incognitas["incognita"].index(restriccion[0])]:
                    incognitas["valores"][incognitas["incognita"].index(
                        restriccion[0])] = int(coincidencias[0])-1

    return incognitas


def ordenar_valores(incognitas, restricciones):
    print('order ', incognitas)
    count = 0
    while None in incognitas["valores"] or int(count) <= 0:
        count = count+1
        for restriccion in restricciones:
            coincidencias = re.findall(r'\d+', restriccion)
            if not coincidencias:
                valor1 = incognitas["valores"][incognitas["incognita"].index(restriccion[0])]
                valor2 = incognitas["valores"][incognitas["incognita"].index(restriccion[2])]
                if valor1 != None or valor2 != None:
                    if valor1 is None or valor2 is None:
                        if (valor1 is None):
                            incognitas["valores"][incognitas["incognita"].index(restriccion[0])] = int(valor2)-1
                        else:
                            incognitas["valores"][incognitas["incognita"].index(restriccion[2])] = int(valor1)+1
                        count = 0
                    else:
                        if int(valor1) > int(valor2) or int(valor1) == int(valor2):
                            if int(valor1) > int(valor2):
                                incognitas["valores"][incognitas["incognita"].index(
                                    restriccion[0])] = valor2
                                incognitas["valores"][incognitas["incognita"].index(
                                    restriccion[2])] = valor1
                            else:
                                incognitas["valores"][incognitas["incognita"].index(restriccion[2])] = int(valor1)+1
                            count = 0
        calcular_incognitas(restricciones, incognitas)
    return incognitas


    # Obtener las cifras del usuario
cifras = input(
    "Ingrese las cifras bien escritas separadas por punto y coma (;): ")
crear_restricciones(cifras)
