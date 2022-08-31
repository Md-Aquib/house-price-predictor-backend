from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import pickle
import numpy as np

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/details',
            'method': 'POST',
            'body': {'crim': "",'zn':"",'indus':"",'chas':"",
                    'nox':"",'rm':"",'age':"",'dis':"",'rad':"",
                    'tax':"",'ptratio':"",'b':"",'lstat':""},
            'description': 'Fetch details'
        },
    ]
    return Response(routes)

@api_view(['POST'])
def setdetails(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        crim = float(data['crim'])
        zn =  float(data['zn'])
        indus= float(data['indus'])
        chas= float(data['chas'])
        nox= float(data['nox'])
        rm= float(data['rm'])
        age= float(data['age'])
        dis= float(data['dis'])
        rad= float(data['rad'])
        tax= float(data['tax'])
        ptratio= float(data['ptratio'])
        b= float(data['b'])
        lstat= float(data['lstat'])

        model = open(r'house.pkl','rb')
        test = pickle.load(model)
        features= np.array([[ crim ,  zn , indus, chas , nox , 
        rm , age , dis  ,rad , tax , 
        ptratio ,b , lstat]])

        val=test.predict(features)

        return JsonResponse({'val': round(val[0]*1000,3),})


