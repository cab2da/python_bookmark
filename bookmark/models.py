from django.db import models
from django.urls import reverse

# Create your models here.

class Bookmark(models.Model):
    # 필드 추가하여 모델 만들기
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 모델 생성 후 마이그레이션(migrate) => 데이터베이스에 모델의 내용을 반영 ( 테이블 생성 )
    # 1. makemigrations => 모델의 변경사항을 추적해서 기록
    #   python manage.py makemigrations bookmark
    #   migrations 폴더에 0001_initial.py 파일 생성됨
    # 2. migrate)
    #   python manage.py migrate bookmark 0001

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])   # args=[str(self.id)] 처럼 해도 무방
