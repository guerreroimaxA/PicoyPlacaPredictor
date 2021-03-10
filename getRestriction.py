from datetime import date, time, datetime

# Validate the last digit of the license plate number with the date of week
def resctrictionDate(licensePlateNumber, weekday, hour):
    if weekday == 0:
        if licensePlateNumber == '1' or licensePlateNumber == '2':
            return restrictionHour(hour)
        else:
            return "The car can be on the road"
    elif weekday == 1:
        if licensePlateNumber == '3' or licensePlateNumber == '4':
            return restrictionHour(hour)
        else:
            return "The car can be on the road"
    elif weekday == 2:
        if licensePlateNumber == '5' or licensePlateNumber == '6':
            return restrictionHour(hour)
        else:
            return "The car can be on the road"
    elif weekday == 3:
        if licensePlateNumber == '7' or licensePlateNumber == '8':
            return restrictionHour(hour)
        else:
            return "The car can be on the road"
    elif weekday == 4:
        if licensePlateNumber == '9' or licensePlateNumber == '0':
            return restrictionHour(hour)
        else:
            return "The car can be on the road"

# Validate the time of the restriction
def restrictionHour(hour):
    time1 = time(7, 0)
    time2 = time(9, 30)
    time3 = time(16, 0)
    time4 = time(19, 30)
    
    if (hour >= time1 and hour <= time2) or (hour >= time3 and hour <= time4):
        return "The car can NOT be on the road"
    else:
        return "The car can be on the road"


