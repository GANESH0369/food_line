from django.http import HttpResponse
from django.shortcuts import render
# from rest_framework import viewsets
from .models import employesviws
from .serilizers import seriempoly,serilogin
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
# from django.contrib.auth import authenticate
from rest_framework import status

# Create your views here.
# class emplist(viewsets.ModelViewSet):
#     queryset=employesviws.objects.all()
#     serilizer_class=seriempoly
    

# class empmix(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=employesviws.objects.all()
#     serializer_class=seriempoly
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)

class empmixnew(mixins.UpdateModelMixin,
                mixins.ListModelMixin,
             mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.DestroyModelMixin,
             generics.GenericAPIView):
    queryset=employesviws.objects.all()
    serializer_class=seriempoly
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    def getid(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
        # return HttpResponse()
    
        

class token_auth(APIView):
    def post(self, request):
        serializer = serilogin(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data['username'],
                                            password=serializer.validated_data['password'])
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(serializer.errors, status=400)


class genricApi(generics.ListCreateAPIView):
    queryset = employesviws.objects.all()
    serializer_class = seriempoly

class MyModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employesviws.objects.all()
    serializer_class = seriempoly


    
#     def post(self, request, *args, **kwargs):
#         # import pdb;pdb.set_trace()
#         name = request.data.get('name')
#         empid = request.data.get('empid')
#         try:
#             employee = employesviws.objects.get(name=name,empid=empid)
#             if employee is not None:
#                 user = authenticate(name=name, empid=empid)
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#         except employesviws.DoesNotExist:
#              return Response({'Message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

# class generate(APIView):
#     def post(self, request, *args, **kwargs):
#         name = request.data.get('name')
#         empid = request.data.get('empid')
#         try:
#             # employee = employesviws.objects.get(name=name, empid=empid)
#             # employee = employesviws.objects.filter(name=name)
#             user = authenticate(name=name,empid=empid)
#             if user is not None:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#         except employesviws.DoesNotExist:
#             return Response({'Message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response({'Message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)