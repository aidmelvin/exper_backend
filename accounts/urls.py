from django.urls import path
from .views import CreateAccountView, LoginView


urlpatterns = [
    path('signup/', CreateAccountView.as_view()),
    path('login/', LoginView.as_view()),
]
