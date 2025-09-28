# Display current date.
import datetime

def display_current_datetime():
    current_date = datetime.date.today()
    print(current_date.strftime("%Y-%m-%d %I:%M:%S"))

display_current_datetime()

# Calculate future date.
from datetime import timedelta
number = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    today = datetime.datetime.now()
    future_date = today + timedelta(days= number)
    print(future_date.strftime("%Y-%m-%d"))

calculate_future_date()