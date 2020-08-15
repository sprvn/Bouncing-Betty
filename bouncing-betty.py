import helpers
import logger

import database
import wrappers.amass as amass

logger.configure(level='info')
log = logger.getLogger(__name__)

amass.scan('test_domain')

#print(helpers.checkVPN())

