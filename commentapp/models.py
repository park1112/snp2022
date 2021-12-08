from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    #아티클 정보 가져온다 .
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    #유저모델 정보 가져온다 .
    content = models.TextField(null=False)
    #내용추가
    created_at = models.DateTimeField(auto_now=True)
    #생성시간