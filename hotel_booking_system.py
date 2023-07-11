import re
import calendar

# Dictionary of user accounts with usernames as keys and passwords as values
users_accounts = {'despoina': 123, 'sofia': 321}

# Dictionary of available rooms with room names as keys and room numbers as values
availale_rooms = {'Room3': 32, 'Room4': 45}

# Dictionary of unavailable rooms with room names as keys and room numbers as values
unavailable_rooms = {'Room1': 29, 'Room2': 9}

# Welcome message
print("Welcome to the Hotel Booking System\nLogin is required")

# Function to check user credentials
def check_credentials(username, password, value, option):
    attempts = 0
    while attempts < 2:
        # Check if admin credentials are entered
        if (username == 'root' and password == 'admin'):
            print(f"You have logged in as admin\nWelcome {username}")
            while True:
                if admin_options(option=option):
                    break
            return True
        
        # Check if client credentials are entered
        elif (username in users_accounts) and (int(value) == users_accounts[username]):
            print(f"You have logged in as a client\nWelcome {username}")
            while True:
                if user_options(option=option):
                    break
            return True
        
        # Invalid credentials
        else:
            attempts += 1
            print("Wrong credentials.\nPlease try again.")
            username = input("Username: ")
            password = input("Password: ")
    
    # Maximum attempts reached
    print("You have exceeded the maximum number of attempts. Exiting...")
    return False

# Function for admin options
def admin_options(option):
    print("How would you like to proceed?: ")
    print("\n1) Available rooms")
    print("2) Registered Accounts")
    print("3) Restaurant Reservation")
    print("4) Logout")
    while True:
        if option == 1:
            print("These are the available rooms:")
            for i in availale_rooms:
                print(f"The following room is \033[92mavailable\033[0m: {i}")
            for i in unavailable_rooms:
                print(f"The following room is \033[91munavailable\033[0m: {i}")
            return True
        elif option == 2:
            print("These are the registered accounts: ")
            for i in users_accounts:
                print(i)
            return True
        elif option == 3:
            print("These are the available hours for reservation: ")
            return True
        elif option == 4:
            print("You have successfully logged out")
            exit()
        else:
            option = int(input("Input here: "))

# Function to check if the email address is valid
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
# Available days for restaurant reservations
available_days = [5, 7, 12, 18, 23]

# Function to generate the calendar and mark available days
def generate_calendar(year, month, available_days):
    # Create a calendar instance
    cal = calendar.Calendar()

    # Generate the calendar for the specified year and month
    month_calendar = cal.monthdatescalendar(year, month)

    # Print the calendar header
    print(f"{calendar.month_name[month]} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Iterate over each week in the month calendar
    for week in month_calendar:
        # Iterate over each day in the week
        for day in week:
            # Check if the day is within the current month
            if day.month == month:
                # Mark the day as available if it is in the available_days list
                if day.day in available_days:
                    day_display = f"\033[92m{day.day:2d}\033[0m"
                else:
                    day_display = f"{day.day:2d}"
            else:
                day_display = "  "
            
            print(day_display, end=" ")

        print()

    choice = int(input("Enter the date for reservation: "))
    if choice in available_days:
        print(f"The date you chose is: {calendar.month_name[month]} {choice}, {year}")
    else:
        print("The chosen date is not available for reservation.")

# Usage example
year = 2023
month = 7

# Function for user options
def user_options(option):
    print("How would you like to proceed?: ")
    print("1) Cancellation Request")
    print("2) Restaurant Reservation")
    print("3) Logout")
    while True:
        if option == 1:
            print("For your cancellation request, your email address is required: ")
            email = input("Email address: ")
            if is_valid_email(email):
                print("Valid email address.")
                print("The reservation has successfully been cancelled.")
            else:
                print("Invalid email address.")
            return True
        elif option == 2:
            print("For which day of the week would you like to reserve?: ")
            generate_calendar(year, month, available_days)
            return True
        elif option == 3:
            print("These are the available hours for reservation: ")
            return True
        else:
            option = int(input("Input here: "))

# Get username and password from the user
username = input("Username: ")
password = input("Password: ")

# Check the user credentials and login
if check_credentials(username=username, password=password, value=password, option=0):
    exit()
