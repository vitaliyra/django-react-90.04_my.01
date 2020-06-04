from django.urls import path
from .views import ArticleView
from articles import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name='home'),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view())
]
