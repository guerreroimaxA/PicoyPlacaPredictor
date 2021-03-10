from datetime import date, time, datetime

# Validate the last digit of the license plate number with the date of week
def restriction(licensePlate, date, schedule):
    licensePlateNumber = licensePlate[-1]

    # Concatenate date and hour
    dateTime = date + ' ' + schedule

    try:
        # Convert date and hour in DateTime Object
        dateTime_obj = datetime.strptime(dateTime, '%Y-%m-%d %H:%M')
        weekday = dateTime_obj.weekday()
        hour = dateTime_obj.time()

        # Check the restrictions
        if weekday == 0:
            if licensePlateNumber == '1' or licensePlateNumber == '2':
                return restrictionHour(hour)
        elif weekday == 1:
            if licensePlateNumber == '3' or licensePlateNumber == '4':
                return restrictionHour(hour)
        elif weekday == 2:
            if licensePlateNumber == '5' or licensePlateNumber == '6':
                return restrictionHour(hour)
        elif weekday == 3:
            if licensePlateNumber == '7' or licensePlateNumber == '8':
                return restrictionHour(hour)
        elif weekday == 4:
            if licensePlateNumber == '9' or licensePlateNumber == '0':
                return restrictionHour(hour)

        return False            
    except ValueError:
        print("The format of date or hour does not match. Please enter again")
    except Exception as e:
        print("Unexpected error: ", e)
        print("\nReview the error message and try again")
    

# Validate the time of the restriction
def restrictionHour(hour):
    time1 = time(7, 0)
    time2 = time(9, 30)
    time3 = time(16, 0)
    time4 = time(19, 30)
    
    if (hour >= time1 and hour <= time2) or (hour >= time3 and hour <= time4):
        return True
    else:
        return False


