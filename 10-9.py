from datetime import date ,timedelta
# When will you be (or when were you) 10,000 days old?
birthday = date(1993,6,3)
fmt = "It's %A %B %d, %Y"
one_day = timedelta(days=1)

ten_thusands_day = one_day*10000+birthday
prt =ten_thusands_day.strftime(fmt)
print(prt)