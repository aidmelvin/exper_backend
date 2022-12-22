from django.urls import path
from user_functionality.views.user_search import UserSearch
from user_functionality.views.fill_interests_table import FillInterestsTable


urlpatterns = [
    path('search_for_users/', UserSearch.as_view()),
    path('fill_interests_table/', FillInterestsTable.as_view()),
]
