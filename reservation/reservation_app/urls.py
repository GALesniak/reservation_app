from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.room_form, name='room_insert'),
    path('<int:id>/', views.room_form, name='room_update'),
    path('delete/<int:id>/', views.room_delete, name='room_delete'),
    path('list/', views.room_list, name='room_list'),
    path('details/<int:id>', views.room_details, name='room_details'),

]
