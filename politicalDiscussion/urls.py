from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from articles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]