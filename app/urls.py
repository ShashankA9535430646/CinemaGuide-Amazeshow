from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('',views.moviess,name="movies"),
    path('tv shows',views.tvshowss,name="tv shows"),
    path('movies+',views.addmovies,name="addmovies"),
    path('tvshows+',views.addtvshows,name="addtvshows")
]


