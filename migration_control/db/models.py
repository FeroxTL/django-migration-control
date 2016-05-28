# -*- coding: utf-8 -*-
from __future__ import absolute_import

from types import FunctionType
from django.db import models

from ..mixins import NoMigrateMixin


for name, cls in models.__dict__.items():
    if isinstance(cls, type):
        if issubclass(cls, models.Field):
            # Fields
            globals()[name] = type(name, (NoMigrateMixin, cls), {})
        else:
            # Managers and so on
            globals()[name] = cls
    elif isinstance(cls, FunctionType):
        # Other functions
        globals()[name] = cls
