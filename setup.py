try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'desciption': 'Card Library',
        'author': 'Tanpreet Grewal',
        'version': '0.1'
}

setup(**config)
