from django.urls import path
from.import views

urlpatterns = [
    path('',views.details2,name='product'),
    path('cmd/',views.comment,name='comment'),
    
]
