from django.db import models
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 썸네일을 임시로 새로 만들어 cache에 저장하는 방식
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(source='image',
    #                                  processors=[ResizeToFill(200, 200)],
    #                                  format='JPEG',
    #                                  options={'quality': 60})

    # 본 이미지 자체를 크롭하는 방식
    image = ProcessedImageField(upload_to='images/%Y/%m/%d/',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 100})
    created_at = models.DateTimeField(auto_now_add=True)