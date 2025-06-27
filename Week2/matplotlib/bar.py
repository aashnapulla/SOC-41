import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 15]
fig, ax = plt.subplots()

ax.bar(categories, values, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])

ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Bar Chart Example')

plt.show()
