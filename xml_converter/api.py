from rest_framework.response import Response
from rest_framework.views import APIView

from .converter import convert
from .serializers import ConvertSerializer


class ConverterView(APIView):

    serializer_class = ConvertSerializer

    def post(self, request, format=None):

        serializer = ConvertSerializer(data=request.data)

        if serializer.is_valid():

            xml_string = request.FILES['file'].read().decode('utf-8')

            result = convert(xml_string)

            return Response(result)

        else:
            return Response(
                {
                    "Success": False,
                    "Error": serializer.errors
                }
            )
