from datetime import date


def get_dates_difference(date1, date2):
    return abs(date1 - date2)


try:
    date1 = date(2021, 12, 28)
    date2 = date(2018, 12, 23)
    print(get_dates_difference(date1, date2))
except Exception as e:
    print("An error occured...See details:", e)
