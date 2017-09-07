from datetime import date
# What day of the week was your day of birth?
birthday = date(1993,6,3)
fmt = "It's %A %B %d, %Y"
prt =birthday.strftime(fmt)
print(prt)