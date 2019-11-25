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
    url = sys.argv[2]
    depth = int(sys.argv[3])
    open(LOG, 'w').close() # clear the file
    if sys.argv[1] == 'local':
        crawling.start_local_crawling(url, 1)
    elif sys.argv[1] == 'pylambder':
        task = crawling.start_crawling(url, 1)
        time.sleep(10)
    else:
        print(f"Usage: {sys.argv[0]} local|pylambder URL DEPTH")
