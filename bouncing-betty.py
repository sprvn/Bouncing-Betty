import helpers
import logger

logger.configure(level='warning')
log = logger.getLogger(__name__)

log.warning('testar')
log.debug('testar2')

#print(helpers.checkVPN())

