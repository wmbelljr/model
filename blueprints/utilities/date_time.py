from datetime import datetime as dt

def datetime_local():
    """
    Returns the local date and time as a string
    in this format 2024-04-07 06:38 \n
    This is the format used by sqlite database (and others too - I think)
"""
    date = dt.now()
    year = str(date.year)

    x = str(date.month)
    month = x if len(x) == 2 else f"0{x}"

    x = str(date.day)
    day = x if len(x) == 2 else f"0{x}"

    x = str(date.hour)
    hour = x if len(x) == 2 else f"0{x}"

    x = str(date.minute)
    minute = x if len(x) == 2 else f"0{x}"
    
    return f"{year}-{month}-{day} {hour}:{minute}"

def convert_str_to_date(str_date: str):
    """
    This converts a date-time back to a date object \n
    the fomat must be: 2024-04-07 18:11 \n
    It won't work otherwise.
    """
    dt_time = str_date.split(" ")
    date = dt_time[0]
    date = date.split("-")
    time = dt_time[1]
    time = time.split(':')
    dt_time = date + time
    d_t = []
    for item in dt_time: # convert all the strings to integers
        d_t.append(int(item))

    return dt(d_t[0], d_t[1], d_t[2], d_t[3], d_t[4])

# -------------- TESTS -------------------------
# x = datetime_local()
# print(f"Local Date/Time: {x}")
# d = convert_str_to_date(x)
# print(f"Date from string: {d}")
