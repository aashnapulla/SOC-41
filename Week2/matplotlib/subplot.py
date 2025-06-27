import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y1, color='blue')
axes[0].set_title('Sine Wave')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

axes[1].plot(x, y2, color='red')
axes[1].set_title('Cosine Wave')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

plt.tight_layout()

plt.show()