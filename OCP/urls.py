from django.urls import path
from OCP import views



   
urlpatterns = [
    #path("", views.home, name="home"),
    path('', views.HomePage,name="home"),
    #path("people/", PersonListView.as_view()),
    #path("info/", InfoListView.as_view()),    
    path('insert_details', views.insert,name="insert"),
    path('update_details', views.update_details,name="update_details"),
    path('delete_details', views.delete_details,name="delete_details"),
    path('insert_table', views.insert_table,name="insert_table"),
    path('simulate', views.simulate,name="simulate"),
]