import pandas as pd
from IPython.display import display
from tabulate import tabulate
import matplotlib.pyplot as plt

def make_index_datetime(filename: str):
    df = pd.read_csv(filename, encoding="shift_jis")

    df = pd.concat([df, df["日付"].str.split("/", expand=True)], axis=1)
    df.rename(columns={
        0: "YYYY",
        1: "MM",
        2: "DD"
    }, inplace=True)

    df["日時"] = df["YYYY"] + "-" + df["MM"] + "-" + df["DD"] + " " + (df["時"]-1).astype(str) + ":00:00"
    df["日時"] = pd.to_datetime(df["日時"])
    df = df.set_index("日時")
    
    return df

def plot_data(df: pd.DataFrame, columns: [str]):
    for c in columns:    
        plt.scatter(df.index, df[c])
    plt.show()
    
def convert_by_time_and_method(df: pd.DataFrame, column: str, time: str, method: str):
    if method == "mean":
        result = pd.DataFrame(df[column].resample(time).mean())
    
    return result
    
def make_index_date(filename: str):
    weather = pd.read_csv(filename, encoding="shift_jis")
    weather["年月日"] = pd.to_datetime(weather["年月日"])
    weather = weather.set_index("年月日")
    
    return weather

def join_air_pollution_and_weather(air_pollution: pd.DataFrame, weather: pd.DataFrame):
    return air_pollution.join(weather)

if __name__ == "__main__":
    column_pm = "PM2.5(ug/m3)"
    column_rain = "降水量の合計(mm)"

    air_pollution = make_index_datetime("2020_14204010.csv")
    daily_air_pollution = convert_by_time_and_method(air_pollution, column_pm, "D", "mean")
    
    weather = make_index_date("weather.csv")
    df = join_air_pollution_and_weather(daily_air_pollution, weather)

    plot_data(df, [column_pm, column_rain])
    
    print(df.corr())