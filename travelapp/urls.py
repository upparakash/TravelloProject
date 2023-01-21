from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='fun'),
    # path('destination/',views.destination,name='destination'),
    path('destination/',views.search,name='search'),
    path('fullview/<int:id>/',views.fullview,name="fullview"),
    path('about/',views.About,name='About')
]