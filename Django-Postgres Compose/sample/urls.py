from django.contrib import admin
from django.urls import path, include
# importing from app folder, the view file
from .views import add_person, list_person

urlpatterns = [
    path('admin/', admin.site.urls),
    # for the home function in the view file
    path('', list_person, name="person_list"),
    # for the create function in the view file
    path('add/', add_person, name="add_person")

]

