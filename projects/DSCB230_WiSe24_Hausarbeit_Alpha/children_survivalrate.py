import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
file_path = 'data/titanic_cleaned.csv'  # Update with the correct path if needed

try:
    titanic_data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Filter for children (age <= 18) and calculate survival counts directly using pandas
children_survival_counts = (
    titanic_data[titanic_data['Age'] <= 18]
    .groupby('Survived')
    .size()
    .reindex([1, 0], fill_value=0)
    .to_dict()
)

# Aggregate survival data
aggregated_children_survival = {
    'Survived': children_survival_counts.get(1, 0),
    'Not Survived': children_survival_counts.get(0, 0),
}

# Data for pie chart
labels = aggregated_children_survival.keys()
sizes = aggregated_children_survival.values()
colors = ['#66b3ff', '#ff6666']  # Custom colors for better visualization
explode = (0.1, 0)  # Only "explode" the Survived slice

# Plotting pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title('Survival Rate of Children on the Titanic')
plt.show()
