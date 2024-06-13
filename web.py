from flask import Flask, render_template
from student import number_unique_student, count_in_college, count_not_mentioned, grad_year,py_exp, top_college
from analysis import avg_cgpa, gpa_by_city, avg_income, event_status, leader_skills, lecorr, grad_yearfour, data_event

app = Flask(__name__)

@app.route('/')
def unique_student():
    unique_student_count = number_unique_student()
    in_college_count = count_in_college()
    not_mentioned_count = count_not_mentioned()
    graduation_year = grad_year()
    python_experience =py_exp()
    top_5_college = top_college()

    return render_template('home.html', unique_student_count=unique_student_count,
                           in_college_count=in_college_count,
                           not_mentioned_count=not_mentioned_count,
                           graduation_year=graduation_year,
                           python_experience=python_experience,
                           top_5_college = top_5_college,
                           )
    

@app.route('/analysis')
def analysis():
    average_cgpa = avg_cgpa()
    average_cgpa_city = gpa_by_city()
    average_family_income = avg_income()
    event_attending_status =event_status()
    leadership_skills= leader_skills()
    leadership_correlation = lecorr()
    year_of_grad = grad_yearfour()
    datascience_events =data_event()
    return render_template('analysis.html', average_cgpa=average_cgpa,
                           average_cgpa_city=average_cgpa_city,
                           average_family_income=average_family_income,
                           event_attending_status=event_attending_status,
                           leadership_skills=leadership_skills,
                           leadership_correlation=leadership_correlation,
                           year_of_grad=year_of_grad,
                           datascience_events=datascience_events)
           

if __name__ == '__main__':
    app.run(debug=True)
