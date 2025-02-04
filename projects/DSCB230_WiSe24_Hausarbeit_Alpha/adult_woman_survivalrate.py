import matplotlib.pyplot as plt
import pandas as pd


# Load the Titanic dataset
def load_titanic_data(filepath):
    try:
        titanic_data = pd.read_csv(filepath)
        return titanic_data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


titanic_data = load_titanic_data('data/titanic_cleaned.csv')

# Filter for adult women (age > 18)

adult_women = titanic_data[(titanic_data['Sex'] == 'female') & (titanic_data['Age'] > 18)]

# Count the number of survivors and non-survivors
survival_counts = adult_women['Survived'].value_counts().to_dict()

# Functional approach: Aggregate data and prepare labels for visualization
def aggregate_survival(survived_count_dict):
    return {
        'Survived': survived_count_dict.get(1, 0),
        'Not Survived': survived_count_dict.get(0, 0)
    }

# Apply aggregation
aggregated_survival = aggregate_survival(survival_counts)

# Data for pie chart
labels = aggregated_survival.keys()
sizes = aggregated_survival.values()
colors = ['#66b3ff', '#ff6666']  # Custom colors for better visualization
explode = (0.1, 0)  # Only "explode" the Survived slice

# Plotting pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
plt.title('Survival Rate of Adult Women on the Titanic')
plt.show()
