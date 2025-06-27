import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

fig, ax = plt.subplots()

ax.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')

ax.set_xlabel('Random X')
ax.set_ylabel('Random Y')
ax.set_title('Scatter Plot with Varying Size and Color')

plt.show()