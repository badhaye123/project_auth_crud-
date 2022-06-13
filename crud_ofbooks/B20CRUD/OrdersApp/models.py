from django.db import models

# Create your models here.
seller_choices = (
    ('Python','Python'),
    ('Javascript','Javascript'),
    ('Reactjs','Reactjs'),
    ('Php','Php'),
    ('Networking','Networking')
)

class Books(models.Model):
    bookname = models.CharField(max_length=32,choices=seller_choices)
    pages = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
   

