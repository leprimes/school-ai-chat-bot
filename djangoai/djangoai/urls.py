from django.contrib import admin
from django.urls import path
from .views import index, ask_bot, chess_game


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('ask/', ask_bot, name='ask'),
    path('chess/', chess_game, name='chess'),

]
