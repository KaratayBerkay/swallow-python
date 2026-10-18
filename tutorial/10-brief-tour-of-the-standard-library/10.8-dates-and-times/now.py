# dates are easily constructed and formatted
import datetime as dt
now = dt.date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = dt.date(1964, 7, 31)
age = now - birthday
age.days
