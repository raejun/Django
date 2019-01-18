from django.db import models

class Guest(models.Model): #부모클래스를 적어준다.(java extension이랑 같음)
    title = models.CharField("제목",max_length=30)
    content = models.CharField("내용",max_length=1000)
    write_date = models.TimeField("날짜",auto_now_add=True, blank=True)

def __str__(self):
    return self.title