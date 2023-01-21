from django.urls import path,include
from . import views

urlpatterns=[

    path('register',views.register,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('news/', views.news, name='news'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('footer/',views.footer,name='footer'),
    path('logout',views.logout,name='logout'),
]