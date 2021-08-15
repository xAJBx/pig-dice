from django.urls import path
from . import views

app_name = 'vinyls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vinyls_id>', views.detail, name='detail')
    ]
