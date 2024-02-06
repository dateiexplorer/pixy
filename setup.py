from distutils.core import setup
import setuptools

setup(name='pixy',
      version='1.0',
      description='Use pip from behind a proxy',
      author='Justus Röderer',
      author_email='justus.roederer@wuerth-it.com',
      packages=setuptools.find_packages(),
      entry_points={
        'console_scripts': ['pixy = pixy.__main__:main']
      })
