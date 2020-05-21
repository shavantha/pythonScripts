#!/usr/bin/env python
import requests
from requests import get
import re
import urlparse


def geturl(host_url):
    try:
        return requests.get("http://" + host_url)
    except requests.exceptions.ConnectionError:
        pass


def crawl(url):
    target_url = url
    target_links = []
    with open("/home/shavantha/Desktop/dir.list", "r") as word_list_file:
        for line in word_list_file:
            word = line.strip()
            new_url = url + "/" + word
            response = geturl(new_url)
            if response:
                print("[+]Discovered the Directory\t" + new_url)
                href_link = re.findall('(?:href=")(.*?)"', response.content)
                for link in response:
                    link = urlparse.urljoin(url, link)
                    if "#" in link:
                        link = link.split("#")[0]

                    if target_url in link and link not in target_links:
                        target_links.append(link)
                        print(">>>\n" + str(link) + "\n")
                        crawl(link)


crawl("localhost:8080")
