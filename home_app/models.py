from django.db import models

class Information(models.Model):
    experience = models.IntegerField(null=True)
    articles = models.IntegerField(null=True)
    courses = models.IntegerField(null=True)

    
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

class About(models.Model):
    bio_f = models.TextField(null=True)
    bio_e = models.TextField(null=True)
    resumes = models.CharField(max_length=100, null=True)

    tool = models.CharField(max_length=100, null=True)

    # Experience
    date_exp = models.DateField(null=True)
    title_exp = models.CharField(max_length=100, null=True)
    place_exp = models.CharField(max_length=100, null=True)
    descripption_exp = models.TextField(null=True)
    
    # Education
    date_edu = models.DateField(null=True)
    title_edu = models.CharField(max_length=100, null=True)
    place_edu = models.CharField(max_length=100, null=True)
    descripption_edu = models.TextField(null=True) 