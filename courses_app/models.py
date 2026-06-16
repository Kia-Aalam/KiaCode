from django.db import models

class Course(models.Model):

    LEVEL_CHOICES = [
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'پیشرفته'),
    ]

    image = models.ImageField(
        upload_to='img/KiaCode', 
        null=True, 
        blank=True, 
        verbose_name="عکس دوره"
    )
    title = models.CharField(max_length=50, verbose_name="عنوان دوره")
    description = models.TextField(verbose_name="توضیحات")
    level = models.CharField(choices=LEVEL_CHOICES, default='beginner', verbose_name="سطح")
    duration_hours = models.IntegerField(verbose_name="مدت زمان (ساعت)")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت (تومان)")
    instructor = models.CharField(max_length=100, verbose_name="مدرس")
    
    # Style
    gradient_start = models.CharField(max_length=20, default='#667eea', verbose_name="رنگ شروع گرادینت")
    gradient_end = models.CharField(max_length=20, default='#764ba2', verbose_name="رنگ پایان گرادینت")

    def __str__(self):
        return self.title
