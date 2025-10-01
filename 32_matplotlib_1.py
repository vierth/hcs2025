# often when you work with data you want to visualize it
import matplotlib.pyplot as plt

# make up some data
my_data = [i for i in range(0,10)]
my_data_2 = [i * 2 for i in range(0,10)]
print(my_data)
print(my_data_2)

plt.plot(my_data, label="made up data")
plt.plot(my_data_2, label='more made up data')
plt.legend()

plt.title("A couple of lines")
plt.ylabel("Made up number")
plt.xlabel("Index of the made up labels")

plt.show()
# plt.savefig("my_figure.jpg")