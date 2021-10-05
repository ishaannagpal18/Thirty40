from django.db import models

# Create your models here.
class about(models.Model):

    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=800, blank=False)
    image=models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title

class slider(models.Model):

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    image=models.ImageField(upload_to='slider/')
    def __str__(self):
        return self.title

class clients(models.Model):

    name=models.CharField(max_length=100)
    link=models.CharField(max_length=400)
    image=models.ImageField(upload_to='clients/')
    def __str__(self):
        return self.name

class portfolio(models.Model):

    product=models.CharField(max_length=100, blank=False)
    image=models.ImageField(upload_to='portfolio/', blank=False)

    def __str__(self):
        return self.product
