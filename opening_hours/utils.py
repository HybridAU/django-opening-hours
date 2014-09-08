import json

def is_open(date, opening_hours):
    if type(opening_hours) == str or type(opening_hours) == unicode:
        opening_hours = json.loads(opening_hours)
    try:
        day = []
        day_check = opening_hours[date.strftime("%A") + "_note"]
        if day_check == "true":
            day = opening_hours[date.strftime("%A")]
    except KeyError:
        return False
    for opening in day:
        start = opening[0].split(":")
        end = opening[1].split(":")
        start = int(start[0])*60 + int(start[1])
        end = int(end[0])*60 + int(end[1])
        if end < start:
            end += 1440  # 24*60 plus 1 day
        now = date.hour*60 + date.minute
        if start < now < end:
            return True
    return False

