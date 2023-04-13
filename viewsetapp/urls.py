from django.urls import path
from .views import empmixnew,token_auth,genricApi,genricApi,MyModelDetail
from . import views
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register('product',emplist,basename='employesviws')



urlpatterns = [
    # path('', include(router.urls)),
    # path('new/,empmixnew.as_view()),
    path("crud",empmixnew.as_view()),
    path("token/",token_auth.as_view()),
    path("genricApi",genricApi.as_view()),
    path("MyModelList",genricApi.as_view()),
    path("MyModelDetail/<int:pk>/",MyModelDetail.as_view())
    # path("auth/",generate.as_view())
]



# from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet)
# router.register(r'instances',views.InstanceList)                                                                            

# urlpatterns = [ 
#     path('', views.dash, name='dash'),
#     path('api/', include(router.urls)),
# ]