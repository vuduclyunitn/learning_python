# Credit https://twitter.com/python_tip/status/1148354152260612097?s=20

# A list of tuples including employee information
employees = [
        ('Heather', 'Data Scientist', 12500),
        ('DeShawn', 'Senior Analysit', 105000),
        ('Kevin', 'Senior Analyst', 98000),
        ('Bridget', 'Analyst', 75000),
        ('Mark', 'Analyst', 70000),
        ('Adam', 'Analyst', 68000)
        ]

# Set the column width
w = 20

# Print the table with a header row
# Header row ... there's no need to pad the final column
print("NAME".ljust(w) + "JOB TITLE".ljust(w) + "SALARY")

# the data rows
for name, job, salary in employees:
    print(name.ljust(w) + job.ljust(w) + '{:,.0f}'.format(salary))

