import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Data analyst Data.csv')

print("Successfully loaded")

def avg_cgpa():
    # Calculate the average CGPA
    average_gpa = data['CGPA'].mean()
    # Format the average CGPA to 2 decimal places
    formatted_average_gpa = "{:.2f}".format(average_gpa)
    return formatted_average_gpa

def gpa_by_city():
    gpa_by_city = data.groupby('City')['CGPA'].mean()
    return gpa_by_city


# Define a function to convert income to numeric values
def convert_income(income):
    if isinstance(income, str):
        income = income.replace('Lakh', '00000')
        income = income.replace('+', '')
        income = income.replace(' ', '')  # Remove any extra spaces
        if '-' in income:
            low, high = income.split('-')
            return (float(low) + float(high)) / 2
        else:
            return float(income)
    return income


#income tasks

def avg_income():
    # Apply the conversion function to the 'Family_Income' column
    data['Family Income'] = data['Family Income'].apply(convert_income)
    average_income = data['Family Income'].mean()
    formatted_average_income = "{:.2f}".format(average_income)
    return formatted_average_income


def corr():
    data['Family Income'] = data['Family Income'].apply(convert_income)
    
    # Now you can calculate the correlation and visualize the data
    correlation = data['Family Income'].corr(data['CGPA'])
    print(f"Correlation between family income and GPA: {correlation:.2f}")
    
    # Visualization of the relationship
    sns.scatterplot(x='Family_Income', y='CGPA', data=data)
    plt.title('Relationship between Family Income and GPA')
    plt.xlabel('Family Income')
    plt.ylabel('CGPA')
    plt.show()
    
def exp_salary():
    sns.scatterplot(data=data, x='CGPA', y='Expected salary (Lac)', hue='Family Income', size='Experience with python (Months)')
    plt.title('Expected Salary Variation')
    plt.xlabel('CGPA')
    plt.ylabel('Expected Salary')
    plt.show()
    
def event_status():
    event_field_distribution = data.groupby(['Events', 'Attendee Status']).size().unstack().fillna(0)
    return event_field_distribution


def leader_skills():
    #data['Leadership- skills'] = data['Leadership- skills'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
    # Group by 'Leadership- skills' and calculate mean CGPA and expected salary
    leadership_comparison = data.groupby('Leadership- skills')[['CGPA', 'Expected salary (Lac)']].mean()
    return leadership_comparison


def lecorr():
    # Clean the data and convert non-numeric values to NaN
    data['Leadership- skills'] = pd.to_numeric(data['Leadership- skills'], errors='coerce')
    data['Expected salary (Lac)'] = pd.to_numeric(data['Expected salary (Lac)'], errors='coerce')

    # Drop rows with NaN values in 'Leadership- skills' or 'Expected salary (Lac)' columns
    data.dropna(subset=['Leadership- skills', 'Expected salary (Lac)'], inplace=True)
    leadership_correlation = data['Leadership- skills'].corr(data['Expected salary (Lac)'])
    return leadership_correlation


def grad_yearfour():
    graduating = data[data['Year of Graduation'] == 2024].shape[0]
    return graduating

def data_event():
    data_science_events = data[data['Events'].str.contains('IS DATA SCIENCE FOR YOU?', case=False)]
    total_attendance_data_science = data_science_events['Attendee Status'].count()
    return total_attendance_data_science
    
    
def promotions():
    promotion_effectiveness = data['How did you come to know about this event?'].value_counts().head(1)
    return promotion_effectiveness

def high_exp():
    high_cgpa_experience = data[(data['CGPA'] > 8.5) & (data['Experience with python (Months)'] > 5)]
    avg_expected_salary = high_cgpa_experience['Expected salary (Lac)'].mean()
    return avg_expected_salary