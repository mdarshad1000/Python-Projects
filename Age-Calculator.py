def ageCalculator(year, month, day):
    """This function calculates the current age of the user"""
    import datetime
    # Computes the current date
    today = datetime.datetime.now().date()
    # User's date of birth
    date_of_birth = datetime.date(year, month, day)
    # Computes the age of user
    age = int((today - date_of_birth).days / 365.25)
    print(age)


# User Input
year = int(input("Enter the year of birth: "))
month = int(input("Enter the month of birth: "))
day = int(input("Enter the day of birth: "))

ageCalculator(year, month, day)