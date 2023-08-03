from rest_framework.decorators import api_view
from rest_framework.response import Response
from .convertir import conv



@api_view([ 'POST'])
def ConverView(request):
    methods = {
        'POST':lambda:  conv(request)
    }
    response_data = methods[request.method]()
    return Response(response_data)