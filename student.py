# student.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Data analyst Data.csv')

print("successfully loaded")

def number_unique_student():
    unique_students = data['First Name'].nunique()
    return unique_students

def count_in_college():
    in_college = (data['Attendee Status'] == 'Attending').sum()
    return in_college

def count_not_mentioned():
    not_mentioned = (data['Attendee Status'] != 'Attending').sum()
    return not_mentioned

def donut_attend():
    labels = 'Attending', 'Not Attending'
    sizes = [count_in_college(), count_not_mentioned()]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('static/img/donut_chart.png')
    plt.close(fig1)
    
def grad_year():
    # Calculate the distribution of graduation years
    grad_year_distribution = data['Year of Graduation'].value_counts()
    year_dist = grad_year_distribution.sort_index()  # Sort by year for a better visual representation
    print(year_dist, "\n")
    return year_dist

def py_exp():
    python_experience = data['Experience with python (Months)'].value_counts()
    python_experience_distribution = python_experience.sort_index()
    return python_experience_distribution

def top_college():
    gpa_by_college = data.groupby('College Name')['CGPA'].mean().sort_values(ascending=False).head(5)
    return gpa_by_college



    
    
donut_attend()
