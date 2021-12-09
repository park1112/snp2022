from django.db import models

# Create your models here.


class Project(models.Model):

    image = models.ImageField(upload_to='project/%Y/%m/%d', blank=True, null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    #어떤 게시판인지 확인할수 있게 하는것
    def __str__(self):
        return f'{self.pk} : {self.title}'
