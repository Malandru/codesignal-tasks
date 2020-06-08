from datetime import datetime


def maliciousProgram(curDate, changes):
    global original
    date_format = "%d %b %Y %H:%M:%S"
    original = datetime.strptime(curDate, date_format)
    keys = ['day', 'month', 'year', 'hour', 'minute', 'second']
    param = dict([(k, eval(f'original.{k} + c')) for k, c in zip(keys, changes)])
    try: spoiled = original.replace(**param)
    except: spoiled = original
    return datetime.strftime(spoiled, date_format)


curDate = "15 Mar 1998 12:09:59"
changes = [-2, 0, 9, 1, 3, 1]
print(maliciousProgram(curDate, changes))
