import re

def buscar_valores(request):
    try:
        expresion_latex=request.data.get("expresion_latex")
        # formato --> 1a1(4);bb(c);2c(a)
        resultado=crear_restricciones(expresion_latex)
        restricciones = resultado[0]
        incognitas = resultado[1]
        incognitas = calcular_incognitas(restricciones, incognitas)
        print(ordenar_valores(incognitas, restricciones))
       # return ordenar_valores(incognitas, restricciones)
    except Exception as ex:
        print(ex)


def crear_restricciones( expresion_latex):
    try:
        numeros =  expresion_latex.split(";")
        restricciones = []
        incognitas = {"incognita": [], "valores": []}
        for num in numeros:
            base = num[num.index('(') + 1:num.index(')')]
            digitos = num[0:num.index('(')]
            restricciones = construir_expresiones(digitos, base, restricciones)
            incognitas = agregar_incognitas(incognitas, digitos)
        return restricciones,incognitas
    except Exception as ex:
        print(ex)
        
        
#Construye las expresiones de las restricciones 1<a
def construir_expresiones(elementos, valor, restricciones):
    try:
        for elemento in elementos:
            expresion = f"{elemento}<{valor}"
            restricciones.append(expresion)
        return restricciones
    except Exception as ex:
        print('ex')

#Busca las incognitas y las a agrega a un diccionario con un atributo valor =None
def agregar_incognitas(incognitas, elementos):
    try:
        for elemento in elementos:
            if elemento.isalpha() and elemento not in incognitas["incognita"]:
                incognitas["incognita"].append(elemento)
                incognitas["valores"].append(None)
        return incognitas
    except Exception as ex:
        print('ex')

#Calcula los posibles valores con las restricciones que contienen numeros
def calcular_incognitas(restricciones, incognitas):
    try:
        for restriccion in restricciones:
            coincidencias = re.findall(r'\d+', restriccion)
            numLetra = re.search(r'\d.*[a-zA-Z]|[a-zA-Z].*\d', restriccion)
            if len(coincidencias) > 0 and numLetra:
                if restriccion.index(coincidencias[0]) == 0:
                    if incognitas["valores"][incognitas["incognita"].index(restriccion[2])] is None or int(coincidencias[0]) > incognitas["valores"][incognitas["incognita"].index(restriccion[2])]:
                        incognitas["valores"][incognitas["incognita"].index(restriccion[2])] = int(coincidencias[0])+1
                else:
                    if incognitas["valores"][incognitas["incognita"].index(restriccion[0])] is None or int(coincidencias[0]) < incognitas["valores"][incognitas["incognita"].index(restriccion[0])]:
                        incognitas["valores"][incognitas["incognita"].index(restriccion[0])] = int(coincidencias[0])-1
        return incognitas
    except Exception as ex:
        print('ex')

#Se recorren las restricciones donde se compara las incognitas
def ordenar_valores(incognitas, restricciones):
    try:
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
    except Exception as ex:
        print(ex)


    # Obtener las cifras del usuario
"""   
expresion_latex = input(
    "Ingrese las cifras bien escritas separadas por punto y coma (;): ")
buscar_valores(expresion_latex)

"""
