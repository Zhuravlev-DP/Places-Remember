from django.contrib.auth import views as auth_views
from django.urls import include, path

from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='index'),
        name='logout'
    ),
    path('home/', views.home, name='home'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path(
        'memory/<int:memory_id>/',
        views.display_memory,
        name='display_memory'
    ),
]
