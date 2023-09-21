from django.urls import path
from .views import index_home, fale_conosco, produto

urlpatterns = [
    path('', index_home, name='index'),
    path('faleconosco/', index_home, name='faleconosco'),
    path('produto/', produto, name='produto'),
]











