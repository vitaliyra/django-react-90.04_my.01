from django.shortcuts import render

from rest_framework.generics import get_object_or_404
from .models import Article
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleSerializer

def index(request):
    return render(request, "articles/index.html")


class ArticleView(APIView):
    def get(self, request):
        articles=Article.objects.all()
        serializer = ArticleSerializer(articles, many= True)
        return Response({"articles":serializer.data})

    def post(self, request):
        article=request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved=serializer.save()
        return Response({"succses":" Статья создана успешно".format(article_saved.title)})
            
        
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })    