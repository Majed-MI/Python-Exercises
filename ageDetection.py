# input taking year of birth or age
yearAge = int(input("What is your Age / Year of Birth?\n"))
# declaring age or year as false so that if condition is ok then it will be true
isAge = False
isYear = False
# condition for year of birth
if len(str(yearAge)) == 4:
    isYear = True
# condition for age
else:
    isAge = True
# too old age condition(error handling)
if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()
# too old age condition(error handling)
if(yearAge>145 and isAge):
    print("You seem to be the oldest person alive")
    exit()
# not born yet condition(error handling)
if(yearAge>2020):
    print("You are not Born yet")
    exit()
# not born yet condition(error handling)
if(yearAge<0 and isAge):
    print("You are not Born yet")
    exit()
# if age is valid then putting the age in year of birth format to ease program
if isAge:
    yearAge = 2020 - yearAge
# prtinting 100 years age
print(f"You will be 100 years old in {yearAge+100}")
# printing interested year which is input taken
interestedYear = int(input("Enter the year you want to know your age in : \n"))
print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")