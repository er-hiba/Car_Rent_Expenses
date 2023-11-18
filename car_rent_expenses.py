# Asking if it's the end of the year
answer = input("Is it the end of the year ('Yes' or 'No'): ")

if answer == "No":
    # Collecting information for rental calculation if it's not the end of the year
    km = float(input("Enter the total number of kilometers driven: "))
    days = float(input("Enter the number of rental days: "))
    rate1 = float(input("Enter the rate for the initial kilometers: ")) 
    rate2 = float(input("Enter the rate for additional kilometers: "))
    rate3 = float(input("Enter the rate for extra kilometers: "))
    insurance = float(input("Enter insurance cost: "))

    # Calculation for total cost
    
    if 0 < km <= 100 :
        cost = rate1 * km + insurance * days
    elif 100 < km <= 1000 :
        cost = rate1 * 100 + rate2 * (km - 100) + insurance * days
    elif km > 1000 :
        cost = rate1 * 100 + rate2 * 900 + rate3 * (km - 1000) + insurance * days
    else:
        print("Invalid number of kilometers")  # Alert for invalid input
    
    # Displaying the total cost
    print(f"\n- The total cost of the rental is: {cost}") 

elif answer == "Yes" :
    # Collecting information for rental calculation if it's the end of the year
    rate4 = float(input("Enter the rate for end-of-year rental: "))
    days = float(input("Enter the number of rental days: "))
    insurance = float(input("Enter insurance cost: "))

    # Calculating the total cost of the rental for the end of the year
    cost = rate4 * days + insurance * days 

    # Displaying the total cost
    print(f"\n- The total cost of the rental at the end of the year is: {cost}")  
