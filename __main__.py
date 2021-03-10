from datetime import date, time, datetime
from getRestriction import resctrictionDate

def main():
    print("*********** \"Pico y Placa\" Predictor ***********")
    print("************************************************")

    while True:    
        # Inputs
        licensePlate = input("\nEnter the license plate number: ")
        date = input("Enter the date yyyy-mm-dd: ")
        hour = input("Enter the time HH:mm : ")
        print("\n")

        # Concatenate date and hour
        dateTime = date + ' ' + hour
        
        try:
            # Convert date and hour in DateTime Object
            dateTime_obj = datetime.strptime(dateTime, '%Y-%m-%d %H:%M')
            
            # Get Pico y Placa restriction
            print("============> " + resctrictionDate(licensePlate[-1], dateTime_obj.weekday(), dateTime_obj.time()) + " <============")
            option = input("\n Do you want to make another query? - Y/N: ").lower()
            if option == 'n' or 'no':
                break
            
        except ValueError:
            print("The format of date or hour does not match. Please enter again")
        except Exception as e:
            print("Unexpected error: ", e)
            print("\nReview the error message and try again")
            break

if __name__ == '__main__':
    main()