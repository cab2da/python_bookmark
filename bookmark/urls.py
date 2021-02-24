from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/ 로 접속한 경우
    path("", BookmarkListView.as_view(), name='list'),   # 클래스형 뷰일 경우 ~~~.as_view() 붙여야 함
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]