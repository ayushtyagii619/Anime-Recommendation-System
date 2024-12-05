from django.urls import path
from .views import RegistrationApiView, LoginApiView,AnimeSearchView,UserPreferencesView,AnimeRecommendationView

urlpatterns = [
    path('auth/register',RegistrationApiView.as_view(),name='registration'),
    path('auth/login',LoginApiView.as_view(),name='login'),
    path('anime/search', AnimeSearchView.as_view(), name='anime-search'),
    path('user/preferences', UserPreferencesView.as_view(), name='user-preferences'),
    path('anime/recommendations', AnimeRecommendationView.as_view(), name='anime-recommendations'),
]