#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

import uuid, os


def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename


class Reader(models.Model):
    class Meta:
        verbose_name = 'reader'
        verbose_name_plural = 'reader'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='reader')
    name = models.CharField(max_length=16, unique=True, verbose_name='name')
    phone = models.IntegerField(unique=True, verbose_name='telephone')
    max_borrowing = models.IntegerField(default=5, verbose_name='remaining quantity')
    balance = models.FloatField(default=0.0, verbose_name='balance')
    photo = models.ImageField(blank=True, upload_to=custom_path, verbose_name='head portrait')
    like = models.IntegerField(default=100, verbose_name='like')

    STATUS_CHOICES = (
        (0, 'normal'),
        (-1, 'overdue')
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = 'books'
        verbose_name_plural = 'books'

    ISBN = models.CharField(max_length=13, primary_key=True, verbose_name='ISBN')
    title = models.CharField(max_length=128, verbose_name='book name')
    author = models.CharField(max_length=32, verbose_name='author')
    press = models.CharField(max_length=64, verbose_name='publisher')

    description = models.CharField(max_length=10240, default='', verbose_name='detials')
    price = models.CharField(max_length=20, null=True, verbose_name='price')

    category = models.CharField(max_length=64, default=u'literature', verbose_name='catelog')
    cover = models.ImageField(blank=True, upload_to=custom_path, verbose_name='cover')
    index = models.CharField(max_length=16, null=True, verbose_name='indexes')
    location = models.CharField(max_length=64, default=u'1st floor in library', verbose_name='position')
    quantity = models.IntegerField(default=1, verbose_name='quantity')

    def __str__(self):
        return self.title + self.author


class Borrowing(models.Model):
    class Meta:
        verbose_name = 'borrow'
        verbose_name_plural = 'borrow'

    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='reader')
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='ISBN')
    date_issued = models.DateField(verbose_name='borrow time')
    date_due_to_returned = models.DateField(verbose_name='deadline')
    date_returned = models.DateField(null=True, verbose_name='return time')
    amount_of_fine = models.FloatField(default=0.0, verbose_name='debt')

    def __str__(self):
        return '{} borrows {}'.format(self.reader, self.ISBN)

class Like(models.Model):
    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'like'

    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='reader',related_name='reader')
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='ISBN')

    def __str__(self):
        return '{} likes {}'.format(self.reader, self.ISBN)

class Movie(models.Model):
    rate=models.CharField(max_length=4,verbose_name='score')
    title=models.CharField(max_length=64,verbose_name='title')
    movie_url=models.URLField(verbose_name='film links')
    image=models.ImageField(blank=True,upload_to=custom_path, verbose_name='film covers')
    info=models.TextField(verbose_name='introduction')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movie'

