# -*- coding: utf-8 -*-
"""https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
"""
import matplotlib.pyplot as plt
import numpy as np


# Example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(3, figsize=(5, 15))
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y, 'tab:green')
axs[0].set(xlabel='x', ylabel='y')
axs[1].plot(x, -y, 'tab:red')
axs[1].set(xlabel='x', ylabel='- y')

axs[2].set_title("unrelated")
axs[2].hist2d(x, y)

# ax.set(xlabel='x-label', ylabel='y-label')

plt.show()
