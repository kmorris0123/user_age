import datetime

name = str(input("What is your name?: "))

current_age = int(input("How old are you?: "))


now = datetime.datetime.now()

current_year = int(now.year)


how_many_till = 100 - int(current_age)

add_years = how_many_till + current_year

add_years = str(add_years
	)
final = name +" will be 100 years old in the year "+add_years+"!"

print(final)


























