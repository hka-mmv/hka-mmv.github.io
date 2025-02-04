# Titanic Survivability Analysis
# Analyze Gender Survival Rates Module

# Best used in notebook

# Author: Leon Gjinovci

import pandas as pd
import matplotlib.pyplot as plt

# Loading the cleaned Titanic dataset
df = pd.read_csv('data/titanic_cleaned.csv')

def visualize_general_survival_rate(df):
        # Calculate the counts of survivors and non-survivors
    survival_counts = df['Survived'].value_counts()
    
    # Labels and sizes for the pie chart
    labels = ['Did Not Survive', 'Survived']
    sizes = [survival_counts[0], survival_counts[1]]
    colors = ['lightcoral', 'lightskyblue']
    explode = (0, 0.1)  # "explode" the slice for survivors for emphasis
    
    # Function to format labels with absolute number and percentage
    def autopct_format(pct, allvals):
        absolute = int(round(pct/100.*sum(allvals)))
        return f'{pct:.1f}%\n({absolute})'
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct=lambda pct: autopct_format(pct, sizes),
            startangle=90, explode=explode)
    plt.title('General Survival Rate')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

# Visualize the general survival rate

def visualize_gender_survival_rates(df):
    # Calculate the total number of survivors by gender
    gender_survived_counts = df.groupby('Sex')['Survived'].sum()
    total_passengers_per_gender = df['Sex'].value_counts()
    
    # Prepare labels, sizes, and colors
    labels = ['Female Survivors', 'Male Survivors']
    sizes = [gender_survived_counts['female'], gender_survived_counts['male']]
    colors = ['lightskyblue', 'lightcoral']
    explode = (0.1, 0)  # "Explode" the female survivors slice for emphasis
    
    # Function to format labels with absolute number and percentage
    def autopct_format(pct, allvals):
        absolute = int(round(pct / 100. * sum(allvals)))
        return f'{pct:.1f}%\n({absolute})'
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct=lambda pct: autopct_format(pct, sizes),
            startangle=90, explode=explode)
    plt.title('Survival Rates by Gender')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

# Call the functions

# Visualize the general survival rate
visualize_general_survival_rate(df)

# Visualize the survival rates per gender
visualize_gender_survival_rates(df)