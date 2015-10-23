try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Cards',
      version='0.1',
      desciption='Card Library written in Python',
      author='Tanpreet Grewal',
      packages=['cards']
)

