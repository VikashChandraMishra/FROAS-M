from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profiles/<int:id>', views.get_profile, name='get_profile'),
    path('profiles/<int:id>/edit', views.edit_profile, name='edit_profile'),
]