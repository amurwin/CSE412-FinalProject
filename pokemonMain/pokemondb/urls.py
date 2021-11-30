from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_pokemon, name="poke_details"),
    path("details/<int:pk>/", views.poke_detail, name="details"),
    path("abilities/", views.all_abilities, name="abilities"),
    path("abilities/<str:pk>/", views.ability_detail, name="ability"),
    path("moves/", views.all_moves, name="moves"),
    path("moves/<str:pk>/", views.move_detail, name="move"),
]