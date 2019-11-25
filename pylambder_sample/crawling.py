import json
import re
import sys

import requests

from pylambder_sample.pylambder import scheduler

LOG = './crawled.json'


@scheduler.task
def get_links(url):
    r = requests.get(url)
    return re.findall('href="(http.*?)"', r.text)


def start_crawling(url, depth):
    task = get_links.delay(url)
    task.set_callback(_make_callback(url, depth))
    return task


def start_local_crawling(url, depth):
    if depth < 0:
        return []

    urls = get_links(url)
    print("Crawled", url)
    _save_found(url, urls)
    for url in urls:
        start_local_crawling(url, depth - 1)

def _make_callback(url, depth):
    def callback(urls):
        print(f"Crawling {url} finished at depth {depth}")
        sys.stdout.flush()
        _save_found(url, urls)
        if depth > 0:
            for u in urls:
                task = get_links.delay(u)
                task.set_callback(_make_callback(u, depth - 1))
    return callback


def _save_found(from_url, urls):
    with open(LOG, 'a') as f:
        for url in urls:
            f.writelines([json.dumps({'from': from_url, 'url': url}) + '\n'])
