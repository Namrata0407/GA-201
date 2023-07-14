
employees = [
    {"name":"JOhn","salary":3000,"designation":"developer"},
     {"name":"abcd","salary":6000,"designation":"coder"},
      {"name":"sdfdf","salary":2450,"designation":"instructor"}
],


max_salary = 0
employees_final_data = None



for employee in employees:
    salary = employee["salary"]
    if salary > max_salary:
        max_salary = salary
        employees_final_data = employee


if employees_final_data is not None:
    print("Name: ", employees_final_data["name"],"Salary: ", employees_final_data["salary"],"Designation: ", employees_final_data["designation"])
    # print("Salary: ", employees_final_data["salary"])
    # print("Designation: ", employees_final_data["designation"])
else:
    print("no data found")

   