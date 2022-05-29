numbers_of_centuries = int(input())

years = 100 * numbers_of_centuries
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{numbers_of_centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
