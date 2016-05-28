#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-migration-control',
    version='0.1.2',
    description='Django migration control allows avoid unnecessary migrations such as changing help_text or verbose_name of fields',
    author='Makarov Yurii',
    author_email='winnerer@ya.ru',
    url='https://github.com/FeroxTL/django-migration-control',
    packages=find_packages(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ),
    license="MIT",
)
