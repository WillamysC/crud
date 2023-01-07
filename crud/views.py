from crud import serialize
from crud.models import DetailsModel
from crud.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class DetailsTable(APIView):
    def get(self, request):
        detailsObj = DetailsModel.objects.all()
        dlSerializeObj = DetailsSerializer(detailsObj, many=True)

        return Response(dlSerializeObj.data)
