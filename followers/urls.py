from django.urls import path
from followers import views


urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
    path('profiles/<int:user_id>/followers/', views.ProfileFollowersList.as_view(), name='profile-followers-list'),
    path('profiles/<int:user_id>/following/', views.ProfileFollowingList.as_view(), name='profile-following-list'),
]