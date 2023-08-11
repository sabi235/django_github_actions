from django.shortcuts import get_object_or_404, render
from .models import Article
def content_view(request, pk):
   post = get_object_or_404(Article, pk=pk)
   return render(request, "blog/article.html", {'post':post})