# Print the last item from year and pop
print(life_exp[-1])
print(gdp_cap[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(gdp_cap,life_exp)

# Display the plot with plt.show()
plt.show()
