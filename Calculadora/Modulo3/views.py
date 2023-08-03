from rest_framework.decorators import api_view
from rest_framework.response import Response
from .aiResolver import resolver


@api_view([ 'POST'])
def problemasAI(request):
    methods = {
     'POST':lambda: resolver(request)
    }
    response_data = methods[request.method]()
    return Response(response_data)