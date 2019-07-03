from django.db import models

class Blog(models.Model):
    content = models.CharField(max_length=100, verbose_name='タイトル')
    posted_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default='', blank=True, null=True, verbose_name='本文')
    image = models.ImageField(upload_to='', default='', blank=True, null=True, verbose_name='画像')

    def __str__(self):
        return self.content

    def summary (self):
        return self.body[:30]
