from datetime import datetime

def PTO_calculator(from_date, to_date, from_hour, to_hour):
    if (from_date) == (to_date):
        from_time = datetime.combine(datetime.today(), from_hour)
        to_time = datetime.combine(datetime.today(), to_hour)
        requested_hours = ((to_time - from_time).total_seconds()) / 3600
    else:
        requested_hours = 8*(((to_date - from_date).days)+1)
    return requested_hours