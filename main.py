#!/usr/bin/env python3

import asyncio
import datetime
import logging
import time
# import sub.module as submodule
import numpy as np
import pandas as pd

import pylambder_sample.utils.tasks as my_tasks
import pylambder_sample.heavy_logic as heavy_logic

logging.basicConfig(format='%(levelname).1s %(asctime).23s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



def test_callback(result):
    logger.info("Callback: {}".format(result['div'] + 100))
    return result['div'] + 100


if __name__ == '__main__':
    print("Task1")
    task = my_tasks.task1.delay(3)
    print(task.get_result())
    
    print("Task2")
    print(my_tasks.task2.delay().get_result())

    print("Heavy:")
    print(heavy_logic.get_id_done())