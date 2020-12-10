from django.contrib import admin
from django.urls import path
from main.views import main_view, delete_view, accounts_view, login_view, signup_view, \
    logout_view, profile_view, like_view, hashtag_view, follow_view, unfollow_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('login_view/', login_view, name='login_view'),
    path('signup_view/', signup_view, name='signup_view'),
    path('logout_view/', logout_view, name='logout_view'),
    path('accounts', accounts_view, name='accounts_view'),
    path('profile/<str:author>/', profile_view, name='profile_view'),
    path('hashtag', hashtag_view, name='hashtag_view'),
    path('follow/<str:author>/', follow_view, name='follow_view'),
    path('unfollow/<str:author>/', unfollow_view, name='unfollow_view'),
    path('delete', delete_view, name='delete_view'),
    path('like', like_view, name='like_view')
]
