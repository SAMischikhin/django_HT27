from django.db import models


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    price = models. PositiveIntegerField()
    description = models.CharField(max_length=300, default='')
    address = models.CharField(max_length=30, default='')
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)



