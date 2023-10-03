from django.shortcuts import render
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({'messsage':'Insert New Invoice'})
    else:
        return Response({'message':'Invalid Response'})


@api_view(['PUT','GET','DELETE'])
def invoice_detail(request,pk):
    if request.method == 'GET':
        return Response({"type":"Action to be performed on single request."})
    elif request.method == 'PUT':
        return Response({'type':'PUT','message':'Update Request'})
    elif request.method == 'DELETE':
        return Response({'type':'delete','message':'Delete Request'})
    else:
        return Response({'type':'None','message':'Invalid Request'})