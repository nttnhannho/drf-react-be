from django.urls import path

from blog_api.views import (
    PostDetail,
    PostList,
)

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('', PostList.as_view(), name='post-list'),
]
