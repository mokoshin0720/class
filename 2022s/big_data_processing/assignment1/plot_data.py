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

def plot_data(df: pd.DataFrame, column: str):
    plt.scatter(df.index, df[column])
    plt.show()
    
def convert_by_time_and_method(column: str, time: str, method: str):
    if method == "mean":
        result = pd.DataFrame(df[column].resample(time).mean())
    
    return result
    
if __name__ == "__main__":
    df = make_index_datetime("2020_14204010.csv")
    df = convert_by_time_and_method("PM2.5(ug/m3)", "D", "mean")
    plot_data(df, "PM2.5(ug/m3)")