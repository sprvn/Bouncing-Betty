import requests
import json
import os
import sys
import datetime

import logger

log = logger.getLogger(__name__)

def checkVPN():
    log.info('Checking VPN status')
    r = requests.get('https://am.i.mullvad.net/json')

    if r.status_code != 200:
        log.debug('VPN status request returned non-zero code: %s' % (r.status_code))
        return False

    try:
        resp = json.loads(r.text)
    except:
        log.debug('Failed to parse response as json')
        return False

    if 'mullvad_exit_ip' not in resp:
        log.debug('mulvad_exit_ip key not present in request response')
        return False

    if resp['mullvad_exit_ip'] == True:
        log.info('VPN connected')
        return True
    else:
        log.critical('VPN not connected')
        return False

def which(program):
    log.info('Verifying the presence of %s' % (program.capitalize()))
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            log.info('%s found' % (program.capitalize()))
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                log.info('%s found' % (program).capitalize())
                return exe_file

    log.warning('%s not found' % (program).capitalize())
    return None

def createDirectory(directory):
    log.debug('Creating %s directory if it does not exist' % (directory))
    if not os.path.exists(os.path.join(sys.path[0], directory)):
        os.makedirs(os.path.join(sys.path[0], directory))
        log.info('Created %s directory' % (directory))
    log.debug('Directory %s already exists')

def getDate():
    return datetime.date.today().strftime('%Y%m%d')
    
