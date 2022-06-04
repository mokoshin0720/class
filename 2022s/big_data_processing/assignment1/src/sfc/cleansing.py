import pandas as pd

def make_index_datetime(filename: str):
    df = pd.read_csv("data/sfc/theta.csv")
    
    df = pd.concat([df, df["timestamp"].str.split("/", 2, expand=True)], axis=1)
    df.rename(columns={
        0: "YYYY",
        1: "MM",
        2: "DDTime",
    }, inplace=True)
    
    df = pd.concat([df, df["DDTime"].str.split(" ", expand=True)], axis=1)
    df.rename(columns={
        0: "DD",
        1: "time",
    }, inplace=True)
    
    df= df.drop("DDTime", axis=1)
    
    df["datetime"] = df["YYYY"] + "-" + df["MM"] + "-" + df["DD"] + " " + df["time"]
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.set_index("datetime")
    
    return df

def convert_by_time_and_method(df: pd.DataFrame, column: str, time: str, method: str):
    if method == "mean":
        result = pd.DataFrame(df[column].resample(time).mean())
    return result

if __name__ == "__main__":
    theta = make_index_datetime("data/sfc/theta.csv")
    daily_co2 = convert_by_time_and_method(theta, "co2", "D", "mean")
    daily_co2.to_csv("daily_co2.csv")