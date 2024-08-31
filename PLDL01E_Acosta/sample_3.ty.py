# initialize the value of NetIncome, GrossIncome, TotalDeduction, NameOfEmployee, PagibigContribution
NetIncome = 0
GrossIncome = 0
TotalDeduction = 0
NameOfEmployee = ""
PagibigContribution = 100.00

# input the value of NameOfEmployee, rate per hour, number of hours per day, number of days per week, number of weeks per month, sss contribution, philhealth contribution, and tax contribution
NameOfEmployee = str(input("Enter employee name"))
rate_per_hour = float(input("Enter employee's rate per hour:"))
num_hrs_per_day = float(input("Enter employee's number of hours per day:"))
num_days_per_week = int(input("Enter employee's number of days per week:"))
num_week_per_month = int(input("Enter employee's number of weeks per month:"))
sss_contribution = float(input("Enter employee's sss contribution:"))
philhealth_contribution = float(input("Enter employee's philhealth contribution:"))
tax_contribution = float(input("Enter employee's tax contribution:"))

# setting the formula for gross income, total deduction, and net income
GrossIncome = rate_per_hour * num_hrs_per_day * num_days_per_week * num_week_per_month
TotalDeduction = sss_contribution + philhealth_contribution + tax_contribution + PagibigContribution
NetIncome = GrossIncome - TotalDeduction

# displaying the computed value for name of employee, net income, gross income,and total deduction
print("Employee Name:",NameOfEmployee)
print("Employee Name:",NetIncome)
print("Employee Name:",GrossIncome)
print("Employee Name:",TotalDeduction)
