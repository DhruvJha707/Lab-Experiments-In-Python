''' Create a program to demonstrate different visual forms using Matplotlib.'''

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# ---------- Line Plot ----------
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# ---------- Bar Chart ----------
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X-axis")
plt.ylabel("Values")
plt.show()

# ---------- Scatter Plot ----------
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# ---------- Pie Chart ----------
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [10, 20, 25, 30, 15]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()