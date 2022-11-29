from django.urls import path
from . import views

app_name = 'tau'

urlpatterns = [
    path('<int:id>/upload', views.upload, name='upload'),
    path('<int:id>/list', views.list, name='list'),
    path('<int:id>/list_data', views.list_data, name='list_data'),
    path('<int:id>/class_history', views.class_history, name='class_history'),
    path('<int:id>/list_classes', views.list_classes, name='list_classes'),
    path('<int:id>/display', views.display, name='display'),
    
    path('<int:id>/create', views.create_class, name='create'),
]