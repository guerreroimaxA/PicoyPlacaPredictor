from datetime import date, time, datetime
from getRestriction import restriction

def main():
    print("*********** \"Pico y Placa\" Predictor ***********")
    print("************************************************")

    while True:    
        # Inputs
        licensePlate = input("\nEnter the license plate number: ")
        date = input("Enter the date yyyy-mm-dd: ")
        hour = input("Enter the time HH:mm (24H): ")
        print("\n")

        # Get Pico y Placa restriction
        result = restriction(licensePlate, date, hour)
        if result == True:
            print("============> The car can NOT be on the road <============")
        elif result == False:
            print("============> The car can be on the road <============")
        
        option = input("\n Do you want to make another query? - Y/N: ").lower()
        if option == 'n' or option == 'no':
            break

if __name__ == '__main__':
    main()