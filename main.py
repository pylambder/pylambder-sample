#!/usr/bin/env python3

import asyncio
import datetime
import logging
import sys
import time

import pylambder_sample.crawling as crawling
from pylambder_sample.pylambder import scheduler

logging.basicConfig(format='%(levelname).1s %(asctime).23s %(message)s')

logging.basicConfig()
logger = logging.getLogger('pylambder')
logger.setLevel(logging.DEBUG)

LOG = crawling.LOG

if __name__ == '__main__':
    url = sys.argv[1]
    open(LOG, 'w').close() # clear the file
    task = crawling.start_crawling(url, 1)
    time.sleep(10)
