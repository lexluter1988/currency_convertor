#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CurrencyData(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100, blank=True, default='')
    short_name = models.TextField()
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=10)

    class Meta:
        ordering = ('updated',)
