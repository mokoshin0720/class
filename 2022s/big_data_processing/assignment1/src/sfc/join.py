import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from cleansing import make_index_datetime, convert_by_time_and_method

def prepare_df1():
    rain = pd.read_csv("weather-rain.csv", encoding="shift-jis")
    rain["年月日"] = pd.to_datetime(rain["年月日"])
    rain = rain.set_index("年月日")
    
    return rain

def prepare_df2():
    theta = make_index_datetime("data/sfc/theta.csv")
    daily_co2 = convert_by_time_and_method(theta, "co2", "D", "mean")
    
    return daily_co2

def plot_data(df: pd.DataFrame, columns: [str]):
    for c in columns:
        plt.scatter(df.index, df[c], label=c)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    column_rain = "降水量の合計(mm)"
    column_co2 = "co2"
    
    rain = prepare_df1()
    daily_co2 = prepare_df2()
    
    df = rain.join(daily_co2)
    
    df.to_csv("combined.csv")
    
    plot_data(df, [column_rain, column_co2])
    
    print(df.corr())