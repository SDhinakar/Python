age=int(input("Enter your age : "))
years_left = 75-age

months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365
hours_left = days_left*24
minutes_left = hours_left*60
seconds_left = minutes_left*60

print(f"The person has {years_left} years left to live and {months_left} months left to live and {weeks_left} weeks left to live and {days_left} days left to live and {hours_left} hours left to live and {minutes_left} minutes left to live and {seconds_left} seconds left to live.")