import calendar


def website_calendar(month, year):
    html = calendar.HTMLCalendar().formatmonth(theyear=year, themonth=month, withyear=True)
    return html.replace('\n', '')


month = 11
year = 2016
print(website_calendar(month, year))
