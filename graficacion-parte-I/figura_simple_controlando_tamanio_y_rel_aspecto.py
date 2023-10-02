#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt


fig = plt.figure(figsize=(6,6))
ax = plt.subplot(aspect=1)
ax.plot(range(10))
plt.show()