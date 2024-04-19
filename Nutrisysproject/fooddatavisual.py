import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Nutrisysproject/FoodData_Central_csv_2023-10-26/input_food.csv')

# Extract relevant columns
milk_types = data['sr_description']
gram_weights = data['gram_weight']

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(milk_types, gram_weights)
plt.xlabel('Milk Types')
plt.ylabel('Gram Weight')
plt.title('Gram Weight of Different Milk Types')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
