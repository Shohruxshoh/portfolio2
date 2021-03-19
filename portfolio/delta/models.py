from django.db import models
from django.shortcuts import reverse


# Create your models here.

class db_projects(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    img = models.ImageField()
    link = models.TextField()

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Contact(models.Model):
    telefon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    Email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class Skills(models.Model):
    html = models.IntegerField()
    css = models.IntegerField()
    python = models.IntegerField()

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"


class Adress(models.Model):
    telefon = models.TextField()
    Email = models.EmailField()
    adress = models.CharField(max_length=100)


class Comments(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'komment'
        verbose_name_plural = 'kommentlar'