
# image = Image.open('image.jpg')
# image.show()
#!/usr/bin/env python

from argparse import ArgumentParser
from bs4 import BeautifulSoup
from os import name, path, makedirs
from requests import get
from sys import argv
from time import sleep
from typing import Tuple
from urllib import request
from PIL import Image


def get_comic() -> Tuple[str, Image.Image]:

    request = get(f"https://xkcd.com").text.strip()
    soup = BeautifulSoup(request, "html.parser")

    comic = soup.find("div", {"id": "comic"})
    print(comic)


def run():

    parser = ArgumentParser(prog="xkcd")

    namespace = parser.parse_args()

    get_comic()

    # title, image =



if __name__ == "__main__":
    run()
