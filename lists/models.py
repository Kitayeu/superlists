from django.db import models


class List(models.Model):
    """list"""
    pass


class Item(models.Model):
    """list item"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
