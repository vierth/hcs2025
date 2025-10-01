import matplotlib.pyplot as plt
import seaborn as sns
import random

sns.set_theme()

x_data = [random.randint(0,100) for i in range(0,100)]
y_data = [random.randint(0,100) for i in range(0,100)]
size_data = [random.randint(4,100) for i in range(0,100)]
colors = ["magenta" for _ in range(0,100)]
for i in range(0, 100):
    random_num = random.randint(0,100)
    if random_num < 20:
        colors[i] = "#000000"

plt.title("Random Data")
plt.scatter(x_data, y_data, s=size_data, c=colors)
plt.xlabel("Some random nums")
plt.ylabel("other random nums")


plt.show()