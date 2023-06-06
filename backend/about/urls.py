from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('about/', views.AboutList.as_view()),
    path('about/<int:pk>/', views.AboutDetail.as_view()),
    path('devotion/', views.DailyDevotionList.as_view()),
    path('devotion/<int:pk>/', views.DailyDevotionDetail.as_view()),
    path('notices/', views.NoticesList.as_view()),
    path('notices/<int:pk>/', views.NoticesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)