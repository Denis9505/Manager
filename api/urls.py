from django.urls import path

from .views import TransactionListView, UserViews, CategoryListViews, UserProfileDetailView

urlpatterns = [
    path('transactionlist', TransactionListView.as_view()),
    path('category', CategoryListViews.as_view()),
    path('all-users', UserViews.as_view()),
   # retrieves profile details of the currently logged in user
    path("user/<int:pk>",UserProfileDetailView.as_view(),name="profile"),
]
