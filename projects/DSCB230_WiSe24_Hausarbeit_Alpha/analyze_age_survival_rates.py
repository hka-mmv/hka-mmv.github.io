# Titanic Survivability Analysis
# Analyze Age Survival Rates Module

# Best used in notebook

# Author: Leon Gjinovci

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Titanic dataset
df = pd.read_csv('data/titanic_cleaned.csv')

def analyze_survivablity_by_age_group(df):
    # Define age groups
    bins = [0, 6, 18, 24, 67, float('inf')] # float('inf') is used to represent infinity, and cover all ages above 67
    labels = ['Infant', 'Child', 'Teen', 'Adult', 'Senior']
    
    # Create a new column 'AgeGroup' based on the defined bins and labels
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # Calculate survivablity rate for each age group
    age_group_counts = df.groupby('AgeGroup')['Survived'].count()
    age_group_deaths = df.groupby('AgeGroup')['Survived'].apply(lambda x: (x == 0).sum())
    survivablity_rates = (age_group_deaths / age_group_counts) * 100
    
    # Plot the survivablity rates as a bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(survivablity_rates.index, survivablity_rates)
    plt.xlabel('Age Group')
    plt.ylabel('Survivablity Rate (%)')
    plt.title('Survivablity Rates by Age Group')
    plt.ylim(0, 100)
    
    # Add exact percentages on top of each bar
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, # Text alignment
                 f'{bar.get_height():.2f}%', ha='center', va='bottom', fontsize=12, color='white') # Formatting
    
    plt.show()

analyze_survivablity_by_age_group(df)
