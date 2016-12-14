try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	"description":"Skeleton",
	"author": "Sankar",
	"url": "URL to get it at.",
	"download_url": "Where to dowload it",
	"author_email": "sesankar11@gmail",
	"version":"0.1",
	"install_requires": ["nose"],
	"packages": ['NAME'],
	"scripts": []
	"name": "projectname" 
]

setup(**config)
