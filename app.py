import os

from scrapyd import get_application
from twisted.internet import reactor
from twisted.application import app
from scrapyd.config import Config


if __name__ == '__main__':

  data_dir = os.environ['OPENSHIFT_DATA_DIR']
   
  config = Config({
    'bind_address': os.environ['OPENSHIFT_PYTHON_IP'],
    'http_port': os.environ['OPENSHIFT_PYTHON_PORT'],
    'logs_dir': os.environ['OPENSHIFT_PYTHON_LOG_DIR'],
    'eggs_dir': data_dir + 'eggs',
    'dbs_dir': data_dir + 'dbs',
    'items_dir': data_dir + 'items'
  })
  
  application = get_application(config)
  app.startApplication(application, False)
  reactor.run()
