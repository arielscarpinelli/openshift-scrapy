from scrapyd import get_application
from twisted.internet import reactor
from twisted.application import app

application = get_application(config)
app.startApplication(application, False)
reactor.run()
