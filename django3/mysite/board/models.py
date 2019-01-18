from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField("제목",max_length=50)
    content = models.CharField("내용",max_length=1000)
    writer = models.CharField("글쓴이",max_length=50)
    pwd = models.CharField("비밀번호",max_length=20)
    hit = models.IntegerField("점수",default=0)
    created_date = models.DateTimeField("처음 글쓴 시간", auto_now_add=True)
    updated_date = models.DateTimeField("수정 시간",auto_now=True)

    def __str__(self):
        return self.title

# title, content, writer, pwd, hit, created_date, updated_date