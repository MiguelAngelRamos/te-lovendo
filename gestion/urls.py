from django.urls import path
from .views import list_productos, login

urlpatterns = [
    path('', login, name = 'login'),
    path('productos/', list_productos, name = 'lista_productos')
]
