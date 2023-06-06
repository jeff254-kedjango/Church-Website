from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.core.validators import FileExtensionValidator

def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)

class Sermons(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="tile", verbose_name="title")
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Sermon"
        verbose_name_plural = "Sermons"


class SermonShorts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="tile", verbose_name="title")
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Short Sermons"
        verbose_name_plural = "Short Sermons"