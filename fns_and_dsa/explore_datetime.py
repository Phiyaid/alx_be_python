from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    
    
current_date = display_current_datetime()

number_of_days = int(input(f"Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date_and_time = (datetime.now() + timedelta(days = number_of_days))
    future_date = future_date_and_time.strftime("%Y-%m-%d")
    return future_date
    # print(f"Future date: {future_date}")


print(f"Future date: {calculate_future_date()}") 
