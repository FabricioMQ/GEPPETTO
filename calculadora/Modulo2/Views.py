from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Resolver import encontrar_variables_numeros_bien_escritos as relatex
from .cifrasBienEscr import crear_restricciones as buscar_valores


@api_view([ 'POST'])
def my_view(request):
    methods = {
      'POST':lambda: relatex(request),
      'POST':lambda: buscar_valores(request)

    }
    response_data = methods[request.method]()
    return Response(response_data)