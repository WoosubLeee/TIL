from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    # `blank` - model field option
    # True일 경우 해당 field는 blank(빈 값)를 허용
    # 유효성 검사에서 빈 값이 통과 될 수 있음(DB에는 ''(빈 문자열)이 저장됨)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
