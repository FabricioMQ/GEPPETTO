from rest_framework.decorators import api_view
from rest_framework.response import Response
from .cifrasBienEscr import crear_restricciones as buscar_valores


@api_view([ 'POST'])
def my_view(request):
    methods = {
      'POST':lambda: buscar_valores(request)
    }
    response_data = methods[request.method]()
    return Response(response_data)