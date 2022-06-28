from django.urls import path
from PizzeriaManuel import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('pizzas', views.pizzas, name="Pizzas"),
    path('formulario', views.crearPizza, name="Formulario"),
    path('buscarPizza',views.buscarPizza, name="BuscarPizza"),
    path('buscar/',views.buscar)

]