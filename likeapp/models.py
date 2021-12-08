from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    #유저 연결 유저 없어지면 이것도 없어짐
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')
    #아티클도 연결

    class Meta:
        unique_together = ('user', 'article')   #유니크 투게더 유저와 아티클은 쌍으로만 존재함.
