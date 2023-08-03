from rest_framework.decorators import api_view
from rest_framework.response import Response
from .cifrasBienEscr import crear_restricciones


@api_view([ 'POST'])
def numbes(request):
    methods = {
      'POST':lambda: crear_restricciones(request)
    }
    response_data = methods[request.method]()
    return Response(response_data)