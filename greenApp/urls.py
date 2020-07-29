from django.urls import path
from . import views
urlpatterns = [
    #giving path to every page to its releted view
    # path('',views.login,name='login'),
    path('',views.status,name='status'),
    path('soilmoisture',views.soilmoisture,name='soilmoisture'),
    path('humtemp',views.humtemp,name='humtemp'),
    path('recv_data',views.recv_data),
    path('history',views.history,name='history'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('logout',views.logout,name='logout'),
    
    
]