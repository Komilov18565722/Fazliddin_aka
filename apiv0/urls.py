from django.urls import path
from .views import CreateList, DeleteList, UpdateList
urlpatterns = [
    path('create/', CreateList.as_view()),
    path('update/', UpdateList.as_view()),
    path('delete/', DeleteList.as_view()),
]
