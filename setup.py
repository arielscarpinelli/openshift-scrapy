from setuptools import setup

setup(name='openshift-scrapy',
      version='1.0',
      description='Scrapy on openshift',
      author='Ariel Scarpinelli',
      author_email='triforcexp AT gmail',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Scrapy', 'Scrapyd', 'service_identity'],
     )
