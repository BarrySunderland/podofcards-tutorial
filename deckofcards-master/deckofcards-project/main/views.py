from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def deck(request):
    return Response({"message": "Hello, world!"})


