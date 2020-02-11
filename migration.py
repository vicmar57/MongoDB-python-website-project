# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:17:36 2020

@author: vicma
"""

from mflix.db import get_movie
from datetime import datetime

result = get_movie("573a13b8f29313caabd4c8c5")
assert isinstance(result.get('lastupdated'), datetime)