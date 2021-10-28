from tkinter import *
from tkcalendar import *
import pytz
import datetime
import time


#  Timezone Code
country = 'Canada/Eastern'
country_1 = 'America/Arizona'
country_2 = 'America/Chicago'
country_3 = 'America/Denver'
country_4 = 'America/Los_Angeles'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("The time in {} is {}".format(country_1, local_time))
print("The time in {} is {}".format(country_2, local_time))
print("The time in {} is {}".format(country_3, local_time))
print("The time in {} is {}".format(country_4, local_time))
print("UTC in relation to local timezone is {}".format(datetime.datetime.utcnow()))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time (DST) is defined for this location")
    print("\tThe DST timezone name is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

#  Calendar code
root = Tk()
root.title('CELLS Calendar GUI')
root.iconbitmap('C:/Users/LVNo28/Desktop/cells_calendar/genesis.ico')
root.geometry("600x400")
root['background'] = "#0abab5"  # tiffany blue
# .configure(bg='aqua')

cell_calendar = Calendar(root, selectmode="day", year=2021, month=3, day=1)
cell_calendar.pack(pady=22, fill="both", expand=True)


def grab_date():
    cell_label.config(text=cell_calendar.date.today())


cell_button = Button(root, text="Today's Date", command=grab_date)
cell_button.pack(pady=22)

cell_label = Label(root, text="")
cell_label.pack(pady=22)

root.mainloop()

#  native calender reference

# # import calendar
#
# # Give us the week headers, each 3 letters long
# print(calendar.weekheader(3))
# print()  # these empty prints are just for spacing. they print a blank space
#
# # Give us the integer value of what the first weekday is (Monday is 0, Tuesday is 1, etc...)
# print(calendar.firstweekday())
# print()
#
# # Print out the specified month
# print(calendar.month(2019, 3))
# print()
#
# # Get the specified month in array form (if you don't understand the distinction, it's okay.)
# print(calendar.monthcalendar(2019, 3))
# print()
#
# # Print out the specified year
# print(calendar.calendar(2019))
# print()
#
# # Find out what day of the week (Mon is 0, Tue is 1, Wed is 2, etc...) the specified day is
# day_of_the_week = calendar.weekday(3000, 3, 8)
#
# # Tell us if the specified year is a leap year
# is_leap = calendar.isleap(2020)
# print(is_leap)
# print()
#
# # Specify how many leap days there are in the specified range of years (exclusive)
# how_many_leap_days = calendar.leapdays(2000, 3000)
# print(how_many_leap_days)
