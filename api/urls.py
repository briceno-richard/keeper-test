from django.urls import path
from .views import BookmarkItemViews

urlpatterns = [
    path('web-items/', BookmarkItemViews.as_view()),
    path('web-items/<int:id>', BookmarkItemViews.as_view())
]