import datetime as dt 

years = int(input("Please input your born years: "))
months = int(input("Please input your born months: "))
dates = int(input("Please input your born dates: "))

borned = dt.date(years,months,dates)

my_age_today = dt.date.today() - borned
change_my_age_today_into_years = my_age_today.days // 365
print(f"You were borned in {borned} and you are {change_my_age_today_into_years} years old and you were borned on {borned:%A}")