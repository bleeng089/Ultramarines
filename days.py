import pandas as pd
pd.set_option('display.max_rows', 365)
pd.set_option('display.max_columns', 365)
pd.set_option('display.width', 1000)

start_date = input("What is the starting date? YYYY-MM-DD: ")
end_date = input("What is the ending date? YYYY-MM-DD: ")

dates = pd.date_range(start=start_date, end=end_date)
dframe = pd.DataFrame({"date": dates})
dframe["day_of_week"] = dframe["date"].dt.dayofweek
dframe["day_of_week"] = dframe["day_of_week"].map({
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
})
print(dframe)