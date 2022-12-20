from django.urls import path
from .views import Noticialv

urlpatterns = [
    path('noticias',Noticialv.as_view())
]
