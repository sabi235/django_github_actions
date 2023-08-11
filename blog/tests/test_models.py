import pytest
from blog.models import Article
@pytest.mark.django_db
def test_article_create():
# Create dummy data
   article = Article.objects.create(
   author_name="Muhammed Ali",
   title="Simple article",
   content="This is my content",
   )
# Assert the dummy data saved as expected
   assert article.author_name=="Muhammed Ali"
   assert article.title=="Simple article"
   assert article.content=="This is my content"