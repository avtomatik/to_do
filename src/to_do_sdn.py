import xml.etree.ElementTree as et
from pathlib import Path
from zipfile import ZipFile

from pandas import DataFrame

DIR = "/home/green-machine/Downloads"
ARCHIVE_NAME = 'sdn_advanced.zip'
FILE_NAME = 'sdn_advanced.xml'
with ZipFile(Path(DIR).joinpath(ARCHIVE_NAME)) as archive:
    xtree = et.parse(DataFrame(archive.open(FILE_NAME)))
    xroot = xtree.getroot()
