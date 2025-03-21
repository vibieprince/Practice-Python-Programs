import matplotlib.pyplot as plt
import numpy as np

# Dataset
foods = ["Meat", "Banana", "Avocados", "Sweet Potatoes", "Spinach", 
         "Watermelon", "Coconut Water", "Beans", "Legumes", "Tomato"]
calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

# Bar width
bar_width = 0.3
x = np.arange(len(foods))

# Create bar plots for Calories, Potassium, and Fat
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width, calories, width=bar_width, label="Calories", color='red')
plt.bar(x, potassium, width=bar_width, label="Potassium", color='blue')
plt.bar(x + bar_width, fat, width=bar_width, label="Fat", color='green')

# Labels and Title
plt.xlabel("Food Items")
plt.ylabel("Nutrient Values")
plt.title("Nutritional Comparison of Foods")
plt.xticks(ticks=x, labels=foods, rotation=45)
plt.legend()

# Show plot
plt.show()
