from django.urls import path
from accounts.views.create_account import CreateAccountView
from accounts.views.home_page import HomePageView
from accounts.views.login import LoginView
from accounts.views.logout import LogoutView
from accounts.views.get_user_info import GetUserInfo
from accounts.views.set_user_info import SetUserInfo


urlpatterns = [
    path('signup/', CreateAccountView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('home/', HomePageView.as_view()),
    path('getuserinfo/', GetUserInfo.as_view()),
    path('setuserinfo/', SetUserInfo.as_view()),
]
