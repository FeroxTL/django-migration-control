# -*- coding: utf-8 -*-
from django.conf import settings


DEFAULT_EXCLUDE_FIELDS = ['help_text', 'verbose_name', 'choices']


class NoMigrateMixin(object):
    """
    Allows to exclude any field from migrations
    """
    def deconstruct(self):
        name, path, args, kwargs = super(NoMigrateMixin, self).deconstruct()
        exclude_fields = getattr(
            settings, 'EXCLUDE_FIELDS', DEFAULT_EXCLUDE_FIELDS)
        for field_name in exclude_fields:
            kwargs.pop(field_name, None)
        return name, path, args, kwargs
