from setuptools import setup

setup(name='openshift-scrapy',
      version='1.0',
      description='Scrapy on openshift',
      author='Ariel Scarpinelli',
      author_email='triforcexp AT gmail',
      url='http://www.python.org/sigs/distutils-sig/',
      # Will need to use Scrapyd's git location until a version is published
      # containing this fix: https://github.com/scrapy/scrapyd/issues/49 (probably 1.0.2)
      # and to do it so, we specify it in requirements.txt to force version override
      install_requires=[
        'Scrapy',
        'service_identity', 
        #'Scrapyd>1.0.1',
      ],
     )
