def practice_counts():
    import datetime
    first_day = datetime.date(2020,3,12)
    last_day = datetime.date.today()
    interval = last_day - first_day
    n = interval.days
    print("*" * 22)
    print(f" 第{n}练: {last_day} ")
    print("*" * 22)

practice_counts()