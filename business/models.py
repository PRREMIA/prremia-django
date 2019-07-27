from django.db import models

class Home(models.Model):
    description = models.TextField()
    DROP = [
        ('Home', 'Home'),
        ('Phone', 'Phone'),
        ('Email', 'Email'),
        ('Products', 'Products'),
        ('About', 'About'),
    ]
    title = models.CharField(max_length=50,choices=DROP)

    def __str__(self):
        return self.title