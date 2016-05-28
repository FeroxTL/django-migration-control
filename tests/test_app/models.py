# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from migration_control.db import models


class TestModel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        help_text='This is old help.')
