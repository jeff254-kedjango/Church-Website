from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('sermons/<int:pk>/', views.SermonsDetail.as_view()),
    path('shorts/<int:pk>/', views.SermonShortsDetail.as_view()),
    path('sermons/', views.SermonsList.as_view()),
    path('shorts/', views.SermonShortsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)