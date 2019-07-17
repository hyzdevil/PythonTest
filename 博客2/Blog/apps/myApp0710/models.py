from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Type(models.Model):
    name = models.CharField(db_column="类别", max_length=32)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(db_column="姓名", max_length=32)

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"

    def __str__(self):
        return self.name

class Artical(models.Model):
    title = models.CharField(db_column="文章", max_length=32)
    content = RichTextField()
    description = RichTextField()
    createtime = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="images")
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"

    def __str__(self):
        return self.title


class LeaveMessage(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name