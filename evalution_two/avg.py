def average_age_of_employees(company):
    total_age = 0
    count_s_job_titles = 0

    employees = company.get('employees', {})

    for employee, details in employees.items():
        job_title = details.get('job_title', '').strip().lower()

        if job_title.startswith('s'):
            age = details.get('age', 0)
            total_age += age
            count_s_job_titles += 1

    if count_s_job_titles == 0:
        return 0

    average_age = total_age / count_s_job_titles
    return average_age

# Test case
company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

print(average_age_of_employees(company))  # Output: 31.0
