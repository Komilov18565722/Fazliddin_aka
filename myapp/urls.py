from django.urls import path
from .views import Add, AdminView, Delete, HomeView, Update, index
urlpatterns = [
    path('', HomeView.as_view()),
    path('reg/', index),
    path('myadmin/', AdminView.as_view()),
    path('add/', Add.as_view()),
    path('<pk>/update/', Update.as_view()),
    path('<pk>/delete/', Delete.as_view()),

]
