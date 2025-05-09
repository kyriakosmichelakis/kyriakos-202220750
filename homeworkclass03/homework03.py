cal_to_seconds = 24 * 60 * 60
 
def unit_calculation(days):
    return days * cal_to_seconds
 
def convert_days():
    while True:
        try:
            days = float(input("Enter the number of days: "))
            if days < 0:
                print("Please enter a non-negative number of days.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
 
    seconds = unit_calculation(days)
    minutes = seconds / 60
    hours = minutes / 60
    print(f"{days} days is equal to:")
    print(f"{seconds} seconds")
    print(f"{minutes} minutes")
    print(f"{hours} hours")
 
convert_days()