from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BooksDetail.as_view()),
    path('merch/', views.MerchandiseList.as_view()),
    path('merch/<int:pk>/', views.MerchandiseDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)