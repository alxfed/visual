import matplotlib.pyplot as plt
import numpy as np


# Example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[0].set(xlabel='x', ylabel='y')
axs[1].plot(x, -y)
axs[1].set_title("unrelated")
axs[1].set(xlabel='x', ylabel='- y')

# ax.set(xlabel='x-label', ylabel='y-label')

plt.show()
