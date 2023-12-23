def convert_time(time):
  if "AM" in time or "PM" in time:
    import datetime
    time_object = datetime.datetime.strptime(time, "%I:%M %p")
    time_string = time_object.strftime("%H:%M")
    return time_string
  else:
    import datetime
    time_object = datetime.datetime.strptime(time, "%H:%M")
    time_string = time_object.strftime("%I:%M %p")
    return time_string
time = "10:15 PM"

print(convert_time(time))
