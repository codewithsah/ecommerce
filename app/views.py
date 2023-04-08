# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from .serializers import CartSerializer
from .models import CartItem
# Create your views here.
class CartNew (APIView):
  def post(self,request):
    serializers=CartSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({"status":"success","data":serializers.data},status=status.HTTP_200_OK)
    else:
        return Response({"status":"error","data":serializers.data},status=status.HTTP_400_BAD_REQUEST)


