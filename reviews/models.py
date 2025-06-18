from django.db import models

class Reviews(models.Model):
    name=models.CharField(max_length=200)
    review=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name+' '+(self.review)[:25]