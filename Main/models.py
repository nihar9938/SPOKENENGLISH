from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Register(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Course = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Mail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email

class Courses(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name + ' - ' + self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' - ' + self.name
