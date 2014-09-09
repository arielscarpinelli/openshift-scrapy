import os

from cStringIO import StringIO
from scrapyd import get_application
from twisted.internet import reactor
from twisted.application import app
from scrapyd.config import Config


if __name__ == '__main__':

  data_dir = os.environ['OPENSHIFT_DATA_DIR']
   
  config_values = {
    'bind_address': os.environ['OPENSHIFT_PYTHON_IP'],
    'http_port': os.environ['OPENSHIFT_PYTHON_PORT'],
    'logs_dir': os.environ['OPENSHIFT_PYTHON_LOG_DIR'],
    'eggs_dir': data_dir + 'eggs',
    'dbs_dir': data_dir + 'dbs',
    'items_dir': data_dir + 'items'
  }

  scrapyd_conf = "[scrapyd]\n" + \
    "\n".join('{}={}'.format(key, val) for key, val in config_values.items())
  
  config = Config(extra_sources=[StringIO(scrapyd_conf)])
  application = get_application(config)
  app.startApplication(application, False)
  reactor.run()
