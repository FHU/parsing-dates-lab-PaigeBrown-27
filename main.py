#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    Jacob = {
        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
    }
    return Jacob[month]

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    Brooke = user_string.split()
    Brookie = Brooke[0]
    Texas_shaped_marshmallow = Brooke[1]
    Bean = Brooke[2]
    Ana = parse_month(Brookie)
    if len(Texas_shaped_marshmallow) == 2:
        Anthony = "0" + Texas_shaped_marshmallow[0:-1]

    else:
        Anthony = Texas_shaped_marshmallow[0:-1]
    Clay = Ana + "/" + Anthony + "/" + Bean
    return Clay

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    Greek = input()
    while Greek != -1:
        print(parse_date(Greek))
        Greek = input()