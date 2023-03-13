# Initialize dictionary with default values. One line solution.
# Input:
# employees = [Kelly, Emma, John]
# defaults = {designation:Application Developer, salary: 8000}
# Output:
# {'Kelly': {'salary': 8000, 'designation': 'Application Developer'},
# 'John': {'salary': 8000, 'designation': 'Application Developer'},
# 'Emma': {'salary': 8000, 'designation': 'Application Developer'}}

employees = ['Kelly', 'Emma', 'John']
defaults = {'designation': 'Application Developer', 'salary': 8000}

res = {}
for i in employees:
    res[i] = defaults

print(res)
