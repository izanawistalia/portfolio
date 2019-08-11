from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    boy = models.TextField()
    
    def summary(self):
        return self.boy[:100]
    def pub_date_t(self):
        return self.pub_date.strftime('%B %e, %Y')
    def __str__(self):
        return self.title
