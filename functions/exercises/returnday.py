# define function with one parameter
def return_day(num):
    # store days in a list
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # check to see if num isn't less than 0 9r greater than 6
    if num > 0 or num > len(days):
        # use num -1 because lists start at 0
        return days[num-1]
    return None

answer = return_day(1)
print(answer)