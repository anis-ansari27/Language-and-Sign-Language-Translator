from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("",views.text, name="text"),
    path("sign",views.sign, name="sign"),
]
