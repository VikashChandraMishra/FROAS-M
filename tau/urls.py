from django.urls import path
from . import views

app_name = 'tau'

urlpatterns = [
    path('<int:id>/upload', views.upload, name='upload'),
    path('<int:id>/list', views.list, name='list'),
    path('<int:id>/list_data', views.list_data, name='list_data'),
    path('<int:id>/create', views.create_class, name='create'),
]