from crud import serialize
from crud.models import DetailsModel
from crud.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class DetailsTable(APIView):
    def get(self, request):
        detailsObj = DetailsModel.objects.all()
        dlSerializeObj = DetailsSerializer(detailsObj, many=True)

        return Response(dlSerializeObj.data)

    def post(self, request):
        serializeObj = DetailsSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(serializeObj.data, status=status.HTTP_201_CREATED)
        return Response(serializeObj.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsUpdate(APIView):

    def get_object(self, pk):
        try:
            return DetailsModel.objects.get(pk=pk)
        except DetailsModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detailObj = self.get_object(pk)
        serializeObj = DetailsSerializer(detailObj)
        return Response(serializeObj.data)

    def post(self, request, pk):
        detailObj = self.get_object(pk)
        serializeObj = DetailsSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(serializeObj.data)
        return Response(serializeObj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        detailObj = self.get_object(pk)
        detailObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
