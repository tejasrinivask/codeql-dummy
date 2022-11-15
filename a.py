import os
from b import *


f = 'a.ini'
os.chmod(f, 0o777)
g = open(f)
