import datetime

birthday = input("What is your birthdate? (DD/MM/YYYY) ")
birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
print("Your birthdate is:", birthdate)
print("Today is : ", datetime.date.today())

days_difference = datetime.date.today() - birthdate

age_days = days_difference.days
age_years = age_days // 365
age_months = age_days // 30

year_module = age_days % 365
month_module = year_module // 30
days = year_module % 30
days_month = age_months % 30

print("Your age is :")
print(age_years, " years, ", month_module, "months and ", days, " days")
print("---------------------- OR -------------------------")
print(age_months, " months and", days_month, " days")
print("---------------------- OR -------------------------")
print(age_days, " days")

