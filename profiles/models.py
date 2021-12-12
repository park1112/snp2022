from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')     #1:1로 연결해준다
                                            #유저가 탈퇴할시 프로파일로 사라진다.
    image = models.ImageField(upload_to='profile/%Y/%m/%d', blank=True, null=False)
          #미디어 밑에 프로파일이라는 폴더에 추가된다 . 꼭 안올려도 된다 .
    nickname = models.CharField(max_length=20, unique=True, null=True)      #유니크=중복값없어야된다.
    message = models.CharField(max_length=100, null=True)   #대화명


