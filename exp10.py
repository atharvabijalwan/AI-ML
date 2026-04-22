import matplotlib.pyplot as plt

# 1. Predefined Data
# X-axis: Hours of Study
hours = [1, 2, 3, 4, 5, 6, 7]
# Y-axis: Marks Scored
marks = [20, 35, 50, 65, 70, 85, 90]

# 2. Create the Plot
plt.figure(figsize=(8, 5))

# Plotting the line (marker='o' adds dots at the data points)
plt.plot(hours, marks, color='blue', marker='o', linestyle='-', linewidth=2)

# 3. Adding Labels and Title
plt.title("Study Hours vs Students Marks")
plt.xlabel("Hours of Study")
plt.ylabel("Marks Obtained")

# Add a grid for better readability
plt.grid(True)

# 4. Show the Graph
plt.show()