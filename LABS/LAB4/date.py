import datetime

#1 Write a Python program to subtract five days from current date.
today = datetime.date.today()
new_date = datetime.date.today() - datetime.timedelta(days=5)

print("\nCurrent date:", today, "\nDate after subtracting 5 days:", new_date)

#2 Write a Python program to print yesterday, today, tomorrow.
yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

print("\nYesterday: " + str(yesterday), "\nToday: " + str(today), "\nTomorrow: " + str(tomorrow))

#3 Write a Python program to drop microseconds from datetime.
print("\nCurrent datetime without microseconds:", datetime.datetime.now().replace(microsecond=0))

#4 Write a Python program to calculate two date difference in seconds.
time1 = datetime.time(13, 24, 56)
time2 = datetime.time(13, 24, 59)
print("\nDifference in seconds: " + str(abs(time1.second-time2.second)))