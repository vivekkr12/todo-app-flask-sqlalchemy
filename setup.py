import setuptools

import todoapp

with open('README.md', 'r') as readme:
    long_description = readme.read()

with open('requirements.txt', 'r') as req:
    requirements = req.readlines()


PACKAGE_NAME = 'todoapp'
VERSION = todoapp.__version__

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='Vivek Kumar',
    author_email='vivekuma@uw.edu',
    description='A simple TODO app using Flask and SQL Alchemy for demonstrating the standard structure',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vivekkr12/todo-app-flask-sqlalchemy',
    packages=setuptools.find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
