"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ourBlog import views

urlpatterns = [
    path('users/', views.users),
    path('categories/', views.categories),
    path('posts/', views.posts),
    path('words/', views.words),
    path('delPost/<post_id>', views.deletePost),
    path('users/revoke/<username>', views.revokeUser),
    path('users/grant/<username>', views.grantUser),
    path('users/block/<username>', views.blockUser),
    path('users/delete/<username>', views.delUser),
]
