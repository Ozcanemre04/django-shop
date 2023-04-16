from django.urls import path,include
from accounts.views import index_view
from rest_framework.decorators import authentication_classes

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
     path('index/',index_view,name='index_view'),
]
