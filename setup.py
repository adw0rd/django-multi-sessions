from setuptools import setup, find_packages
from multi_sessions import __version__
setup(
    name='django-multi-sessions',
    version=__version__,
    description="Multi-sessions backend for Django",
    long_description="",
    keywords='django, sessions',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/django-multi-sessions',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
