#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt


fig, ax = plt.subplots(figsize=(6,6), subplot_kw={"aspect":1})
ax.plot(range(10))
plt.show()