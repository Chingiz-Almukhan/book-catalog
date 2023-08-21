from django.urls import path

from accounts.views import register_user, get_user_favorites

urlpatterns = [
    path('register/', register_user, name='create'),
    path('user/favorites/', get_user_favorites, name='get_user')
]
