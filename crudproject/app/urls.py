from django.urls import path
from .import views
urlpatterns = [
    path('new/',views.create,name='create'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('',views.read,name='read')

]
