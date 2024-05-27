from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='short_time/videos/%Y/%m/%d/}')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return f'[{self.pk}]{self.title}'