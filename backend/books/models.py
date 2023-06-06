from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.core.validators import FileExtensionValidator

def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)


class Books(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="tile", verbose_name="title")
    prologue = models.TextField(help_text="Prologue")
    price = models.IntegerField(blank=False, null=False)
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    secondImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    thirdImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    fourthImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class Merchandise(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="tile", verbose_name="title")
    prologue = models.TextField(help_text="Prologue")
    price = models.IntegerField(blank=False, null=False)
    image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    secondImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    thirdImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    fourthImage = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Merchandise"
        verbose_name_plural = "Merchandise"