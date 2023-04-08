# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from pathlib import Path

from lxml import etree

DIR = '../data/raw'
FILE_NAME = 'conforti-figure1.stm'

with open(Path(DIR).joinpath(FILE_NAME)) as f:
    root = etree.parse(f).getroot().getchildren()
    for children in root:
        print(children.xpath)
