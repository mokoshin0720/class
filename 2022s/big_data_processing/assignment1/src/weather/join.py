import pandas as pd
import matplotlib.pyplot as plt

weather =pd.read_csv("weather.csv", encoding="shift_jis")
weather["年月日"] = pd.to_datetime(weather["年月日"])
weather = weather.set_index("年月日")

df = make_index_datetime("2020_14204010.csv")
daily = convert_by_time_and_method(column, "D", "mean")

data = daily.join(weather)

plt.scatter(data.index, data[column])
plt.scatter(data.index, data["降水量の合計(mm)"])
plt.show()

data.corr()