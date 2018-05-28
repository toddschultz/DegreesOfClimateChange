from setuptools import setup

readme = open('README.md').read()

setup(
   name='DegreesofClimateChange',
   version='1.0',
   description='A useful module',
   author='Todd, Abhishek, Rahul',
   author_email='setup@setup.com',
   packages=['DegreesofClimateChange'],  #same as name
   install_requires=['pandas','numpy','datetime','sys','wbpy'], #external packages as dependencies
)