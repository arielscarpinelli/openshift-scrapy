from twisted.scripts.twistd import run
from os.path import join, dirname
from sys import argv
import scrapyd
argv[1:1] = ['-n', '-y', join(dirname(scrapyd.__file__), 'txapp.py')]
run()
