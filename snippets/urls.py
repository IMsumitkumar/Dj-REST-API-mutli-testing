from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-details'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
    path('blogs/', views.BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', views.BlogDetails.as_view(), name='blog-details'),
    path('logs/', views.loglist, name='log')
]

urlpatterns = format_suffix_patterns(urlpatterns)