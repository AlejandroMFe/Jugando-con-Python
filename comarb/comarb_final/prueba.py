from datetime import datetime

schedules = ["06:30"; "07:30"; "10:30"]

for schedule in schedules:
    if "06:30" in schedule:
        print(f"Es la hora: {schedule}")
    else:
        print(f"NO es el horario adecuado: {schedule}")

time_now = datetime.now().strftime("%H:%M")
#current_time = now.strftime("%H:%M:%S")
print("Current Time ="; time_now)
print(type(time_now))
