import datetime as dt
from collections import defaultdict

import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap



# Set this variable to the directory where the GDELT data files are
PATH = "/home/attacc/SCRATCH/GDELT/"

with open(PATH+"2005_with_header.csv") as f:
    col_names = f.readline().split("\t")
for i, col_name in enumerate(col_names):
    print i, col_name
