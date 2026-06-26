from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته")
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField(
        upload_to='img/blog',
        null=True,
        blank=True,
        verbose_name="عکس دوره"
    )
    title = models.CharField(max_length=50, verbose_name="عنوان دوره")
    excerpt = models.TextField(verbose_name="توضیحات")
    instructor = models.CharField(max_length=100, verbose_name="مدرس")
    date = models.DateField(verbose_name="تاریخ", default=date.today)
    views = models.IntegerField(verbose_name="بازدید")
    tags = models.CharField(max_length=50, blank=True, verbose_name="تگ‌ها")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title