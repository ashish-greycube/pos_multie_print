# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pos_multie_print/__init__.py
from pos_multie_print import __version__ as version

setup(
	name='pos_multie_print',
	version=version,
	description='App that does multi printing of invoice on different printers',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
