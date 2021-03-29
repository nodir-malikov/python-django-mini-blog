from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Article title', max_length=200)  # CharField - it is varchar (for short texts)
    article_text = models.TextField('Article text')  # TextField - it is varchar (for long texts)
    pub_date = models.DateTimeField('Date of publish')  # Date and time type

    def __repr__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(hours=5))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Name of author', max_length=50)
    comment_text = models.CharField('Comment text', max_length=200)

    def __repr__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
