
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='blog-home'),
    path('home/',views.index, name='index'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('service/', views.service, name='blog-service'),
    path('display/',views.stdisplay,name="stdisplay"),               #app/index
    path('create/',views.stinsert,name="stinsert"),           #app/create
    path('edit/<int:id>',views.stedit,name="stedit"),        #app/edit
    path('update/<int:id>',views.stupdate,name="stupdate"),   #app/
    path('delete/<int:id>',views.stdel,name="stdel"), 
    path("js/",views.jsondata,name = "jsondata"),     
    path("graph/",views.graph, name='graph'), 
    path("dashboard/",views.dashboard, name='dashboard'), 
    path("page11/",views.page11, name='page11'), 
    path("page12/",views.page12, name='page12'), 
    path("page13/",views.page13, name='page13'), 
    path("charts/",views.charts, name='charts'), 
 
   path('display1/',views.stdisplay1,name="stdisplay1"), 
   path('create1/',views.stinsert1,name="stinsert1"),           #app/create
    path('edit1/<int:id>',views.stedit1,name="stedit1"),        #app/edit
    path('update1/<int:id>',views.stupdate1,name="stupdate1"),   #app/
    path('delete1/<int:id>',views.stdel1,name="stdel1"), 



    
    
    
]