from django.db import models

# Create your models here.

class About(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="Enter title", verbose_name="title")
    more = models.TextField(help_text="Explain yourself")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Pillar Statement"
        verbose_name_plural = "Pillar Statements"

class Dailydevotion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=225, help_text="Your Name", verbose_name="name")
    verse = models.TextField(help_text="Enter Verse")
    devotion = models.TextField(help_text="Enter devotion")
    video = models.FileField(upload_to='images',null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Devotion"
        verbose_name_plural = "Devotions"


class Notices(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225, help_text="tile", verbose_name="title")
    notice = models.TextField(help_text="Enter notice")
    image = models.ImageField(upload_to ='images', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

