from django.db import models

# Create your models here.

class Aboutus(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self):
        return self.title

class Why_Chose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'why chose us'
        verbose_name_plural = 'why chose us'

    def __str__(self):
        return self.title
