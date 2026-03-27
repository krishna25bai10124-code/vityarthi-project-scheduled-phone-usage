from datetime import datetime
import time
allowed_times = [(9, 10),(14, 15),(20, 21)]
def is_allowed():
    now = datetime.now()
    current_hour = now.hour
    for start, end in allowed_times:
        if start <= current_hour < end:
            return True
    return False
def show_schedule():
    print("\nAllowed Phone Usage Times:")
    for start, end in allowed_times:
        print(f" - {start}:00 to {end}:00")
def use_phone():
    if is_allowed():
        print("\nPhone usage allowed.")
        minutes = int(input("Enter how many minutes you want to use: "))
        print("Using phone")
        time.sleep(1)
        for i in range(minutes, 0, -1):
            print(f"Time left: {i} minute(s)")
            time.sleep(1)      
        print("Time's up! Stop using phone.\n")
    else:
        print("\nNot allowed right now. Focus on your work.\n")
while True:
    print("\nPhone Usage Manager")
    print("1. Check if phone usage is allowed")
    print("2. Use phone (with timer)")
    print("3. Show schedule")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        if is_allowed():
            print("You can use your phone now.")
        else:
            print("Not allowed right now.")
    elif choice == '2':
        use_phone()
    elif choice == '3':
        show_schedule()
    elif choice == '4':
        print("Exiting program. Stay focused!")
        break
    else:
        print("Invalid choice. Try again.")
