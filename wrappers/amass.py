import subprocess

import helpers
import logger

log = logger.getLogger(__name__)


def scan(domain):
    binaryPath = helpers.which('amass')

    resultsDirectory = 'results/%s/amass-%s' % ('domain', helpers.getDate())
    if not binaryPath:
        log.warning('Aborting Amass scan')
        return False

    helpers.createDirectory(resultsDirectory)

    subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
