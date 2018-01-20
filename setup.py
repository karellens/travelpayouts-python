#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('VERSION.txt', 'r') as v:
    version = v.read().strip()

with open('README.rst', 'r') as r:
    readme = r.read()

download_url = (
    'https://github.com/karellens/travelpayouts-python/archive/%s.tar.gz'
)

setup(name='travelpayouts',
      version=version,
      description='Travel Payouts API Wrapper',
      long_description=readme,
      url='http://github.com/karellens/travelpayouts-python',
      download_url=download_url % version,
      author='Denis Bozhenkov',
      author_email='mm@karellens.com',
      license='MIT',
      packages=['travelpayouts'],
      install_requires=[
          'requests',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3'
      ],
      python_requires='>=3',
      zip_safe=False)
