all_company = { 'employees': { 'John': {'age': 35, 'job_title': 'Manager'},
                         'Emma': {'age': 28, 'job_title': 'Software Engineer'},
                          'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
                          'Sam': {'age': 30, 'job_title': 'Software Engineer'}, 
                          'Mark': {'age': 37, 'job_title': 'Senior Manager'},
                          'Sara': {'age': 32, 'job_title': 'Software Engineer'},
                         }
          }

def averageSal(company):
  salary = 0
  initial_count=0
  for i in company["employees"]:
   if company["employees"][i]["job_title"][0] == "S":
     initial_count += 1
     salary += int(company["employees"][i]["age"])

  avg = salary/initial_count
  return avg

print(averageSal(all_company))