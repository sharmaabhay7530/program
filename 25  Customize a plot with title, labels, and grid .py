import matplotlib.pyplot as plt # type: ignore

# Example input data (Monthly revenue)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [2000, 2500, 1800, 3000, 2800, 3500]

# Create the plot
plt.plot(months, revenue, marker='o', linestyle='-')

# Customize the plot
plt.title("Monthly Revenue Analysis")
plt.xlabel("Months")
plt.ylabel("Revenue (in ₹)")
plt.grid(True)

# Show the plot
plt.show()