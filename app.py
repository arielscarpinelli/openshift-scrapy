import os

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
 
  with open('scrapyd.conf', 'w') as f:
    f.write(scrapyd_conf)

  os.system("scrapyd") 
