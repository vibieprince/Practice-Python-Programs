def ConvertTime(time):
    from datetime import datetime
    try:
        time24 = datetime.strptime(time,"%I:%M %p").strftime("%H:%M")
        return time24
    except ValueError:
        return "Invalid Time Format! Use HH:MM AM/PM"
    

time12 = input("Enter time in 12-hour format (HH:MM AM?PM)")
Converted = ConvertTime(time12)

print("Time in 24-hour format : ",Converted)