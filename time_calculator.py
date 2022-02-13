def add_time(start, duration, day_of_week=False):

    index_of_days = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    arrays_of_days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]

    duration_tuple = duration.partition(":")
    print(duration_tuple)
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_min_tuple = start_tuple[2].partition(" ")
    start_hrs = int(start_tuple[0])
    start_mins = int(start_min_tuple[0])
    am_pm = start_min_tuple[2]
    am_pm_flip = {"AM": "PM", "PM": "AM"}

    amount_of_days = int(duration_hours / 24)

    end_mins = start_mins + duration_minutes
    if (end_mins >= 60):
        start_hrs += 1
        end_mins = end_mins % 60
    amount_of_am_pm_flip = int((start_hrs + duration_hours) / 12)
    end_hrs = (start_hrs + duration_hours) % 12

    end_mins = end_mins if end_mins > 9 else "0" + str(end_mins)
    end_hrs = end_hrs = 12 if end_hrs == 0 else end_hrs

    am_pm = am_pm_flip[am_pm] if amount_of_am_pm_flip % 2 == 1 else am_pm

    returnTime = str(end_hrs) + ":" + str(end_mins) + " " + am_pm
    if (day of week):
        day_of_week = day_of_week.lower()
        index = int((index_of_days[day_of_week]) + amount_of_days) % 7
        new_day = arrays_of_days[index]
        returnTime += ", " + new_day
        
    if(amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif (amount_of_days > 1):
      return returnTime + " (" + str(amount_of_days) + " days later)"
    
    return returnTime
