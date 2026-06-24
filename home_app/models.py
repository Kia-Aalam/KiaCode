from django.db import models

class Footer(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    
class Contact(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    
    SUBJECT_CHOICES = [
        ('Collaboration', 'پیشنهاد همکاری'),
        ('Course Question', 'سوال درباره دوره‌ها'),
        ('Content Suggestion', 'پیشنهاد محتوا'),
        ('Bug Report', 'گزارش مشکل '),
        ('Just Saying Hi', 'فقط سلام')
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    
    message = models.TextField(null=False)
    
    def __str__(self):
        return self.username